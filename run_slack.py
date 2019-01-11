from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.tracker_store import MongoTrackerStore
from rasa_core.domain import Domain


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weather_nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
mongo_tracker_store = MongoTrackerStore(domain=Domain, host="mongodb://localhost:27017", db="rasa", collection="conversations")

agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint, tracker_store=mongo_tracker_store)

input_channel = SlackInput('xoxb-499929904805-511978697586-oBurYOvD5NgBASQhMpXXqr7w' #your bot user authentication token
                           )

agent.handle_channels([input_channel], 5004, serve_forever=True)