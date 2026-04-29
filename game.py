import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (25, 200, 25)

class Game:
    """A class to help manage gameplay"""

    def __init__(self, player, zombie_group, platform_group, portal_group, bullet_group, ruby_group):
        """Initialize the game"""
        self.player = player
        self.zombie_group = zombie_group
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group
        self.ruby_group = ruby_group
        self.zombie_group.start_new_round()
        self.platform_group.start_new_round()
        self.portal_group.start_new_round()
        self.bullet_group.start_new_round()
        self.ruby_group.start_new_round()
    def update(self):
        """Update the game"""
        self.zombie_group.update()
        self.platform_group.update()
        self.portal_group.update()
        self.bullet_group.update()
        self.ruby_group.update()
    def draw(self):
        """Draw the game HUD"""
        self.zombie_group.draw()
        self.platform_group.draw()
        self.portal_group.draw()
        self.bullet_group.draw()
        self.ruby_group.draw()
    def add_zombie(self):
        """Add a zombie to the game"""
        self.zombie_group.add_zombie()
    def check_collisions(self):
        """Check collisions that affect gameplay"""
        self.zombie_group.check_collisions()
        self.platform_group.check_collisions()
        self.portal_group.check_collisions()
        self.bullet_group.check_collisions()
        self.ruby_group.check_collisions()
    def check_round_completion(self):
        """Check if the player survived a single night"""
        self.zombie_group.check_round_completion()
        self.platform_group.check_round_completion()
        self.portal_group.check_round_completion()
        self.bullet_group.check_round_completion()
        self.ruby_group.check_round_completion()
    def check_game_over(self):
        """Check to see if the player lost the game"""
        self.zombie_group.check_game_over()
        self.platform_group.check_game_over()
        self.portal_group.check_game_over()
        self.bullet_group.check_game_over()
        self.ruby_group.check_game_over()
    def start_new_round(self):
        """Start a new night"""
        self.zombie_group.start_new_round()
        self.platform_group.start_new_round()
        self.portal_group.start_new_round()
        self.bullet_group.start_new_round()
        self.ruby_group.start_new_round()
    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        self.zombie_group.pause_game(main_text, sub_text)
        self.platform_group.pause_game(main_text, sub_text)
        self.portal_group.pause_game(main_text, sub_text)
        self.bullet_group.pause_game(main_text, sub_text)
        self.ruby_group.pause_game(main_text, sub_text)
    def reset_game(self):
        """Reset the game"""
        self.zombie_group.reset_game()
        self.platform_group.reset_game()
        self.portal_group.reset_game()
        self.bullet_group.reset_game()
        self.ruby_group.reset_game()