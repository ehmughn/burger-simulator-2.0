import pygame

class Image:
    
    def __init__(self, directory: str):
        self.image = pygame.image.load(directory)

    def transform_image(self, width: int, height: int) -> pygame.Surface:
        return pygame.transform.scale(self.image, (width, height))