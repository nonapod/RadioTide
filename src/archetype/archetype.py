"""
archetype.py
lcordell
"""

class Archetype:
  """
  the archetype is the base character type, child archetypes
  can be extended from this; i.e. humans, mutants, androids, plans etc
  """
  def __init__(self):
    self.archetype    = None # the name identifier of this archetype; must be overriden in child to work
    self.name         = None # name based on allowed archetype name
    self.age          = None # age based on allowed archetype gender
    self.gender       = None # character gender based on allowed archetype gender
    self.gear         = None # an instance of gear manager
    self.resistances  = None # resistances to various effects
    self.attributes   = None # attributes and modifiers
    self.knowledge    = None # knowledge and modifiers
    self.fame         = {}   # wasteland tile location rating by denizens: +good, -evil
    self.traits       = None # traits acquired
    self.currency     = {}   # currencies and quantities owned; including your own
    self.affiliations = {}   # affiliation/diplomacy to other gang leaders
    self.loyalty      = {}   # loyalties within own gang

    # set base values
    self.set_resistances()
    self.set_attributes()
    self.set_knowledges()

    self.setup()

  def set_resistances(self):
    """
    set the base resistances for this instance
    """
    from cnf.character import resistances as resistances
    self.resistances = resistances


  def set_attributes(self):
    """
    set the base attributes for this instance
    """
    from cnf.character import attributes as attributes
    self.attributes = attributes


  def set_knowledges(self):
    """
    set the base knowledges for this instance
    """
    from cnf.character import knowledge as knowledge
    self.knowledge = knowledge


  def set_resistance(self, resistance, value):
   """
   set a resistance value if the resistance type exists.
   """
   if type(value) == int and type(resistance) == str:
    if resistance in self.resistances:
      self.resistances[resistance] = value


  def set_attribute(self, attribute, value):
   """
   set an attribute value if the attribute type exists.
   """
   if type(value) == int and type(attribute) == str:
    if attribute in self.attributes:
      self.attributes[attribute] = value


  def set_knowledge(self, knowledge, value):
   """
   set a knowledge value if the knowledge type exists.
   """
   if type(value) == int and type(knowledge) == str:
    if knowledge in self.knowledge:
      self.knowledge[knowledge] = value


  def get_ages(self):
    """
    returns a range of possible ages
    """
    return range(16, 60)


  def set_age(self, age):
    """
    set the age of a characher provided it is within the allowed
    date range of the archetype. any character who goes over
    the age range, will race a much greater risk of dying of
    natural causes.
    """
    if type(age) == int and age in self.get_ages():
      self.age = age


  def get_genders(self):
    """
    return a list of possible genders, the
    base archetype has male and female.
    """
    return ["male", "female"]


  def set_gender(self, gender):
    """
    set the gender of the character, if it
    is a string and in the available genders,
    set it.
    """
    if type(gender) == str and gender in self.get_genders():
      self.gender = gender


  def setup(self):
    """
    run this as the last step to set up some better values.
    """
    pass
