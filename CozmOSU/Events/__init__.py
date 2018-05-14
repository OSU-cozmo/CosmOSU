from ..Robot import Robot
import cozmo
import asyncio



def bindEvent(self, event, func):

    ev = evt(func, event)
    dispatcher.add_event_handler(event, ev.boundHandler)

Robot.bindEvent = bindEvent


class evt:

    def __init__(self, event, callback):
        self.callback = callback
        self.event = event

    def run(self, evt, state):
        if self.callback != -1:
            self.callback(evt, state)

    async def boundHandler(self, evt, **kwargs):
        #build state here 
        state = {}
        
        self.run(evt, state)
        