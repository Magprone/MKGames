import pygame
import operations
from level_screen import LevelScreen
from game_screen import GameScreen


class Setup:
    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 0, 0
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        self.size = self.width, self.height = pygame.display.get_window_size()
        pygame.display.set_caption('BeerFlight')

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.operations = operations
        self.StartScreen = LevelScreen
        self.GameScreen = GameScreen

        self.state = self.StartScreen()
        while True:
            self.state = self.state.start(self)


if __name__ == '__main__':
    Setup()