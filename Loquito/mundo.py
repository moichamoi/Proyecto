from rooms import Room
import random


class World:

    m_rooms = []

    def __init__(self):

        for i in range (4):
            self.m_rooms.append(Room(5,5,i))
        
        for w in range(5):
            for i in range(5):
                for j in range(5):
                    random.seed(w + i + j)
                    print(random.randint(0, 9), end = " ")
                print()
            print()
            # print (self.m_rooms[i].m_terrain)

        
