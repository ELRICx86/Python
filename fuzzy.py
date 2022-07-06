import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# New Antecedent/Consequent objects hold universe variables and membership
# functions
funding = ctrl.Antecedent(np.arange(0, 101, 1), 'funding' )
staffing = ctrl.Antecedent(np.arange(0, 101, 1), 'staffing' )
risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk' )
# Auto-membership function population is possible with .automf(3, 5, or 7)
#quality.automf(3)
#service.automf(3)

funding[ 'inadequate' ] = fuzz.trapmf(funding.universe, [ 0,0, 20, 30])
funding[ 'marginal' ] = fuzz.trimf(funding.universe, [ 20, 50, 80])
funding[ 'adequate' ] = fuzz.trapmf(funding.universe, [ 60, 80, 100,100])

#service[ 'bad' ] = fuzz.trimf(service.universe, [ 0, 0, 50])
staffing[ 'small' ] = fuzz.trapmf(staffing.universe, [ 0, 0, 30, 60])
staffing[ 'large' ] = fuzz.trapmf(staffing.universe, [ 40, 60, 100, 100])
# Custom membership functions can be built interactively with a familiar,
# Pythonic API
risk[ 'low' ] = fuzz.trapmf(risk.universe, [ 0,0,20, 40])
risk[ 'normal' ] = fuzz.trimf(risk.universe, [ 20, 50, 80])
risk[ 'high' ] = fuzz.trapmf(risk.universe, [ 60, 80, 100,100 ])


# You can see how these look with .view()
funding[ 'inadequate' ].view()
staffing['large'].view()
risk['high'].view()

rule1 = ctrl.Rule(funding[ 'adequate' ] | staffing[ 'small' ], risk[ 'low' ])
rule2 = ctrl.Rule(staffing[ 'small' ] & funding[ 'marginal' ], risk[ 'normal' ])
rule3 = ctrl.Rule(funding[ 'inadequate' ] | staffing[ 'large' ], risk[ 'high' ])


risk_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
final_risk = ctrl.ControlSystemSimulation(risk_ctrl)

final_risk.input[ 'funding' ] = 35
final_risk.input[ 'staffing' ] = 65
# Crunch the numbers
final_risk.compute()
# final_risk.compute_rule(rule1)

print (final_risk.output[ 'risk' ])
risk.view(sim=final_risk)


# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
final_risk.input[ 'funding' ] = 60
final_risk.input[ 'staffing' ] = 35
# Crunch the numbers
final_risk.compute()
print (final_risk.output[ 'risk' ])
risk.view(sim=final_risk)