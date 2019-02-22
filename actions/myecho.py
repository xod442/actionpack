import sys

from st2common.runners.base_action import Action

# class takes two variables, message (position 1) and other (position 2)

# st2 run rick.echo_action message="message" other="other"

class MyEchoAction(Action):
    def run(self, message, other):
        print(message)
        print(other)

        if message == 'working':
            return (True, message)
        return (False, message, other)
