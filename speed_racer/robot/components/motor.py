import atexit
import traitlets
import RPi.GPIO as GPIO
from traitlets.config.configurable import Configurable
class Motor(Configurable):

    # Value that will be watched
    speed = traitlets.Integer()
    
    _gpio_pin = 3

    def __init__(self, *args, **kwargs) :
        #initialize the traitlet
        super(Motor, self).__init__(*args, **kwargs)

        GPIO.setmode(GPIO.BOARD)

        self._arm_esc()
        atexit.register(self._release)

    @traitlets.observe('value')
    def _observe_value(self, change):
        self._take_action(change)

    def _take_action(self, new_motor_value):
        print("Taking action on new motor value")

    def _arm_esc(self):
        print("Arming ESC")
        
    def _release(self) :
        # Release and reset motor resources
        print("Releasing motor resources")