def __init__(self):
    self.state = False

@property
def state(self):
    return self._state

@state.setter
def set_state(self, bool):
    self._state = bool

def alive(self):
    self.set_state(True)

def die(self):
    self.set_state(False)