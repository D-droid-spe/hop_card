from django.apps import AppConfig
from suit.apps import DjangoSuitConfig



class HospitalConfig(AppConfig):
    name = 'hospital'
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'