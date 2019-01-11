from __future__ import absolute_import, division, unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionName(Action):
    def name(self):
        return 'action_name'

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name')
        print('TRACKER SLOTS:')
        print(tracker.slots)

        response = """Olá {}, como posso lhe ajudar?""".format(name)
        dispatcher.utter_message(response)
        return [SlotSet('name',name)]