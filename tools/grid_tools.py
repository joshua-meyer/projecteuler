def grid_value(grid,location):
  return grid[location[0]][location[1]]

# Assumes the grid is well formed, but mistrusts the location.
def is_in_grid(grid,location):
  try:
    if len(location) < 2:
      return False
    elif not type(location[0]) == int:
      return False
    elif not type(location[1]) == int:
      return False
    elif location[0] < 0 or location[0] >= len(grid):
      return False
    elif location[1] < 0 or location[1] >= len(grid[location[0]]):
      return False
    else:
      return True
  except ValueError:
    return False
