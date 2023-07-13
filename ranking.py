import pygame
import sqlite3
from constants import *
class Ranking:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("Juego_freeknight\mis_assets\\btn\Banner01.png"),(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/2))
        self.player_name = None

    def create_db(self):
        connection = sqlite3.connect("ranking.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ranking (name TEXT,score TEXT)")  
        connection.close()

    def insert_player(self,score):
        connection = sqlite3.connect("ranking.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO ranking VALUES (?,?)",(self.player_name,score))
        connection.commit()
        connection.close()

    def print_ranking(self,screen):
        connection = sqlite3.connect("ranking.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name, score FROM ranking")
        rows = cursor.fetchall()
        text = "Ranking"
        for row in rows:
            name = row[0]
            score = row[1]
            line = "{0}: {1}\n".format(name,score)
            text += line
        menu_text = pygame.font.SysFont("Terminal",100).render(text,True,C_BLACK)
        screen.blit(menu_text,menu_text.get_rect(center=(WINDOWS_WIDTH/2,WINDOWS_HEIGHT/3)))
        connection.close()