from .Speech import Speech
from .Lighting import Lighting
from .Head import Head
from .Lift import Lift


class Actions(Speech, Head, Lift, Lighting):
    def __init__(self):
        #NO OP
        x = x

    '''
    Predefine a set of actions in this class
    '''
