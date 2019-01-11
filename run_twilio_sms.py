from rasa_core.channels.twilio import TwilioInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weather_nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = TwilioInput(
    # you get this from your twilio account
    account_sid="AC5bb1242b97d3880aadf4b407730cf3eb",
    # also from your twilio account
    auth_token="57278821b1d2e8861a6a9a9c5a3b1d84",
    # a number associated with your twilio account
    twilio_number="+18329090952"
)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=True)