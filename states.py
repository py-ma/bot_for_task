from transitions import Machine, State
from main import *


class Model(object):
    states = ['START',
              'CHOOSE SIZE',
              'GO PAY',
              'CHOOSE PAY METHOD',
              'REPEATING ORDER',
              'FINISH']


s = Model()
transitions = [
    ['t1', 'START', 'CHOOSE SIZE'],
    ['t2', 'CHOOSE SIZE', 'GO PAY' or 'START'],
    ['t3', 'GO PAY', 'CHOOSE PAY METHOD' or 'START'],
    ['t4', 'CHOOSE PAY METHOD', 'REPEATING ORDER' or 'START'],
    ['t5', 'REPEATING ORDER', 'FINISH' or 'START'],
    ['tn', 'REPEATING ORDER', 'START'],
    ['t6', 'FINISH', 'START']
]

machine = Machine(model=s, states=Model.states, initial='START')
machine.add_transition('t1', source='START', dest='CHOOSE SIZE' or 'START')
machine.add_transition('t2', source='CHOOSE SIZE', dest='GO PAY' or 'START')
machine.add_transition('t3', source='GO PAY', dest='CHOOSE PAY METHOD' or 'START')
machine.add_transition('t4', source='CHOOSE PAY METHOD', dest='REPEATING ORDER' or 'START')
machine.add_transition('t5', source='REPEATING ORDER', dest='FINISH')
machine.add_transition('tn', source='REPEATING ORDER', dest='CHOOSE SIZE')
machine.add_transition('t6', source='FINISH', dest='START')
