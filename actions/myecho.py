import sys

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message, other):
        print(message)
        print(other)

        if message == 'working':
            return (True, message)
        return (False, message, other)
