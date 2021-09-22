from random import randrange, random
import sys
from cnf.tiles.tiles import tiles
from cnf.tiles.tile_characteristics import characteristics
from cnf.colours import Colours
from src.mapgen.maptile import MapTile
from src.mapgen.tilemanager import TileManager

class Map():
  """
  Generates a map using a class instance
  must be passed a map file.
  param int height: the amount of tiles high the map will be
  param int width: the amount of tiles wide the map will be
  param boolean colours: a boolean operator specifying to use colour for
                         console printing or not, if using a shell for
                         playing/testing.
  param string shell: what shell to use if using a console
  param **kargs: extra arguments include;
    - dict density: a key pair value of characteristic name and chance tuple
  """

  def __init__(self, height=50, width=50, colours=False, shell=False, **kargs):
    self._map_tiles = tiles
    self._tile_key_map = {}
    self.height = height
    self.width = width
    self._map = []
    self._colours = False
    self._shell = shell
    self._tile_manager = TileManager()
    self._tile_types = {}
    self._tile_characteristics = characteristics

    for tile in self._map_tiles:
      tile_type = tile['characteristic']
      if not tile_type in self._tile_types:
        self._tile_types[tile_type] = []
      self._tile_types[tile_type].append(tile['name'])

    if colours and self.supports_colour():
      #@TODO Get shell type, do this cleverly etc
      self._colours = Colours(self._shell)

  def reset_map(self):
    """
    reset the map to an empty array
    """
    self._map = []

  def build_map(self):
    """
    build out an initial map, adds as many rows as height and as many
    columns as width, using random tiles, however these tiles are
    generated in such a way to keep rivers running together
    tracks running together, lakes etc.
    """
    self.reset_map()
    # create a name to tile keymapping
    for idx, tile in enumerate(self._map_tiles):
      name = tile['name']
      self._tile_key_map[name] = idx

    # loop height first, add an array as row per height
    for y in range(0, self.height):
      self._map.append([])
      for x in range(0, self.width):
        self.process_tile(x, y)

    self.map_sparkle()

  def map_sparkle(self):
    """
    some clean up routines once the intial map has been built, this
    can do things like replace tiles surrounded by water with water,
    or anything of the like to clean a pregenerated map up for play.
    @TODO make this pull from a sparkle directory, that has routines
          defined for each tile. which means little plugins can be
          written per tile type, to be run during map sparkle.
    """
    # fix non-water tiles surrounded by water.
    for y in range(1, self.height):
      for x in range(0, self.width):
        proximity = self._tile_manager.tile_proximity(self._map, x, y)
        surrounded = True
        for key in proximity:
          val = proximity[key]
          if val and val.characteristic:
            char_type = val.characteristic['name']
            # set not surrounded if we have a tile that's not water in proximity
            if not char_type == 'water':
              surrounded = False
        # if surrounded, replace tile with another water tile
        if surrounded:
          self._map[y][x] = self.new_tile_of_type('water')


  def new_tile_of_type(self, tile_type):
    """
    get a new tile of a given type
    param str type: a tile type name
    """
    tile = None
    if tile_type in self._tile_types:
      random_new_tile_range = len(self._tile_types[tile_type])
      tile_name = self._tile_types[tile_type][randrange(0, random_new_tile_range)]
      tile_idx = self._tile_key_map[tile_name]
      tile = MapTile(self._map_tiles[tile_idx], self._tile_characteristics)
    return tile

  def process_tile(self, x, y):
    """
    take in a tile on map generation, and check it to make sure tiles are
    grouped together cleverly and not just a big random mess.

    param int x: the x coordinate on the map we're processing
    param int y: the y coordinate on the map we're processing
    """
    tile = False
    # get the tile proximities so we can judge the best tile to place
    proximity = self._tile_manager.tile_proximity(self._map, x, y)
    for key in proximity:
      val = proximity[key]
      # need a MapTile a chance value in the characteristics and to roll successfully for chance 
      if val and val.characteristic:
        attr = val.characteristic['attr']
        char_type = val.characteristic['name']
        # if we succeed add a new tile of the same type, not neccessarily the same tile
        if attr and 'chance' in attr and random() < (attr['chance'] / 100.0):
          #random_new_tile_range = len(self._tile_types[char_type])
          #tile_name = self._tile_types[char_type][randrange(0, random_new_tile_range)]
          #tile_idx = self._tile_key_map[tile_name]
          #tile = MapTile(self._map_tiles[tile_idx], self._tile_characteristics)
          tile = self.new_tile_of_type(char_type)
          # don't break, keep going for more of a chance

    # get a random tile instead
    if not tile:
      new_tile = self._map_tiles[randrange(0, len(self._map_tiles))]
      tile = MapTile(new_tile, self._tile_characteristics)

    self._map[y].append(tile)

  def supports_colour(self):
    """
    Returns True if the running system's terminal supports color, and False
    otherwise. (Taken from Django)
    """
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                  'ANSICON' in os.environ)
    # isatty is not always implemented, #6223.
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    if not supported_platform or not is_a_tty:
        return False
    return True

  def change_density(self, name, chance):
    """
    change the density of a tile type
    param string name: the tile characteristic name
    param tuple change: the tuple ratio of chance
    """
    if name in self._tile_characteristics:
      # if we fail, just don't set
      try:
        chance = int(chance)
      except Exception:
        pass
      if type(chance) == int and chance > 0 and chance < 100:
        self._tile_characteristics[name]['chance'] = chance

  def get_density(self):
    """
    return just the characteristic chance identified by name
    from the characteristics in a key/val dict
    """
    density = {}
    for name in self._tile_characteristics:
      characteristic = self._tile_characteristics[name]
      density[name] = characteristic['chance']

    return density



  def printmap(self):
    """
    print the map as a string; useful for console interfaces
    """
    map_str = ""
    for x in self._map:
      row = ""
      for y in x:
        # paint tile a colour if applicable/available
        if self._colours and y.colour:
          row = row + self._colours.paint(y.colour, y.term_display)
        else:
          row = row + y.term_display
      map_str = map_str + row + "\n"

    return map_str


#TESTING#
if __name__ == "__main__":
  pass
