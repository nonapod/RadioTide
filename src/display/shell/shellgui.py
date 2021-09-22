from src.mapgen.mapgen import Map

class ShellGui():
  """
  the shell interface to radtide
  """ 
  def __init__(self):
    self.game_map = Map(height=25, width=60, colours=True, shell="zsh")  
    self.startgame()


  def startgame(self):
    """
    start the game
    @TODO this is just testing filler, completely not
          how this should be or will be.
    """
    exit_vars = ['yes', 'YES', 'y', 'Y']
    quit_game = False
    while quit_game == False:
      print "RadTide"
      print "======"
      self.game_map.build_map()
      print self.game_map.printmap()

      print "Dimensions"
      print "height: %s tiles" % self.game_map.height
      print "width: %s tiles" % self.game_map.width
      
      print "Density"
      print "======="
      density = self.game_map.get_density()
      for name in density:
        print "density of %s: %s%%" % (name, density[name]) 


      print ""
      print "Accept this map? (y)" 
      print "or change density percentage? (enter density name)" 
      print "or press any key to regenerate using the same values"
      print "or change dimension? (enter dimension name)"
      selection = raw_input()
      quit_game = True if selection in exit_vars else False
      if selection in density:
        print "Enter a new value for this density (1-99)\n"
        new_density = raw_input()
        self.game_map.change_density(selection, new_density)
      if selection == "height" or selection == "width":
        print "Enter value for this dimension"
        dimension = raw_input()
        try: 
          dimension = int(dimension)
          setattr(self.game_map, selection, dimension)
        except:
          pass
