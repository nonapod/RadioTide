"""
human.py
by lcordell

the basic human archetype
"""
from src.archetype.archetype import Archetype

class SubArchetype(Archetype):
  """
  the classic human archetype with some default values
  """

  def __init__(self):
    Archetype.__init__(self)
    self.archetype = "human"


  def setup(self):
    attributes = {
      "communication" : 40,
      "courage"       : 40,
      "intelligence"  : 45,
      "intimidation"  : 30,
      "intuition"     : 40,
      "manipulation"  : 30,
      "seduction"     : 30,
      "strategy"      : 35,
      "wit"           : 35,
    }

    resistances = {
      "cold"          : 30,
      "thirst"        : 15,
      "heat"          : 30,
      "hunger"        : 40,
      "pain"          : 15,
      "fear"          : 30,
      "seduction"     : 35,
      "manipulation"  : 35,
      "intimidation"  : 30,
      "poison"        : 20,
      "radiation"     : 10,
    }

    knowledge = {
      "bushcraft"     : 10,
      "teaching"      : 10,
      "trading"       : 5,
      "driving"       : 10,
      "riding"        : 5,
      "flying"        : 0,
      "sailing"       : 0,
      "history"       : 15,
      "robotics"      : 5,
      "repair"        : 10,
      "computers"     : 5,
      "herbology"     : 10,
    }

    for key in resistances:
      self.set_resistance(key, resistances[key])

    for key in attributes:
      self.set_attribute(key, attributes[key])

    for key in knowledge:
      self.set_knowledge(key, knowledge[key])
