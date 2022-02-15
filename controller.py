# -*- coding: utf-8 -*-

# python imports
from math import degrees
# pyfuzzy imports
from fuzzy.storage.fcl.Reader import Reader

# myclasses imports
from fuzzificaion import Pa_fuzzification, Pv_fuzzification, Force_fuzzification, Cv_fuzzification

force_fuzzification = Force_fuzzification()
pa_fuzzification = Pa_fuzzification()
pv_fuzzification = Pv_fuzzification()
cv_fuzzification = Cv_fuzzification()

class FuzzyController:

    def __init__(self, fcl_path):
        self.system = Reader().load_from_file(fcl_path)

    def _make_input(self, world):
        return dict(
            cp=world.x,
            cv=world.v,
            pa=degrees(world.theta),
            pv=degrees(world.omega)
        )

    def _make_output(self):
        return dict(
            force=0.
        )

    def fuzzify(self, input):
        fuzzy_pa = pa_fuzzification.calc_fuzzy_pa(input['pa'])
        fuzzy_pv = pv_fuzzification.calc_fuzzy_pv(input['pv'])
        fuzzy_cv = cv_fuzzification.calc_fuzzy_cv(input['cv'])
        return fuzzy_pa, fuzzy_pv, fuzzy_cv

    def inference(self, pa, pv, cv, complex):
        right_fast, right_slow, left_fast, left_slow, stop = ([] for i in range(5))

        # rule0
        stop.append(max(min(pa['up'], pv['stop']),min(pa['up_right'], pv['ccw_slow']) ,min(pa['up_left'], pv['cw_slow'])))
        right_fast.append(min(pa['up_more_right'], pv['ccw_slow']))
        right_fast.append(min(pa['up_more_right'], pv['cw_slow']))
        left_fast.append(min(pa['up_more_left'], pv['cw_slow']))
        if complex:
            left_fast.append(min(pa['up_more_left'], pv['ccw_slow'], cv['left_fast'])) #rule4'
            right_fast.append(min(pa['up_more_right'], pv['cw_fast'], cv['right_fast'])) #rule6'
            right_slow.append(min(pa['up_right'], pv['cw_slow'], cv['right_fast']))#rule26'
            left_slow.append(min(pa['up_left'], pv['ccw_fast'], cv['left_fast'])) #rule34'
            left_slow.append(min(pa['up'], pv['ccw_fast'], cv['left_fast'])) #rule39'
        else:
            left_fast.append(min(pa['up_more_left'], pv['ccw_slow'])) #rule4
            right_fast.append(min(pa['up_more_right'], pv['cw_fast'])) #rule6
            right_fast.append(min(pa['up_right'], pv['cw_slow'])) #rule26
            left_fast.append(min(pa['up_left'], pv['ccw_fast'])) #rule34
            left_fast.append(min(pa['up'], pv['ccw_fast'])) #rule39

        left_slow.append(min(pa['up_more_right'], pv['ccw_fast']))
        #rule7
        right_slow.append(min(pa['up_more_left'], pv['cw_fast']))
        left_fast.append(min(pa['up_more_left'], pv['ccw_fast']))
        right_fast.append(min(pa['down_more_right'], pv['ccw_slow']))
        stop.append(min(pa['down_more_right'], pv['cw_slow']))
        # rule11
        left_fast.append(min(pa['down_more_left'], pv['cw_slow']))
        stop.append(min(pa['down_more_left'], pv['ccw_slow']))
        stop.append(min(pa['down_more_right'], pv['ccw_fast']))
        stop.append(min(pa['down_more_right'], pv['cw_fast']))
        stop.append(min(pa['down_more_left'], pv['cw_fast']))
        # rule16
        stop.append(min(pa['down_more_left'], pv['ccw_fast']))
        right_fast.append(min(pa['down_right'], pv['ccw_slow']))
        right_fast.append(min(pa['down_right'], pv['cw_slow']))
        left_fast.append(min(pa['down_left'], pv['cw_slow']))
        left_fast.append(min(pa['down_left'], pv['ccw_slow']))
        # rule21
        stop.append(min(pa['down_right'], pv['ccw_fast']))
        right_slow.append(min(pa['down_right'], pv['cw_fast']))
        stop.append(min(pa['down_left'], pv['cw_fast']))
        left_slow.append(min(pa['down_left'], pv['ccw_fast']))
        right_slow.append(min(pa['up_right'], pv['ccw_slow']))
        # rule27
        right_fast.append(min(pa['up_right'], pv['stop']))
        left_slow.append(min(pa['up_left'], pv['cw_slow']))
        left_fast.append(min(pa['up_left'], pv['ccw_slow']))
        left_fast.append(min(pa['up_left'], pv['stop']))
        # rule31
        left_fast.append(min(pa['up_right'], pv['ccw_fast']))
        right_fast.append(min(pa['up_right'], pv['cw_fast']))
        right_fast.append(min(pa['up_left'], pv['cw_fast']))
        right_fast.append(min(pa['down'], pv['stop']))
        # rule36
        stop.append(min(pa['down'], pv['cw_fast']))
        stop.append(min(pa['down'], pv['ccw_fast']))
        left_slow.append(min(pa['up'], pv['ccw_slow']))
        right_slow.append(min(pa['up'], pv['cw_slow']))
        # rule41
        right_fast.append(min(pa['up'], pv['cw_fast']))
        stop.append(min(pa['up'], pv['stop']))

        return dict(
            left_fast=max(left_fast),
            left_slow=max(left_slow),
            stop=max(stop),
            right_slow=max(right_slow),
            right_fast=max(right_fast)
        )

    def defuzzify(self, x):
        n = 10000
        delta = 200. / n
        pointsOfForce = [-100. + i * delta for i in range(n + 1)]

        numerator = 0.
        denominator = 0.
        for point in pointsOfForce:
            lf = force_fuzzification.left_fast(point)
            if lf > x['left_fast']:
                lf = x['left_fast']
            ls = force_fuzzification.left_slow(point)
            if ls > x['left_slow']:
                ls = x['left_slow']
            stop = force_fuzzification.stop(point)
            if stop > x['stop']:
                stop = x['stop']
            rs = force_fuzzification.right_slow(point)
            if rs > x['right_slow']:
                rs = x['right_slow']
            rf = force_fuzzification.right_fast(point)
            if rf > x['right_fast']:
                rf = x['right_fast']

            res = max(lf, ls, stop, rs, rf)
            numerator += res * point * delta
            denominator += res * delta
        try:
            force = numerator / denominator
        except ZeroDivisionError:
            force = 0
        return force

    def calc_force(self, input):
        fuzzy_pa, fuzzy_pv, fuzzy_cv = self.fuzzify(input)
        fuzzy_force = self.inference(fuzzy_pa, fuzzy_pv, fuzzy_cv, True)
        force = self.defuzzify(fuzzy_force)
        return force

    def decide(self, world):
        output = self._make_output()
        # self.system.calculate(self._make_input(world), output)
        # return output['force']
        force = self.calc_force(self._make_input(world))
        return force
