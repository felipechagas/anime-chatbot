from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig

# load your trained agent
nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weather_nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)


input_channel = FacebookInput(
    fb_verify="YOUR_FB_VERIFY",
    # you need tell facebook this token, to confirm your URL
    fb_secret="c0a30a5fca7df12a0111d6db5f683c79",  # your app secret
    fb_access_token="EAAEvGaFSU1kBAGokBRg30vqZA7wRihjVjv5SeuTZBLbnwXRG8R0r33AZBUT0eCxPtvohLuSqGEaor8b5Eccq5LzzLF071lJjZBf3flZBZAZBH9XOmCiiUpXneTz3FiiTZA1B3dePRxzZBZCtSb7MwbO2lEco5RATZC8psnmZBuK1rbCBsAZDZD"
    # token for the page you subscribed to
)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=False)