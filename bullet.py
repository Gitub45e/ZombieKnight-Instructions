import pygame


class Bullet(pygame.sprite.Sprite):
    """A projectile launched by the player"""

    def __init__(self, x, y, bullet_group, player):
        """Initialize the bullet"""
        super().__init__()

        #Set constant variables
        self.VELOCITY = 20
        # TODO: assign 500 to self.RANGE

        #Load image and get rect
        if player.velocity.x > 0:
            self.image = pygame.transform.scale(pygame.image.load("images/player.slash.png"), (32, 32))
        else:
            self.image = pygame.transform.scale(pygame.transform.flip(pygame.image.load("images/player/slash.png"), True, False), (32, 32))
            self.VELOCITY = -1 * self.VELOCITY

        # TODO: assign self.image.get_rect() to self.rect
        # TODO: assign (x, y) to self.rect.center

        # TODO: assign x to self.starting_x

        # TODO: call bullet_group.add() with this 1 argument
        #  1: self


    def update(self):
        """Update the bullet"""
        # TODO: add self.VELOCITY to self.rect.x

        #If the bullet has passed the range, kill it
        # TODO: if abs(self.rect.x - self.starting_x) > self.RANGE:
            # TODO: self.kill()
