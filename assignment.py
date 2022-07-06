

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

funding = ctrl.Antecedent(np.arange(0, 101, 1), 'funding' )
staffing = ctrl.Antecedent(np.arange(0, 101, 1), 'staffing' )
risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk' )

funding[ 'inadequate' ] = fuzz.trapmf(funding.universe, [ 0,0, 20, 30])
funding[ 'marginal' ] = fuzz.trimf(funding.universe, [ 20, 50, 80])
funding[ 'adequate' ] = fuzz.trapmf(funding.universe, [ 60, 80, 100,100])

staffing[ 'small' ] = fuzz.trapmf(staffing.universe, [ 0, 0, 30, 60])
staffing[ 'large' ] = fuzz.trapmf(staffing.universe, [ 40, 60, 100, 100])


risk[ 'low' ] = fuzz.trapmf(risk.universe, [ 0,0,20, 40])
risk[ 'normal' ] = fuzz.trimf(risk.universe, [ 20, 50, 80])
risk[ 'high' ] = fuzz.trapmf(risk.universe, [ 60, 80, 100,100 ])


funding[ 'inadequate' ].view()
staffing['large'].view()
risk['high'].view()

rule1 = ctrl.Rule(funding[ 'adequate' ] | staffing[ 'small' ], risk[ 'low' ])
rule2 = ctrl.Rule(funding[ 'marginal' ] & staffing[ 'large' ], risk[ 'normal' ])
rule3 = ctrl.Rule(funding[ 'inadequate' ], risk[ 'high' ])

rule1.view()
rule2.view()
rule3.view()

output_risk_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
output_risk_ctrl.view()
final_risk = ctrl.ControlSystemSimulation(output_risk_ctrl)


final_risk.input[ 'funding' ] = 35
final_risk.input[ 'staffing' ] = 60

final_risk.compute()

print (final_risk.output[ 'risk' ])
risk.view(sim=final_risk)
