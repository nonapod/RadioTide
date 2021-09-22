#
# RadTide
# 
# A little post apocalyptic 4x strategy concept
#
import os
from src.mapgen.mapgen import Map
from src.display.curses.cursesgui import CursesGui
from src.display.shell.shellgui import ShellGui
from curses import wrapper
from cnf.tiles import tiles

def shellmode():
  """
  run game in the shell
  """
  radtime = ShellGui()

def cursesmode(SCREEN):
  """
  curses mode is called from the curses
  wrapper function for nice exit.
  """
  radtide = CursesGui()

if __name__ == "__main__":
  gamemode = raw_input("Which version do you want? (s)hell version or (c)urses version? (c/s) ")
  if gamemode == "c":
    wrapper(cursesmode)
  elif gamemode == "s":
    shellmode()
  else:
    print "not a valid gamemode, try running again"
