# Fuzzy Inverted Pendulum
The inverted pendulum system is an example commonly found in control system textbooks and research literature. This pendulum is unstable and without additional help will fall over. It is inverted to a cart that can only move along the x-axis. The goal is to keep the pendulum fixed on the top of the cart in reverse.  
  
Basically, this project consists of an inverted pendulum simulator and a controller which work based on a **Fuzzy Expert System** algorithm.  
  
This project was implemented using **pygame** in *python2.7*.

## Fuzzy Expert System
The *FuzzyController* class in **controller.py** module, loads an *FCL* file to decide how much force needs to be applied to the cart in each cycle of simulation.
*FCL* files can be found in **controllers** directory.  
 
### Input and Output
FES *inputs* are:  
> **pa**: pendulum central angle, *radian*
> 
> **pv**: pendulum angular velocity, *m/s*
>
> **cp**: cart position, *m*
> 
> **cv**: cart velocity, *m/s*  

FES *output* is:
> **force**: force applied on cart, *newton*

### Fuzzy sets
Defined fuzzy sets can be found in [this directory](https://github.com/hedzd/Fuzzy-inverted-pendulum/tree/main/Fuzzy%20sets%20images)

## FES implementation
As any other fuzzy expert system, the controller is consisted of 3 main parts:  
1. **Fuzzification:** For this purpose, fuzzy sets have been defined and according to the membership functions, the degree of belonging of each value to each set is calculated.
2. **Inference:** The truth value for the premise of each rule is computed, and applied to the conclusion part of each rule.
3. **Defuzzification:** The process of conversion of fuzzy quantity into a absolute value. Defuzzification was implemented using *Centroid method*. 

## Getting Started


### Install

    $ sudo pip install virtualenv
    $ virtualenv -p python2.7 venv
    $ source venv/Scripts/activate
    
    then install required libraries

### Physical parameters of simulator

You can see all the parameters in **world.py** module.
Also these parameters can be modified using configuration files located in **configs** directory.




