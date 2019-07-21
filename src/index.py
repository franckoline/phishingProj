# from random import randint
# from time import clock
#
#
# ##===================================================
# State = type("State", (object,),{})
#
# class LightOn(State):
#     def Execute(self):
#         print("Light is On!")
#
# class LightOff(State):
#     def Execute(self):
#         print("Light is Off!")
# ##===================================================
#
# class Transition(object):
#     def __init__(self, toState):
#         self.toState = toState
#
#     def Execute(self):
#         print("Transitioning")
#
#
# ##===================================================
# class SimpleFSM(object):
#     def __init__(self, char):
#         self.char = char
#         self.states = {}
#         self.transitions = {}
#         self.curState = None
#         self.trans = None
#
#     def SetState(self, stateName):
#         self.curState = self.states[stateName]
#
#     def Transition(self, transName):
#         self.trans = self.transitions[transName]
#
#     def Execute(self):
#         if(self.trans):
#             self.trans.Execute()
#             self.SetState(self.trans.toState)
#             self.trans = None
#         self.curState.Execute()
#
#
# ##===================================================
# class Char(object):
#     def __init__(self):
#         self.FSM = SimpleFSM(self)
#         self.LightOn = True
#
#
# ##===================================================
# if __name__ =="__main__":
#     light = Char()
#     light.FSM.states["On"] = LightOn()
#     light.FSM.states["Off"] = LightOff()
#     light.FSM.transitions["toOn"] = Transition("On")
#     light.FSM.transitions["toOff"] = Transition("Off")
#
#     light.FSM.SetState("On")
#     for i in range(20):
#         startTime = clock()
#         timeInterval = 1
#         while(startTime+timeInterval>clock()):
#             pass
#         if(randint(0,2)):
#             if(light.LightOn):
#                 light.FSM.Transition("toOff")
#                 light.LightOn = False
#             else:
#                 light.FSM.Transition("toOn")
#                 light.LightOn = True
#         light.FSM.Execute()
##===================================================

# from transitions import Machine
#
# class Matter(object):
#     pass
#
# lump = Matter()
#
# machine = Machine(model=lump, states=['solid', 'liquid', 'gas', 'plasma'], initial='solid')

from transitions import Machine
import random

class NarcolepticSuperhero(object):

    # Define some states...
    states = ['Ta', 'Tb', 'Tc', 'Td', 'Te', 'Tf', 'Tg', 'Th', 'Ti', 'Tj','Tk', 'Tl', 'SafeFinal', 'UnsafeFinal']

    def __init__(self, name):

        ###
        self.name = name

        ### What have we accomplished today?
        self.kittens_rescued = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=NarcolepticSuperhero.states, initial='asleep')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        # At some point, every superhero must rise and shine.
        self.machine.add_transition(trigger='wake_up', source='asleep', dest='hanging out')

        # Superheroes need to keep in shape.
        self.machine.add_transition('work_out', 'hanging out', 'hungry')

        # Those calories won't replenish themselves!
        self.machine.add_transition('eat', 'hungry', 'hanging out')

        # Superheroes are always on call. ALWAYS. But they're not always
        # dressed in work-appropriate clothing.
        self.machine.add_transition('distress_call', '*', 'saving the world',
                         before='change_into_super_secret_costume')

        # When they get off work, they're all sweaty and disgusting. But before
        # they do anything else, they have to meticulously log their latest
        # escapades. Because the legal department says so.
        self.machine.add_transition('complete_mission', 'saving the world', 'sweaty',
                         after='update_journal')

        # Sweat is a disorder that can be remedied with water.
        # Unless you've had a particularly long day, in which case... bed time!
        self.machine.add_transition('clean_up', 'sweaty', 'asleep', conditions=['is_exhausted'])
        self.machine.add_transition('clean_up', 'sweaty', 'hanging out')

        # Our NarcolepticSuperhero can fall asleep at pretty much any time.
        self.machine.add_transition('nap', '*', 'asleep')

    def update_journal(self):
        """ Dear Diary, today I saved Mr. Whiskers. Again. """
        self.kittens_rescued += 1

    def is_exhausted(self):
        """ Basically a coin toss. """
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        print("Beauty, eh?")

##===================================================
