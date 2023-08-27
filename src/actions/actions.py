import re
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionExtractSlotFrequenciaRespiratoria(Action):
    def name(self) -> Text:
        return "action_extract_slot_frequencia_respiratoria"

    def run(
        self,
        _dispatcher: CollectingDispatcher,
        tracker: Tracker,
        _domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entity_values = tracker.get_latest_entity_values(
            "entity_frequencia_respiratoria"
        )

        try:
            value = next(entity_values)
            numbers = re.findall(r"\d+", value)

            if len(numbers):
                return [SlotSet("slot_frequencia_respiratoria", float(numbers[0]))]

        except:
            pass

        return []


class ActionExtractSlotPressaoArterial(Action):
    def name(self) -> Text:
        return "action_extract_slot_pressao_arterial"

    def run(
        self,
        _dispatcher: CollectingDispatcher,
        tracker: Tracker,
        _domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entity_values = tracker.get_latest_entity_values("entity_pressao_arterial")

        try:
            value = next(entity_values)
            numbers = re.findall(r"\d+", value)

            if len(numbers):
                return [SlotSet("slot_pressao_arterial", float(numbers[0]))]

        except:
            pass

        return []
