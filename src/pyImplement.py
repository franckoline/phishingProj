from transitions import Machine

import random
###===========================================================
class fsm(object):
    # Define some states.
    states = ['Starting_Point',
              'Counter_Checker',
              'Security_Level',
              'User_Caution',
              'Two_Ways_Authentication',
              'Assumption_About_Connection',
              'Doubt_Error_Message',
              'Password_Error',
              'Problem_Recovery',
              'Permission_Check',
              'Genuine_Information',
              'Phishing_Attack',
              'Unsafe_Final',
              'Safe_Final']

    transitions = [
        {'trigger': '1', 'source': 'Starting_Point', 'dest': 'Counter_Checker'},
        {'trigger': '14', 'Counter_Checker': 'liquid', 'dest': 'Unsafe_Final'},
        {'trigger': '2', 'source': 'Starting_Point', 'dest': 'Security_Level'},
        {'trigger': '3', 'source': 'Security_Level', 'dest': 'Final_Safe'}
    ]


###===========================================================

    def __init__(self, name):

        self.name = name

        # What have we accomplished today?
        self.iteration_time = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=fsm.states, initial='Starting_Point')

        # At some point, every superhero must rise and shine.
        self.machine.add_transition(trigger=1, source='Starting_Point', dest='Counter_Checker')

###===========================================================