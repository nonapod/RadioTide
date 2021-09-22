class TileManager():
  """
  This class works soely with operations regarding tiles,
  updating tiles, checking proximity, changing tiles,
  checking stats, adding stats etc.
  """

  def __init__(self):
    self.UP = (0, -1)
    self.DOWN = (0, 1)
    self.LEFT = (-1, 0)
    self.RIGHT = (1, 0)
    self.UP_LEFT = (-1, -1)
    self.UP_RIGHT = (1, -1)
    self.UP_LEFT = (-1, -1)
    self.DOWN_RIGHT = (1, 1)
    self.DOWN_LEFT = (-1, 1)
    

  def tile_proximity(self, gamemap, x, y): 
    """
    get a directional list of tiles in proximity of the current one.
    param int x: the x coordinate on the map we're checking
    param int y: the y coordinate on the map we're checking 
    param bool tile: whether or not to include the full tile in the result or id 
    return dict: each value either has a tile name, a bool, or a full blown tile
      {up:MapTile/False, upleft:MapTile/False, upright:MapTile/False, left: MapTile/False}
    """
    # parameters of positions to check
    check = {"up": self.UP, "upleft": self.UP_LEFT, "left": self.LEFT, "upright": self.UP_RIGHT}
    for key in check:
      try:
        cy = y + check[key][1]
        cx = x + check[key][0] 
        cy = cy if cy >= 0 else 0
        cx = cx if cx >= 0 else 0

        # if we're on the first row of y, then we can't go up
        if y == 0 and (key == 'upleft' or key == 'upright' or key == 'up'): 
          raise Exception
        # if we're on the first row of x, then we can't go left 
        if x == 0 and (key == 'left'):
          raise Exception
        check[key] = gamemap[cy][cx]

      # no proximity, set false
      except Exception as e:
        check[key] = False
        continue

    return check
