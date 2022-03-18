import random


class Room:

    m_terrain = [] 
    
    def __init__(self, sizex, sizey, seed):
      
        for i in range (sizex):
            n=[]
            for j in range(sizey):
                random.seed(seed + i + j)
                n.append (random.randint (0, 5))
            
            self.m_terrain.append(n) 
        
        # print (self.m_terrain)