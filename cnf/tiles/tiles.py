# tiles.py
# 
#
# define some tiles to display; needs to be an array
# of objects
#
# name - tile display name, should be unique
# term_display - character to display in terminal
# movement - movement bonus
# cover - cover bonus
# loot_chance - chance to find loot
# view_bonus - view distance visibility bonus
# blocked - tile is not passable (always defaults to False)
# colour  - tile colour if printing colours
# characteristic - (these are defined in tile_characteristics.py)
#   o urban - this is used to bunch city tiles together
#   o water - this is used to bunch lake and stream tiles together
#   o path  - this is used to form an orderly line of rivers, roads, tracks etc
#


tiles = [
  { 
    "name" : "mountains",
    "term_display" : '^',
    "movement" : 4, 
    "cover" : -2,
    "loot_chance" : 10,
    "view_bonus" : 2,
    "blocked" : False,
    "colour" : "lightgray",
    "characteristic" : "elevation",
  },
  { 
    "name" : "hills",
    "term_display" : '^',
    "movement" : 4, 
    "cover" : -2,
    "loot_chance" : 10,
    "view_bonus" : 2,
    "blocked" : False,
    "colour" : "brown",
    "characteristic" : "elevation",
  },
  { 
    "name" : "flat",
    "term_display" : '.',
    "movement" : 6, 
    "cover" : -2,
    "loot_chance" : 10,
    "view_bonus" : 1,
    "blocked" : False,
    "colour" : "yellow",
    "characteristic" : "wilderness",
  },
  { 
    "name" : "grassland",
    "term_display" : '.',
    "movement" : 6, 
    "cover" : -2,
    "loot_chance" : 10,
    "view_bonus" : 1,
    "blocked" : False,
    "colour" : "green",
    "characteristic" : "wilderness",
  },
  { 
    "name" : "clearing",
    "term_display" : '+',
    "movement" : 6, 
    "cover" : -2,
    "loot_chance" : 10,
    "view_bonus" : 1,
    "blocked" : False,
    "colour" : "green",
    "characteristic" : "foliage",
  },
  { 
    "name" : "ruins",
    "term_display" : 'x',
    "movement" : 6, 
    "cover" : -2,
    "loot_chance" : 10,
    "view_bonus" : 1,
    "blocked" : False,
    "colour" : "purple",
    "characteristic" : "urban",
  },
  { 
    "name" : "barren",
    "term_display" : '.',
    "movement" : 6, 
    "cover" : -2,
    "loot_chance" : 10,
    "view_bonus" : 1,
    "blocked" : False,
    "colour" : "red",
    "characteristic" : "wilderness",
  },
  { 
    "name" : "woodland",
    "term_display" : 't',
    "movement" : -2, 
    "cover" : 4,
    "loot_chance" : 10,
    "view_bonus" : -2,
    "blocked" : False,
    "characteristic" : "foliage",
    "colour": "green",
  },
  { 
    "name" : "forest",
    "term_display" : 'T',
    "movement" : -2, 
    "cover" : 4,
    "loot_chance" : 10,
    "view_bonus" : -2,
    "blocked" : False,
    "characteristic" : "foliage",
    "colour": "lightgreen",
  },
  { 
    "name" : "water",
    "term_display" : '~',
    "movement" : -2, 
    "cover" : 6,
    "loot_chance" : 10,
    "view_bonus" : 0,
    "blocked" : True,
    "characteristic" : "water",
    "colour": "cyan",
  },
  { 
    "name" : "city",
    "term_display" : 'H',
    "movement" : -2, 
    "cover" : 6,
    "loot_chance" : 5,
    "view_bonus" : -2,
    "blocked" : False,
    "characteristic" : "urban",
    "colour": "white",
  },
  { 
    "name" : "settlement",
    "term_display" : 'h',
    "movement" : -2, 
    "cover" : 6,
    "loot_chance" : 5,
    "view_bonus" : -2,
    "blocked" : False,
    "characteristic" : "urban",
    "colour": "lightgray",
  },
]
     
