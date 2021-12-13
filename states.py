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
    ['t2', 'CHOOSE SIZE', 'GO PAY'],
    ['t3', 'GO PAY', 'CHOOSE PAY METHOD'],
    ['t4', 'CHOOSE PAY METHOD', 'REPEATING ORDER'],
    ['t5', 'REPEATING ORDER', 'FINISH'],
    ['tn', 'REPEATING ORDER', 'CHOOSE SIZE'],
    ['t6', 'FINISH', 'START']]

machine = Machine(model = s,states=Model.states, initial='START')
machine.add_transition('t1', source='START', dest='CHOOSE SIZE')
machine.add_transition('t2', source='CHOOSE SIZE', dest='GO PAY')
machine.add_transition('t3', source='GO PAY', dest='CHOOSE PAY METHOD')
machine.add_transition('t4', source='CHOOSE PAY METHOD', dest='REPEATING ORDER')
machine.add_transition('t5', source='REPEATING ORDER', dest='FINISH')
machine.add_transition('tn', source='REPEATING ORDER', dest='CHOOSE SIZE')
machine.add_transition('t6', source='FINISH', dest='START')