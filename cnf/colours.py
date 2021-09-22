"""
  Colours
  description: allows the painting of strings to be various colours
               depending on shell and colour avilability
  @TODO a little rudimentary at the moment, detect shell, colours etc
        may need to remove this altogether as NCURSES should be handling
        all of the colours.
"""
class Colours():

  def __init__(self, shell="zsh"):
    self.shell = shell 
    self.colours = {
      "sh" : {
        "none"        : "\e[0m",
        "white"       : "\e[1;37m",
        "black"       : "\e[0;30m",
        "blue"        : "\e[0;34m",
        "lightblue"   : "\e[1;34m",
        "green"       : "\e[0;32m",
        "lightgreen"  : "\e[1;32m",
        "cyan"        : "\e[0;36m",
        "lightcyan"   : "\e[1;36m",
        "red"         : "\e[0;31m",
        "lightred"    : "\e[1;31m",
        "purple"      : "\e[0;35m",
        "lightpurple" : "\e[1;35m",
        "brown"       : "\e[0;33m",
        "yellow"      : "\e[1;33m",
        "gray"        : "\e[0;30m",
        "lightgray"   : "\e[0;37m",
        "termchar"    : "\]",
      },
      "zsh" : {
        "none"        : "\033[0m",
        "white"       : "\033[1;37m",
        "black"       : "\033[0;30m",
        "blue"        : "\033[0;34m",
        "lightblue"   : "\033[1;34m",
        "green"       : "\033[0;32m",
        "lightgreen"  : "\033[1;32m",
        "cyan"        : "\033[0;36m",
        "lightcyan"   : "\033[1;36m",
        "red"         : "\033[0;31m",
        "lightred"    : "\033[1;31m",
        "purple"      : "\033[0;35m",
        "lightpurple" : "\033[1;35m",
        "brown"       : "\033[0;33m",
        "yellow"      : "\033[1;33m",
        "gray"        : "\033[0;30m",
        "lightgray"   : "\033[0;37m",
      }
    }


  """
    paint
    description: paint a tile or string a certain colour
  """
  def paint(self, colour="white", string=""):
    if self.shell:
      if colour in self.colours[self.shell]:
        return "%s%s%s" % (self.colours[self.shell][colour], string, self.colours[self.shell]['none'])
      return "%s %s" % (self.colours[self.shell]["none"], string)
    return string
