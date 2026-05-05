import pygame,Zombie, Ruby

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (25, 200, 25)

class Game:
    """A class to help manage gameplay"""

    def __init__(self, player, zombie_group, platform_group, portal_group, bullet_group, ruby_group):
        """Initialize the game"""
        #Set constant variables
        # TODO: assign 30 to self.STARTING_ROUND_TIME
        self.STARTING_ROUND_TIME = 30
        # TODO: assign 5 to self.STARTING_ZOMBIE_CREATION_TIME
        self.STARTING_ZOMBIE_CREATION_TIME = 5

        #Set game values
        # TODO: assign 0 to self.score
        self.score = 0
        # TODO: assign 1 to self.round_number
        self.round_number = 1
        # TODO: assign 0 to self.frame_count
        self.frame_count = 0
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time
        self.round_time = self.STARTING_ROUND_TIME
        # TODO: assign self.STARTING_ZOMBIE_CREATION_TIME to self.zombie_creation_time
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME

        #Set fonts
        # TODO: assign pygame.font.Font() to self.title_font with these 2 arguments
        self.title_font = pygame.font.Font("fonts/Poultrygeist.ttf",48)
        #  1: "fonts/Poultrygeist.ttf"
        #  2: 48
        # TODO: assign pygame.font.Font() to self.HUD_font with these 2 arguments
        self.HUD_font = pygame.font.Font("fonts/Pixel.ttf",24)
        #  1: "fonts/Pixel.ttf"
        #  2: 24

        #Set sounds
        # TODO: assign pygame.mixer.Sound() to self.lost_ruby_sound with this 1 argument
        self.lost_ruby_sound = pygame.mixer.Sound(pygame.mixer.Sound())
        #  1: pygame.mixer.Sound()
        # TODO: assign pygame.mixer.Sound() to self.ruby_pickup_sound with this 1 argument
        self.ruby_pickup_sound = pygame.mixer.Sound("sounds/ruby_pickup.wav")
        #  1: "sounds/ruby_pickup.wav"
        # TODO: call pygame.mixer.music.load() with this 1 argument
        pygame.mixer.music.load("sounds/level_music.wav")
        #  1: "sounds/level_music.wav"

        #Attach groups and sprites
        # TODO: assign player to self.player
        self.player = player
        # TODO: assign zombie_group to self.zombie_group
        self.zombie_group = zombie_group
        # TODO: assign platform_group to self.platform_group
        self.platform_group = platform_group
        # TODO: assign portal_group to self.portal_group
        self.portal_group = portal_group
        # TODO: assign bullet_group to self.bullet_group
        self.bullet_group = bullet_group
        # TODO: assign ruby_group to self.ruby_group
        self.ruby_group = ruby_group


    def update(self):
        """Update the game"""
        #Update the round time every second
        # TODO: add 1 to self.frame_count
        self.frame_count += 1
        # TODO: if self.frame_count % FPS == 0:
        if self.frame_count % FPS == 0:
            # TODO: subtract 1 from self.round_time
            self.round_time -= 1
            # TODO: assign 0 to self.frame_count
            self.frame_count = 0

        # TODO: call self.check_collisions()
        self.check_collisions()
        # TODO: call self.add_zombie()
        self.add_zombie()
        # TODO: call self.check_round_completion()
        self.check_round_completion()
        # TODO: call self.check_game_over()
        self.check_game_over()


    def draw(self):
        """Draw the game HUD"""

        #Set text
        # TODO: assign self.HUD_font.render() to score_text with these 3 arguments
        score_text = self.HUD_font.render("Score: " + str(self.score),True,WHITE)
        #  1: "Score: " + str(self.score)
        #  2: True
        #  3: WHITE
        # TODO: assign score_text.get_rect() to score_rect
        score_rect = score_text.get_rect()
        # TODO: assign (10, WINDOW_HEIGHT - 50) to score_rect.topleft
        score_rect.topleft = (10, WINDOW_HEIGHT - 50)

        # TODO: assign self.HUD_font.render() to health_text with these 3 arguments
        health_text = self.HUD_font.render("Health: " + str(self.player.health),True,WHITE)
        #  1: "Health: " + str(self.player.health)
        #  2: True
        #  3: WHITE
        # TODO: assign health_text.get_rect() to health_rect
        health_rect = health_text.get_rect()
        # TODO: assign (10, WINDOW_HEIGHT - 25) to health_rect.topleft
        health_rect.topleft = (10, WINDOW_HEIGHT - 50)

        # TODO: assign self.title_font.render() to title_text with these 3 arguments
        title_text = self.title_font.render("Zombie Knight",True,GREEN)
        # TODO: assign title_text.get_rect() to title_rect
        # TODO: assign (WINDOW_WIDTH//2, WINDOW_HEIGHT - 25) to title_rect.center
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 25)
        # TODO: assign self.HUD_font.render() to round_text with these 3 arguments
        round_text = self.HUD_font.render("Night: " + str(self.round_number),True,WHITE)
        #  1: "Night: " + str(self.round_number,)
        #  2: True
        #  3: WHITE
        # TODO: assign round_text.get_rect() to round_rect
        # TODO: assign (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50) to round_rect.topright
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50)
        # TODO: assign self.HUD_font.render() to time_text with these 3 arguments
        time_text = self.HUD_font.render("Sunrise In: " + str(self.round_time),True,WHITE)
        #  1: "Sunrise In: " + str(self.round_time)
        #  2: True
        #  3: WHITE
        # TODO: assign time_text.get_rect() to time_rect
        time_rect = time_text.get_rect()
        # TODO: assign (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25) to time_rect.topright
        time_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25)

        #Draw the HUD
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: score_text
        #  2: score_rect
        display_surface.blit( score_rect, score_rect)
        # TODO: call display_surface.blit() with these 2 arguments
        display_surface.blit(health_text,health_rect)
        #  1: health_text
        #  2: health_rect
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: title_text
        #  2: title_rect
        display_surface.blit(title_text,title_rect)
        # TODO: call display_surface.blit() with these 2 arguments
        display_surface.blit(round_text,round_rect)
        #  1: round_text
        #  2: round_rect
        # TODO: call display_surface.blit() with these 2 arguments
        display_surface.blit(time_text,time_rect)
        #  1: time_text
        #  2: time_rect


    def add_zombie(self):
        """Add a zombie to the game"""
        #Check to add a zombie every second
        # TODO: if self.frame_count % FPS == 0:
        if self.frame_count % FPS == 0:
            #Only add a zombie if zombie creation time has passed
            # TODO: if self.round_time % self.zombie_creation_time == 0:
            if self.round_time % self.zombie_creation_time == 0:
                # TODO: assign Zombie() to zombie with these 4 arguments
                zombie = Zombie(self.platform_group,self.portal_group,self.round_number,5 + self.round_number)
                #  1: self.platform_group
                #  2: self.portal_group
                #  3: self.round_number
                #  4: 5 + self.round_number
                # TODO: call self.zombie_group.add() with this 1 argument
                self.zombie_group.add(zombie)
                #  1: zombie


    def check_collisions(self):
        """Check collisions that affect gameplay"""
        #See if any bullet in the bullet group hit a zombie in the zombie group
        collision_dict = pygame.sprite.groupcollide(self.bullet_group,self.zombie_group, True, False)
        if collision_dict:
            for zombies in collision_dict.values():
                for zombie in zombies:
                    zombie.hit_sound.play()
                    zombie.is_dead = True
                    zombie.animate_death = True
        #See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        # TODO: assign pygame.sprite.spritecollide() to collision_list with these 3 arguments
        collision_list = pygame.sprite.spritecollide(self.player,self.zombie_group,False)
        #  1: self.player
        #  2: self.zombie_group
        #  3: False
        # TODO: if collision_list:
        if collision_list:
            # TODO: for zombie in collision_list:
            for zombie in collision_list:
                #The zombie is dead; stomp it
                # TODO: if zombie.is_dead:
                if zombie.is_dead:
                    # TODO: call zombie.kick_sound.play()
                    zombie.kick_sound.play()
                    # TODO: call zombie.kill()
                    zombie.kill()
                    # TODO: add 25 to self.score
                    self.score = 25

                    # TODO: assign Ruby() to ruby with these 2 arguments
                    ruby = Ruby(self.platform_group,self.portal_group)
                    #  1: self.platform_group
                    #  2: self.portal_group
                    # TODO: call self.ruby_group.add() with this 1 argument
                    self.ruby_group.add(ruby)
                    #  1: ruby
                #The zombie isn't dead, so take damage
                # TODO: else:
                else:
                    # TODO: subtract 20 from self.player.health
                    self.player.health -= 20
                    # TODO: call self.player.hit_sound.play()
                    self.player.hit_sound.play()
                    #Move the player to not continually take damage
                    # TODO: subtract 256*zombie.direction from self.player.position.x
                    self.player.position.x -= 256*zombie.direction
                    # TODO: assign self.player.position to self.player.rect.bottomleft
                    self.player.rect.bottomleft = self.player.position

        #See if a player collided with a ruby
        if pygame.sprite.spritecollide(self.player, self.ruby_group, True):
            self.ruby_pickup_sound.play()
            self.score += 100
            self.player.health += 10
            if self.player.health > self.player.STARTING_HEALTH:
                self.player.health = self.player.STARTING_HEALTH
        #See if a living zombie collided with a ruby
        # TODO: for zombie in self.zombie_group:
        for zombie in self.zombie_group:
            # TODO: if not zombie.is_dead:
            if not zombie.is_dead:
                # TODO: if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                    # TODO: call self.lost_ruby_sound.play()
                    self.lost_ruby_sound.play()
            # TODO: assign Zombie() to zombie with these 4 arguments
            zombie = Zombie(self.platform_group,self.portal_group,self.round_number,5 + self.round_number)
            #  1: self.platform_group
                    #  2: self.portal_group
                    #  3: self.round_number
                    #  4: 5 + self.round_number
                    # TODO: call self.zombie_group.add() with this 1 argument
            self.zombie_group.add(zombie)
                    #  1: zombie


    def check_round_completion(self):
        """Check if the player survived a single night"""
        # TODO: if self.round_time == 0:
            # TODO: call self.start_new_round()
        if self.round_time == 0:
            self.start_new_round()
    def check_game_over(self):
        """Check to see if the player lost the game"""
            # TODO: call self.reset_game()
        if self.player.health <= 0:
            pygame.mixer.music.stop()
            self.pause_game("Game Over! Final Score: " + str(self.score),"Press 'Enter' to play again..." )
            self.reset_game()
    def start_new_round(self):
        """Start a new night"""
        # TODO: add 1 to self.round_number
        self.round_number += 1
        #Decrease zombie creation time...more zombies
        # TODO: if self.round_number < self.STARTING_ZOMBIE_CREATION_TIME:
        if self.round_number < self.STARTING_ZOMBIE_CREATION_TIME:
            # TODO: subtract 1 from self.zombie_creation_time
            self.zombie_creation_time -= 1

        #Reset round values
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time
        self.round_time = self.STARTING_ROUND_TIME

        # TODO: call self.zombie_group.empty()
        self.zombie_group.empty()
        # TODO: call self.ruby_group.empty()
        self.ruby_group.empty()
        # TODO: call self.bullet_group.empty()
        self.bullet_group.empty()

        # TODO: call self.player.reset()
        self.player.reset()

        # TODO: call self.pause_game() with these 2 arguments
        self.pause_game("You survived the night!","Press 'Enter' to continue...")
        #  1: "You survived the night!"
        #  2: "Press 'Enter' to continue..."


    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        # TODO: call pygame.mixer.music.pause()
        pygame.mixer.music.pause()
        #Create main pause text
        # TODO: assign main_text.get_rect() to main_rect
        # TODO: assign (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) to main_rect.center
        main_text = self.title_font.render( main_text, True, GREEN)
        main_rect = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        #Create sub pause text
        # TODO: assign self.title_font.render() to sub_text with these 3 arguments
        sub_text = self.title_font.render(sub_text,True, WHITE)
        #  1: sub_text
        #  2: True
        #  3: WHITE
        # TODO: assign sub_text.get_rect() to sub_rect
        sub_rect = sub_text.get_rect()
        # TODO: assign (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64) to sub_rect.center
        sub_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

        #Display the pause text
        # TODO: call display_surface.fill() with this 1 argument
        display_surface.fill(BLACK)
        #  1: BLACK
        # TODO: call display_surface.blit() with these 2 arguments
        display_surface.blit(main_text,main_rect)
        #  1: main_text
        #  2: main_rect
        # TODO: call display_surface.blit() with these 2 arguments
        #  1: sub_text
        #  2: sub_rect
        display_surface.blit(sub_text, sub_rect)
        # TODO: call pygame.display.update()
        pygame.display.update()

        #Pause the game until user hits enter or quits
        # TODO: assign True to is_paused
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # TODO: if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    #User wants to continue
                    # TODO: if event.key == pygame.K_RETURN:
                    if event.key == pygame.K_RETURN:
                        # TODO: assign False to is_paused
                        is_paused
                        # TODO: call pygame.mixer.music.unpause()
                    pygame.mixer.music.unpause()

                #User wants to quit
                # TODO: if event.type == pygame.QUIT:
        if event.type == pygame.QUIT:
                    # TODO: assign False to is_paused
                    is_paused = False
                    # TODO: call pygame.event.post() with this 1 argument
                    pygame.event.post(pygame.event.Event(pygame.QUIT),pygame.mixer.music.stop())
                    #  1: pygame.event.Event(pygame.QUIT)
                    # TODO: call pygame.mixer.music.stop()
        pygame.mixer.music.stop()
    def reset_game(self):
        """Reset the game"""
        self.score = 0
        self.round_number = 1
        self.round_time = self.STARTING_ROUND_TIME
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME
        self.player.health = self.player.STARTING_HEALTH
        self.player.reset()
        self.zombie_group.empty()
        self.ruby_group.empty()
        self.bullet_group.empty()
        pygame.mixer.music.play(-1 ,0.0)