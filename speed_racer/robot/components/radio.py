import atexit
import traitlets 
from traitlets.config.configurable import Configurable

class Radio(Configurable):

    # Value that will be watched
    value = traitlets.Integer()

    def __init__(self, *args, **kwargs) :
        #initialize the traitlet
        super(Radio, self).__init__(*args, **kwargs)

        atexit.register(self._release)

    @traitlets.observe('value')
    def _observe_value(self, change):
        self._take_action(change)

    def _take_action(self, new_radio_value):
        print("Taking action on new motor value")

    def _release(self) :
        # Release and reset motor resources
        print("Releasing radio resources")