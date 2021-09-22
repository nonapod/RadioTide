from cnf.tiles import tiles
from src.mapgen.mapgen import Map
from curses import wrapper
import curses 

class CursesGui():
  """
  returns a fully playable version of the game
  using the curses library
  """  

  def __init__(self):
    self._shell = "zsh"
    self.game_map = Map(height=25, width=60, colours=True, shell=self._shell)  
    self.game_map.build_map()
    self._STATE = "mainmenu"

    # setup curses
    self.stdscr = curses.initscr()
    self.stdscr.keypad(1) 
    curses.noecho()
    curses.cbreak()
    self.init_colors()  

    #self.init_main_toolbar()
    #self.init_map_gen()
    self.mainloop()
      

  def init_main_toolbar(self):
    """
    initialise the main toolbar
    """
    #init tool bar window
    begin_x = 1
    begin_y = 1
    height = 4
    width = 50
    self.tool_bar_win = curses.newwin(height, width, begin_y, begin_x)
    self.tool_bar_win.addstr(1, 2, "RadTide v0.1", curses.color_pair(self.RED))
    self.tool_bar_win.addstr(2, 2, "Main Menu", curses.color_pair(self.MAGENTA))
    self.tool_bar_win.border()
    self.tool_bar_win.refresh()
  
  def main_toolbar_options_set(self, string, y, color_pair_id):
    """
    add a string to a line of the main toolbar
    """
    self.tool_bar_win.move(y, 1)
    self.tool_bar_win.clrtoeol()
    self.tool_bar_win.addstr(y, 2, string, curses.color_pair(color_pair_id))
    self.tool_bar_win.border()
    self.tool_bar_win.refresh()
    

  def new_selection_window(self, options):
    """
    add a new selection window, pass in a 
    dict of options to display.
    param dict options: a dict of options
    """
    pass

  def init_main_menu(self):
    """
    initialise the main game menu
    """
    begin_x = 1
    begin_y = 5
    height = 6 
    width = 50 

    self.main_menu_window = curses.newwin(height, width, begin_y, begin_x)
    self.main_menu_window.addstr(1, 2, "(S)tart a new game", curses.color_pair(self.GREEN))
    self.main_menu_window.addstr(2, 2, "(L)oad an existing game", curses.color_pair(self.MAGENTA))
    self.main_menu_window.addstr(3, 2, "(O)ptions", curses.color_pair(self.MAGENTA))
    self.main_menu_window.addstr(4, 2, "(Q)uit game", curses.color_pair(self.RED))
    self.main_menu_window.border()
    self.main_menu_window.refresh()

  def init_map_gen(self):
    """
    initialise the map gen windows
    """

    #init map window
    begin_x = 1
    begin_y = 5
    height = self.game_map.height
    width = self.game_map.width
    self.map_win = curses.newwin(height+2, width+4, begin_y, begin_x)
    self.tool_bar_win.addstr(2, 2, "Change the following? (S)ize (D)ensity", curses.color_pair(self.MAGENTA))

    self.displaymap()
    self.map_win.border()
    self.map_win.refresh()

  def main_menu_state(self):
    """
    this is called when the game state is 'mainmenu'
    """
    self.init_main_toolbar()
    self.init_main_menu()
    while self._STATE == "mainmenu":
      # handle keys
      key = self.stdscr.getch()
      if key == ord('q'):
        self._STATE = "done"
      if key == ord('s'):
        self._STATE = "newgame"
        del self.main_menu_window
    
  def new_game_state(self):
    """
    this is called when the game state is 'newgame'
    """
    self.init_map_gen()
    self.main_toolbar_options_set("(N)ew Map | (M)ap Settings | (Q)uit",2, self.MAGENTA)
    while self._STATE == "newgame":
      key = self.stdscr.getch()
      if key == ord('q'):
        self._STATE = "done"
      elif key == ord('n'):
        self.game_map.build_map()
        self.displaymap()
    

  def mainloop(self):
    """
    The main loop
    """
    self.stdscr.refresh()
    while not self._STATE == "done":
      # main game menu
      if self._STATE == "mainmenu":
        self.main_menu_state()
      elif self._STATE == "newgame":
        self.new_game_state()

  def quitgame(self):
    """
    close the game nicely
    """
    curses.nocbreak();
    self.stdscr.keypad(0)
    curses.echo()
    curses.endwin()

  def displaymap(self): 
    """
    display the map in the ncurses gamemap window
    """
    map_str = ""
    for ypos, y in enumerate(self.game_map._map):
      row = ""
      for xpos, x in enumerate(y):
        # use the ncurses color
        color = self.color_map[x.colour]
        self.map_win.addstr(ypos+1, xpos+2, x.term_display, curses.color_pair(color))

    self.map_win.refresh()
    self.stdscr.refresh()



  def init_colors(self):
    """
    set up curses color pairs
    """
    curses.start_color()
    self.RED = 1
    self.GREEN = 2
    self.YELLOW = 3
    self.BLUE = 4
    self.MAGENTA = 5
    self.CYAN = 6
    self.WHITE = 7
    # map the colors set in the colours config to
    # reflect available curses colours
    self.color_map = {
        "none"        : self.GREEN,
        "white"       : self.WHITE,
        "black"       : self.GREEN,
        "blue"        : self.BLUE,
        "lightblue"   : self.CYAN,
        "green"       : self.GREEN,
        "lightgreen"  : self.GREEN,
        "cyan"        : self.CYAN,
        "lightcyan"   : self.CYAN,
        "red"         : self.RED,
        "lightred"    : self.RED,
        "purple"      : self.MAGENTA,
        "lightpurple" : self.MAGENTA,
        "brown"       : self.YELLOW,
        "yellow"      : self.YELLOW,
        "gray"        : self.WHITE,
        "lightgray"   : self.WHITE,
    }
    
    curses.init_pair(self.RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(self.GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(self.YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(self.BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(self.MAGENTA, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(self.CYAN, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(self.WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
