"""
robot.py
by lcordell

the robot archetype
"""
from src.archetype.archetype import Archetype

class SubArchetype(Archetype):
  """
  the robot archetype with some default values
  """

  def __init__(self):
    Archetype.__init__(self)
    self.archetype = "robot"


  def setup(self):
    attributes = {
      "communication" : 20,
      "courage"       : 50,
      "intelligence"  : 50,
      "intimidation"  : 40,
      "intuition"     : 20,
      "manipulation"  : 20,
      "seduction"     : 10,
      "strategy"      : 50,
      "wit"           : 30,
    }

    resistances = {
      "cold"          : 50,
      "thirst"        : 50,
      "heat"          : 50,
      "hunger"        : 100,
      "pain"          : 45,
      "fear"          : 45,
      "seduction"     : 10,
      "manipulation"  : 10,
      "intimidation"  : 40,
      "poison"        : 100,
      "radiation"     : 50,
    }

    knowledge = {
      "bushcraft"     : 5,
      "teaching"      : 0,
      "trading"       : 0,
      "driving"       : 5,
      "riding"        : 0,
      "flying"        : 0,
      "sailing"       : 0,
      "history"       : 25,
      "robotics"      : 25,
      "repair"        : 25,
      "computers"     : 25,
      "herbology"     : 0,
    }

    for key in resistances:
      self.set_resistance(key, resistances[key])

    for key in attributes:
      self.set_attribute(key, attributes[key])

    for key in knowledge:
      self.set_knowledge(key, knowledge[key])
