from utils import *


class Snake:
    
    
    def __init__(self):
        
        self.body_pos = [[3, 3], [2, 3],[ 1, 3],[ 0, 3], [0, 4]]
        self.body_dir = [[1, 0],[1, 0],[1, 0],[1, 0], [0, -1]]
        self.previus_dir = (self.body_dir[0][0], self.body_dir[0][1])
    
    def move_snake(self):

        # head
        
        new_pos = [0, 0]
        
        new_pos[0] = (self.body_pos[0][0] + self.body_dir[0][0]) % grid_w
        new_pos[1] = (self.body_pos[0][1] + self.body_dir[0][1]) % grid_h
        
        if not self.check_chollision(new_pos):
            self.body_pos[0][0] = new_pos[0]
            self.body_pos[0][1] = new_pos[1]
            self.previus_dir = (self.body_dir[0][0], self.body_dir[0][1])
        else:
            return False
        
    
        # body
        for index in reversed(range(1, len(self.body_pos))):
            self.body_pos[index][0] = (self.body_pos[index][0] + self.body_dir[index][0]) % grid_w
            self.body_pos[index][1] = (self.body_pos[index][1] + self.body_dir[index][1]) % grid_h
            
            self.body_dir[index][0] = self.body_dir[index-1][0]
            self.body_dir[index][1] = self.body_dir[index-1][1]
            
        return True
        
    def change_dir(self, dir_x, dir_y):
        
        if( (dir_x, dir_y) != (self.previus_dir[0]*-1, self.previus_dir[1]*-1)):
            self.body_dir[0][0] = dir_x
            self.body_dir[0][1] = dir_y  
    
    def check_collision_with_head(self, taget):
        
        if self.body_pos[0][0] == taget[0] and self.body_pos[0][1] == taget[1]:
            return True
        
        return False
    
    def check_chollision(self, target):
        for pos in self.body_pos:
            if target[0] == pos[0] and target[1] == pos[1]:
                return True
    
        return False 
    
    def eat(self, food):
        
        if self.check_collision_with_head(food):
            self.body_pos.append([self.body_pos[-1][0], self.body_pos[-1][1]])
            self.body_dir.append([0, 0])
            return True
        
        return False