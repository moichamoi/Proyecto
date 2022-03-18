from player import Jugador
from mundo import World

class App:

    m_player = Jugador()
    m_world = World ()

    def __init__(self):
        self.m_com = ''

    def run(self):
        while (self.m_com != "exit"):
            m_com = input(str("A donde te quieres mover? "))
            if (m_com == 'w' or m_com == 'a' or m_com == 's' or m_com == 'd'):
                self.m_player.move(self.m_world.m_rooms,self.m_com)
