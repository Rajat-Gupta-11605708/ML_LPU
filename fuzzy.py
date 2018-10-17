from numpy import *
from skfuzzy import *
from skfuzzy import control as ctrl

quality = ctrl.Antecedent(arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(arange(0, 11, 1), 'service')
tip = ctrl.Antecedent(arange(0, 26, 1), 'tip')

quality.automf(3)
service.automf(3)


tip['low'] = trimf(tip.universe, [0, 0, 13])
tip['medium'] = trimf(tip.universe, [0, 13, 25])
tip['high'] = trimf(tip.universe, [13, 25, 25])

quality['average'].view()
service.view()
tip.view()

rule1 = ctrl.rule(quality['poor']|service['poor'], tip['low'])
rule2 = ctrl.rule(quality['average'], tip['medium'])
rule3 = ctrl.rule(quality['good']|service['good'], tip['high'])


rule1.view()

tipping_ctrl = ctrl.ControlSystem(rule1, rule2, rule3)
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

tipping.compute()
print(tipping.output['tip'])
tip.view(sim=tipping)
