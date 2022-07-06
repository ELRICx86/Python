# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:59:47 2020

@author: AAS
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# New Antecedent/Consequent objects hold universe variables and membership
# functions
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality' )
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service' )
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip' )
# Auto-membership function population is possible with .automf(3, 5, or 7)
#quality.automf(3)
#service.automf(3)

quality[ 'poor' ] = fuzz.trimf(quality.universe, [ 0, 0, 5])
quality[ 'acceptable' ] = fuzz.trimf(quality.universe, [ 0, 5, 10])
quality[ 'amazing' ] = fuzz.trimf(quality.universe, [ 5, 10, 10])

service[ 'bad' ] = fuzz.trimf(service.universe, [ 0, 0, 5])
service[ 'decent' ] = fuzz.trimf(service.universe, [ 0, 5, 10])
service[ 'great' ] = fuzz.trimf(service.universe, [ 5, 10, 10])
# Custom membership functions can be built interactively with a familiar,
# Pythonic API
tip[ 'low' ] = fuzz.trimf(tip.universe, [ 0, 0, 13])
tip[ 'medium' ] = fuzz.trimf(tip.universe, [ 0, 13, 25])
tip[ 'high' ] = fuzz.trimf(tip.universe, [ 13, 25, 25])


# You can see how these look with .view()
quality[ 'poor' ].view()
service['great'].view()
tip['high'].view()

rule1 = ctrl.Rule(quality[ 'poor' ] | service[ 'bad' ], tip[ 'low' ])
rule2 = ctrl.Rule(service[ 'decent' ], tip[ 'medium' ])
rule3 = ctrl.Rule(service[ 'great' ] | quality[ 'amazing' ], tip[ 'high' ])
#rule1.view()
#rule2.view()

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input[ 'quality' ] = 6.5
tipping.input[ 'service' ] = 9.8
# Crunch the numbers
tipping.compute()
print (tipping.output[ 'tip' ])
tip.view(sim=tipping)
