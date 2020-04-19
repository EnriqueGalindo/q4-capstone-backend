from django.forms import model_to_dict

from encounters.models import Encounters

def hydrateEncounter(encounter):
    encounter_dict = model_to_dict(encounter)
    encounter_dict['creatures'] = [
        model_to_dict(c) for c in encounter_dict['creatures']
    ]
    return encounter_dict