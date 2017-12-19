class Tile(object):
    
    def __init__(self, width, length):
        self.width=width
        self.length=length
        
    def cost_of_each_tile(self):
        cost=float(raw_input('Please provide the cost of each tile: '))
        
        return cost
    
    
    def no_of_tiles(self, floor_width, floor_length):
        tile_no=(round(floor_width/self.width,0))*(round(floor_length/self.length,0))        
        return tile_no
    
        
    def Cost_of_Tiles(self, tile_no, cost_tile):
        return tile_no*cost_tile
    

#Main Program

width=float(raw_input('Please input width of tile: '))
length=float(raw_input('Please input length of tile: '))

tile=Tile(width, length)
floor_width=float(raw_input('Please input width of floor: '))
floor_length=float(raw_input('Please input length of floor: '))

tile.Cost_of_Tiles(tile.no_of_tiles(floor_width,floor_length),tile.cost_of_each_tile())
