#!/usr/local/bin/python
"""
chargen_test.py
by lcordell

a character generator test, using
all the classes.
"""
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.archetype.loader import load_archetypes

def archetypes():
  return load_archetypes()


if __name__ == "__main__":
  for archetype in archetypes():
    a = archetype()
    raw_input("Viewing archetype: %s" % a.archetype)
    print "Base Attributes -> "
    print a.attributes
    raw_input("press any key... ")
    print "Base Knowledge -> "
    print a.knowledge
    raw_input("press any key... ")
    print "Base Resistances -> "
    print a.resistances
    raw_input("press any key... ")
