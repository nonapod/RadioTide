"""
herbinoid.py
by lcordell

the herbinoid archetype; this is a plant "person",
or entity.
"""
from src.archetype.archetype import Archetype

class SubArchetype(Archetype):
  """
  the herbinoid archetype with some default values
  """

  def __init__(self):
    Archetype.__init__(self)
    self.archetype = "herbinoid"


  def setup(self):
    attributes = {
      "communication" : 10,
      "courage"       : 50,
      "intelligence"  : 35,
      "intimidation"  : 40,
      "intuition"     : 20,
      "manipulation"  : 20,
      "seduction"     : 0,
      "strategy"      : 20,
      "wit"           : 20,
    }

    resistances = {
      "cold"          : 20,
      "thirst"        : 35,
      "heat"          : 60,
      "hunger"        : 60,
      "pain"          : 45,
      "fear"          : 80,
      "seduction"     : 100,
      "manipulation"  : 40,
      "intimidation"  : 50,
      "poison"        : 100,
      "radiation"     : 100,
    }

    knowledge = {
      "bushcraft"     : 20,
      "teaching"      : 20,
      "trading"       : 0,
      "driving"       : 0,
      "riding"        : 0,
      "flying"        : 0,
      "sailing"       : 0,
      "history"       : 5,
      "robotics"      : 0,
      "repair"        : 0,
      "computers"     : 0,
      "herbology"     : 30,
    }

    for key in resistances:
      self.set_resistance(key, resistances[key])

    for key in attributes:
      self.set_attribute(key, attributes[key])

    for key in knowledge:
      self.set_knowledge(key, knowledge[key])
