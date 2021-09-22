"""
mutant.py
by lcordell

the mutant archetype
"""
from src.archetype.archetype import Archetype

class SubArchetype(Archetype):
  """
  the mutant archetype with some default values
  """

  def __init__(self):
    Archetype.__init__(self)
    self.archetype = "mutant"


  def setup(self):
    attributes = {
      "communication" : 30,
      "courage"       : 45,
      "intelligence"  : 30,
      "intimidation"  : 50,
      "intuition"     : 30,
      "manipulation"  : 25,
      "seduction"     : 10,
      "strategy"      : 40,
      "wit"           : 25,
    }

    resistances = {
      "cold"          : 40,
      "thirst"        : 40,
      "heat"          : 40,
      "hunger"        : 25,
      "pain"          : 35,
      "fear"          : 45,
      "seduction"     : 5,
      "manipulation"  : 5,
      "intimidation"  : 40,
      "poison"        : 35,
      "radiation"     : 100,
    }

    knowledge = {
      "bushcraft"     : 15,
      "teaching"      : 5,
      "trading"       : 10,
      "driving"       : 15,
      "riding"        : 0,
      "flying"        : 0,
      "sailing"       : 0,
      "history"       : 30,
      "robotics"      : 15,
      "repair"        : 15,
      "computers"     : 5,
      "herbology"     : 15,
    }

    for key in resistances:
      self.set_resistance(key, resistances[key])

    for key in attributes:
      self.set_attribute(key, attributes[key])

    for key in knowledge:
      self.set_knowledge(key, knowledge[key])
