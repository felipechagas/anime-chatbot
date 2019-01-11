from __future__ import absolute_import, division, unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests

class ActionAnime(Action):
    def name(self):
        return 'action_anime'

    def run(self, dispatcher, tracker, domain):
        print("TRACKER SLOTS:")
        print(tracker.slots)
        #https://advisor.climatempo.com.br
        api_key = 'dc68ddc0d1818cc98707d01fc85d3ddf'
        loc = tracker.get_slot('location')
        r = requests.get("http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+loc+"&token="+api_key)
        print(r.json()[0]['id'])
        city_id = r.json()[0]['id']

        r2 = requests.get("http://apiadvisor.climatempo.com.br/api/v1/weather/locale/"+str(city_id)+"/current?token="+api_key)
        print(r2.json()['data'])

        city = r2.json()['name']
        condition = r2.json()['data']['condition']
        temperature_c = r2.json()['data']['temperature']
        humidity = r2.json()['data']['humidity']
        windspeed = r2.json()['data']['wind_velocity']

        response = """Atualmente está {} em {}. A temperatura é de {} graus, a humidade é de {} e a velocidade do vento é de {} mph""".format(condition, city, temperature_c, humidity, windspeed)
        #response = r
        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]
