import traitlets
from traitlets.config.configurable import SingletonConfigurable
from robot.components.motor import Motor

class app(SingletonConfigurable):
    motor = traitlets.Instance(Motor)

    def __init__(self, *args, **kwargs):
        #Initialize traitlet
        super(app, self).__init__(*args, **kwargs)
        print("__init__ app")
        self.motor = Motor()

