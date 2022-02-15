class Pa_fuzzification:
    def __init__(self):
        pass

    def up_more_right(self, x):
        if 0 < x <= 30:
            return (1.0 / 30) * x
        if 30 < x < 60:
            return (-1.0 / 30) * x + 2
        else:
            return 0

    def up_right(self, x):
        if 30 < x <= 60:
            return (1.0 / 30) * x - 1
        if 60 < x < 90:
            return (-1.0 / 30) * x + 3
        else:
            return 0

    def up(self, x):
        if 60 < x <= 90:
            return (1.0 / 30) * x - 2
        if 90 < x < 120:
            return (-1.0 / 30) * x + 4
        else:
            return 0

    def up_left(self, x):
        if 90 < x <= 120:
            return (1.0 / 30) * x - 3
        if 120 < x < 150:
            return (-1.0 / 30) * x + 5
        else:
            return 0

    def up_more_left(self, x):
        if 120 < x <= 150:
            return (1.0 / 30) * x - 4
        if 150 < x < 180:
            return (-1.0 / 30) * x + 6
        else:
            return 0

    def down_more_left(self, x):
        if 180 < x <= 210:
            return (1.0 / 30) * x - 6
        if 210 < x < 240:
            return (-1.0 / 30) * x + 8
        else:
            return 0

    def down_left(self, x):
        if 210 < x <= 240:
            return (1.0 / 30) * x - 7
        if 240 < x < 270:
            return (-1.0 / 30) * x + 9
        else:
            return 0

    def down(self, x):
        if 240 < x <= 270:
            return (1.0/30) * x - 8
        if 270 < x < 300:
            return (-1.0 / 30) * x + 10
        else:
            return 0

    def down_right(self, x):
        if 270 < x <= 300:
            return (1.0 / 30) * x - 9
        if 300 < x < 330:
            return (-1.0 / 30) * x + 11
        else:
            return 0

    def down_more_right(self, x):
        if 300 < x <= 330:
            return (1.0 / 30) * x - 10
        if 330 < x < 360:
            return (-1.0 / 30) * x + 12
        else:
            return 0

    def calc_fuzzy_pa(self, pa):
        return dict(
            up_more_right=self.up_more_right(pa),
            up_right=self.up_right(pa),
            up=self.up(pa),
            up_left=self.up_left(pa),
            up_more_left=self.up_more_left(pa),
            down_more_left=self.down_more_left(pa),
            down_left=self.down_left(pa),
            down=self.down(pa),
            down_right=self.down_right(pa),
            down_more_right=self.down_more_right(pa)
        )


class Pv_fuzzification:
    def __init__(self):
        pass

    def cw_fast(self, x):
        if -200 < x <= -100:
            return -0.01 * x - 1
        if x < -200:
            return 1
        else:
            return 0

    def cw_slow(self, x):
        if -200 < x <= -100:
            return 0.01 * x + 2
        if -100 < x < 0:
            return -0.01 * x
        else:
            return 0

    def stop(self, x):
        if -100 < x <= 0:
            return 0.01 * x + 1
        if 0 < x < 100:
            return -0.01 * x + 1
        else:
            return 0

    def ccw_slow(self, x):
        if 0 < x <= 100:
            return 0.01 * x
        if 100 < x < 200:
            return -0.01 * x + 2
        else:
            return 0

    def ccw_fast(self, x):
        if 100 < x <= 200:
            return 0.01 * x - 1
        if x > 200:
            return 1
        else:
            return 0

    def calc_fuzzy_pv(self, pv):
        return dict(
            cw_fast=self.cw_fast(pv),
            cw_slow=self.cw_slow(pv),
            stop=self.stop(pv),
            ccw_slow=self.ccw_slow(pv),
            ccw_fast=self.ccw_fast(pv)
        )


class Force_fuzzification:
    def __init__(self):
        pass

    def left_fast(self, x):
        if -100 < x <= -80:
            return 0.05 * x + 5
        if -80 < x < -60:
            return -0.05 * x + -3
        else:
            return 0

    def left_slow(self, x):
        if -80 < x <= -60:
            return 0.05 * x + 4
        if -60 < x < 0:
            return (-1.0 / 60) * x
        else:
            return 0

    def stop(self, x):
        if -60 < x <= 0:
            return (1.0 / 60) * x + 1
        if 0 < x < 60:
            return (-1.0 / 60) * x + 1
        else:
            return 0

    def right_slow(self, x):
        if 0 < x <= 60:
            return (1.0 / 60) * x
        if 60 < x < 80:
            return -0.05 * x + 4
        else:
            return 0

    def right_fast(self, x):
        if 60 < x <= 80:
            return 0.05 * x + -3
        if 80 < x < 100:
            return -0.05 * x + 5
        else:
            return 0


class Cv_fuzzification:
    def __init__(self):
        pass

    def left_fast(self, x):
        if -5 < x <= -2.5:
            return -0.4 * x - 1
        if x < -5:
            return 1
        else:
            return 0

    def left_slow(self, x):
        if -5 < x <= -1:
            return 0.25 * x + 1.25
        if -1 < x < 0:
            return -1 * x
        else:
            return 0

    def stop(self, x):
        if -1 < x <= 0:
            return x + 1
        if 0 < x < 1:
            return -1 * x + 1
        else:
            return 0

    def right_slow(self, x):
        if 0 < x <= 1:
            return x
        if 1 < x < 5:
            return -0.25 * x + 1.25
        else:
            return 0

    def right_fast(self, x):
        if 2.5 < x <= 5:
            return 0.4 * x - 1
        if 5 < x:
            return 1
        else:
            return 0

    def calc_fuzzy_cv(self, cv):
        return dict(
            left_fast=self.left_fast(cv),
            left_slow=self.left_slow(cv),
            stop=self.stop(cv),
            right_slow=self.right_slow(cv),
            right_fast=self.right_fast(cv)
        )