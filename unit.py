class Unit:
    def __init__(self):
        self.state = False

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def alive(self):
        self.state(True)

    def die(self):
        self.state(False)

