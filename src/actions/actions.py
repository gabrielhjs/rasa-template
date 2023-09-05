import re
import logging
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from .utils import SlotName, EntityName


class AbstractExtractFloatSlot(Action):
    entity_name: EntityName
    slot_name: SlotName = SlotName.DEFAULT

    def name(self) -> Text:
        return f"action_extract_{self.slot_name.value}"

    def run(
        self,
        _dispatcher: CollectingDispatcher,
        tracker: Tracker,
        _domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entity_values = tracker.get_latest_entity_values(self.entity_name.value)

        value = next(entity_values, None)

        if value is not None:
            numbers = re.findall(r"\d+", value)

            if len(numbers):
                return [SlotSet(self.slot_name.value, float(numbers[0]))]

        return []


class ActionExtractSlotFrequenciaRespiratoria(AbstractExtractFloatSlot):
    entity_name = EntityName.FREQUENCIA_RESPIRATORIA
    slot_name = SlotName.FREQUENCIA_RESPIRATORIA


class ActionExtractSlotPressaoArterialSistolica(AbstractExtractFloatSlot):
    entity_name = EntityName.PRESSAO_ARTERIAL_SISTOLICA
    slot_name = SlotName.PRESSAO_ARTERIAL_SISTOLICA


class ActionExtractSlotPressaoArterialDiastolica(AbstractExtractFloatSlot):
    entity_name = EntityName.PRESSAO_ARTERIAL_DIASTOLICA
    slot_name = SlotName.PRESSAO_ARTERIAL_DIASTOLICA


class ActionExtractSlotIdade(AbstractExtractFloatSlot):
    entity_name = EntityName.IDADE
    slot_name = SlotName.IDADE


class ActionExtractSlotUreia(AbstractExtractFloatSlot):
    entity_name = EntityName.UREIA
    slot_name = SlotName.UREIA


class ActionExtractSlotSaturacaoDeOxigenio(AbstractExtractFloatSlot):
    entity_name = EntityName.SATURACAO_DE_OXIGENIO
    slot_name = SlotName.SATURACAO_DE_OXIGENIO


class ActionCalculateCurb65(Action):
    def name(self) -> Text:
        return "action_calculate_curb65"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        _domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        nivel_de_consciencia = tracker.get_slot(SlotName.NIVEL_DE_CONSCIENCIA.value)
        ureia = tracker.get_slot(SlotName.UREIA.value)
        frequencia_respiratoria = tracker.get_slot(
            SlotName.FREQUENCIA_RESPIRATORIA.value
        )
        pressao_arterial_diastolica = tracker.get_slot(
            SlotName.PRESSAO_ARTERIAL_DIASTOLICA.value
        )
        pressao_arterial_sistolica = tracker.get_slot(
            SlotName.PRESSAO_ARTERIAL_SISTOLICA.value
        )
        idade = tracker.get_slot(SlotName.IDADE.value)

        score = 0.0

        try:
            if nivel_de_consciencia == "Confusão mental":
                score += 1

            if ureia is not None and int(ureia) > 43:
                score += 1

            if (
                frequencia_respiratoria is not None
                and int(frequencia_respiratoria) > 30
            ):
                score += 1

            if (
                pressao_arterial_diastolica is not None
                and int(pressao_arterial_diastolica) < 60
            ) or (
                pressao_arterial_sistolica is not None
                and int(pressao_arterial_sistolica) < 90
            ):
                score += 1

            if idade is not None and int(idade) > 65:
                score += 1

            dispatcher.utter_message(f"O score de CURB65 é ({score})")

            return [SlotSet(SlotName.CURB65.value, score)]

        except ValueError as error:
            logging.error(error)

            dispatcher.utter_message("Desculpe, ocorreu um erro durante o cálculo")

            return []


class ActionCalculateSepse(Action):
    def name(self) -> Text:
        return "action_calculate_sepse"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        _domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        nivel_de_consciencia = tracker.get_slot(SlotName.NIVEL_DE_CONSCIENCIA.value)
        frequencia_respiratoria = tracker.get_slot(
            SlotName.FREQUENCIA_RESPIRATORIA.value
        )
        pressao_arterial_sistolica = tracker.get_slot(
            SlotName.PRESSAO_ARTERIAL_SISTOLICA.value
        )

        score = 0.0

        try:
            if nivel_de_consciencia == "Confusão mental":
                score += 1

            if (
                frequencia_respiratoria is not None
                and int(frequencia_respiratoria) > 30
            ):
                score += 1

            if (
                pressao_arterial_sistolica is not None
                and int(pressao_arterial_sistolica) < 90
            ):
                score += 1

            if score >= 2:
                dispatcher.utter_message(f"Deve considerar coletar sepse")

            else:
                dispatcher.utter_message(f"Não há indicativos de sepse")

        except ValueError as error:
            logging.error(error)

            dispatcher.utter_message("Desculpe, ocorreu um erro durante o cálculo")

        return []
