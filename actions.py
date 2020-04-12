from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "job",
            "use_case",
            "budget",
            "name",
            "company",
            "email",
        ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("感谢您的联系，我们会尽快与您联系")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "job": [
                self.from_text(intent="inform"),
            ],
            "use_case": [
                self.from_text(intent="inform"),
            ],
            "budget": [
                self.from_text(intent="inform"),
            ],
            "name": [
                self.from_text(intent="inform"),
            ],
            "company": [
                self.from_text(intent="inform"),
            ],
            "business_email": [
                self.from_text(intent="inform"),
            ],
        }
