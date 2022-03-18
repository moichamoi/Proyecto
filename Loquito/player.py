from position import Position
from rooms import Room

class Jugador:


    def __init__ (self):
            self.m_vida = 10
            self.m_pos = Position(0,0,0)
            self.m_inv = 0
            self.m_room = 0
            self.m_dmg = True
        

    def dmg (self, enemy):
        pass

    def move(self, rooms, direction):
        print ("El jugador se movio")
        print (rooms[self.m_pos.m_croom].m_terrain[self.m_pos.m_x][self.m_pos.m_y])
        if direction == "w":
            print (rooms[self.m_pos.m_croom].m_terrain[self.m_pos.m_y-1][self.m_pos.m_x])
        if direction == "s":
            print (rooms[self.m_pos.m_croom].m_terrain[self.m_pos.m_y+1][self.m_pos.m_x])
        if direction == "a":
            print (rooms[self.m_pos.m_croom].m_terrain[self.m_pos.m_y][self.m_pos.m_x-1])
        if direction == "d":
            print (rooms[self.m_pos.m_croom].m_terrain[self.m_pos.m_y][self.m_pos.m_x+1])
