
class MapTile():
  """
  the tile class, each tile is loaded into a 
  tile object from the config during map generation
  param dict dict_tile: a dictionary style tile
  param dict characteristics: a dict of tile characteristics
  """
  def __init__(self, dict_tile, characteristics):
    # must be a dictionary tile to add
    if not type(dict_tile) == dict:
      raise Exception

    self.__construct_tile(dict_tile)

        
  def __construct_tile(self, dict_tile):
    """
    build the actual tile out into the class using
    allowed attribute keys only. these keys should
    match the keys defined in the tiles.py file in
    the cnf directory. 
    param dict dict_tile: the dict tile to initialise the oobject as 
    """
    allowed_keys = ["name", "term_display", "movement", "cover", "loot_chance", "view_bonus", "blocked", "colour", "characteristic"]
    # set only the allowed values
    for key in dict_tile:
      if key in allowed_keys:
        setattr(self, key, dict_tile[key])
    # set None for missing tile variables
    for key in allowed_keys:
      if not key in dict_tile:
        setattr(self, key, None)

    # if we have a characteristic id, then we import the
    # characteristics, find the characteristic and store
    # it as a dictionary with the name as the identifier
    # and attr as the attribute contents
    if self.characteristic:
      from cnf.tiles.tile_characteristics import characteristics
      if self.characteristic in characteristics:
        self.characteristic = {
          "name" : self.characteristic, 
          "attr" : characteristics[self.characteristic]
        }
      else:
         self.characteristic = None
      
      
    
