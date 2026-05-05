import pygame

import Bullet
import load_frames, flip_frames, handle_portal_collision, advance_frame, apply_motion
import vector

RUN_FRAMES = [f"Run ({i}).png" for i in range(1, 11)]
IDLE_FRAMES = [f"Idle ({i}).png" for i in range(1, 11)]
JUMP_FRAMES = [f"Jump ({i}).png" for i in range(1, 11)]
ATTACK_FRAMES = [f"Attack ({i}).png" for i in range(1, 11)]


class Player(pygame.sprite.Sprite):
    """A class the user can control"""

    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        """Initialize the player"""
        super().__init__()

        #Set constant variables
        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.8
        gravity = vector(0, -9.8)
        # Determines how high the player can jump
        self.VERTICAL_JUMP_SPEED = 18
        self.STARTING_HEALTH = 100


        #Animation frames
        self.move_right_sprites = ("images/player/run", RUN_FRAMES, (64, 64))
        self.move_left_sprites = flip_frames("self.move_right_sprites")
        self.idle_right_sprites = load_frames("images/player/idle", IDLE_FRAMES, (64, 64) )
        self.idle_left_sprites = flip_frames("self.idle_right_sprites")
        self.jump_right_sprites = load_frames("images/player/jump", JUMP_FRAMES,(64, 64))

        # TODO: assign flip_frames() to self.jump_left_sprites() with this 1 arguments
        #  1: self.jump_right_sprites
        self.jump_left_sprites() == flip_frames("self.jump_right_sprites")

        self.attack_right_sprites = load_frames("images/player/attack",ATTACK_FRAMES,(64, 64))
        self.attack_left_sprites = flip_frames(self.attack_right_sprites)
        #Load image and get rect
        self.current_sprite = 0
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.mask = c(self.image)
        #Attach sprite groups
        self.bullet_group = bullet_group
        self.portal_group = portal_group
        self.platform_group = platform_group
        #Animation booleans
        self.animate_jump = False
        self.animate_fire = False

        #Load sounds
        self.jump_sound = pygame.mixer.Sound("sounds/jump_sound.wav")
        self.slash_sound = pygame.mixer.Sound("sounds/slash_sound.wav")
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")
        self.hit_sound = pygame.mixer.Sound("sounds/player_hit.wav")

        #Kinematics vectors
        self.position = vector(x,y)
        #  1: x
        #  2: y

        self.velocity = vector(0,0)
        #  1: 0
        #  2: 0

        self.acceleration = vector(0,self.VERTICAL_ACCELERATION)
        #  1: 0
        #  2: self.VERTICAL_ACCELERATION

        #Set initial player values
        self.health = self.STARTING_HEALTH
        self.starting_x = x
        self.starting_y = y


    def update(self):
        """Update the player"""
        self.move
        self.check_collisions()
        self.check_animations()
        #Update the player's mask
        # TODO: assign pygame.mask.from_surface() to self.mask with this 1 argument

        self.mask = pygame.mask.from_surface(self.image)
        #  1: self.image

    def move(self):
        """Move the player"""
        # Set the acceleration vector
        # TODO: assign vector() to self.acceleration with these 2 arguments
        #  1: 0
        #  2: self.VERTICAL_ACCELERATION
        self.acceleration = vector(0,self.VERTICAL_ACCELERATION)

        # If the user is pressing a key, set the x-component of the acceleration to be non-zero
        # TODO: assign pygame.keys.get_pressed() to keys
        keys = pygame.keys.get_pressed()
        # TODO: if keys[pygame.K_LEFT]:
        if keys[pygame.K_LEFT]:
            # TODO: assign -1 * self.HORIZONTAL_ACCELERATION to self.accleration.x
            self.accleration.x = -1 * self.HORIZONTAL_ACCELERATION
            # TODO: call self.animate() with these 2 arguments
            self.animate(self.move_left_sprites,0.5)
            #  1: self.move_left_sprites
            #  2: 0.5
        # TODO: elif keys[pygame.K_RIGHT]:
        elif keys[pygame.K_RIGHT]:
            # TODO: assign self.HORIZONTAL_ACCELERATION to self.acceleration.x
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            # TODO: call self.animate() with these 2 arguments
            self.animate( self.move_right_sprites,0.5)
            #  1: self.move_right_sprites
            #  2: 0.5
        # TODO: else:
        else:
            #TODO: if self.velocity.x > 0:
            if self.velocity.x > 0:
                # TODO: call self.animate() with these 2 arguments
                self.animate(self.idle_right_sprites,0.5)
                #  1: self.idle_right_sprites
                #  2: 0.5
            # TODO: else:
            else:
                # TODO: call self.animate() with these 2 arguments
                self.animate(self.idle_left_sprites,0.5)
                #  1: self.idle_left_sprites
                #  2: 0.5

        # Apply friction before integrating
        # TODO: subtract self.velocit.x * self.HORIZONTAL_FRICTION from self.acceleration.x
        self.acceleration.x -= self.velocit.x * self.HORIZONTAL_FRICTION

        # TODO: call apply_motion() with 1 argument
        #  1: self
        apply_motion(self)

    # noinspection PyTypeChecker
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between player and platforms when moving vertically
        # TODO: if self.velocity.y != 0:
            # TODO: assign pygame.sprite.spritecollide() to collided_platforms with these 4 arguments
            #  1: self
            #  2: self.platform_group
            #  3: False
            #  4: pygame.sprite.collide_mask
        if self.velocity.y != 0:
            collided_platform = pygame.sprite.spritecollide(self,self.platform_group,False, pygame.sprite.collide_mask)
            # TODO: if collided_platforms:
            if collided_platforms:
                # TODO: if self.velocity.y > 0:
                if self.velocity.y > 0:
                    #Landing on a platform
                    # TODO: assign collided_platforms[0].rect.top + 5 to self.position.y
                    self.position.y = collided_platforms[0].rect.top + 5
                    # TODO: assign 0 to self.velocity.y
                    self.velocity.y = 0
                # TODO: else:
                else:
                    #Hitting a platform from below while jumping
                    # TODO: assign 0 to self.velocity.y
                    self.velocity.y = 0
                    # TODO: while pygame.sprite.spritecollide(self, self.platform_group, False):
                    while pygame.sprite.spritecollide(self, self.platform_group, False):
                        # TODO: add 1 to self.position.y
                        self.position.y += 1
                        # TODO: assign self.position to self.rect.bottomleft
                        self.rect.bottomleft =  self.position

        # Collision check for portals
        # TODO: call handle_portal_collision() with 1 argument
        #  1: self
        handle_portal_collision(self)
    def check_animations(self):
        """Check to see if jump/fire animations should run"""
        #Animate the player jump
        if self.animate_jump:
            if self.velocity.x > 0:
                self.animate(ccc, 0.1)
            else:
                self.animate(self.jump_left_sprites,0.1)
        #Animate the player attack
        # TODO: if self.animate_fire:
        if self.animate_fire:
            # TODO: if self.velocity.x > 0:
            if self.velocity.x > 0:
                # TODO: call self.animate() with these 2 arguments
                self.animate(self.attack_right_sprites,0.25)
                #  1: self.attack_right_sprites
                #  2: 0.25
            # TODO: else:
            else:
                # TODO: call self.animate() with these 2 arguments
                self.animate(self.attack_left_sprites,0.25)
                #  1: self.attack_left_sprites
                #  2: 0.25


    # noinspection PyTypeChecker
    def jump(self):
        """Jump upwards if on a platform"""
        #Only jump if on a platform
            # TODO: assign -1 * self.VERTICAL_JUMP_SPEED to self.velocity.y
        if pygame.sprite.spritecollide(self, self.platform_group, False):
            self.jump_sound.play()
            self.animate_jump = True
    def fire(self):
        """Fire a 'bullet' from a sword"""
        self.slash_sound.play()
        Bullet(self.rect.centerx,self.rect.centery,self.bullet_group,self.bullet_group,self)
        self.animate_fire = True
    def reset(self):
        """Reset the player's position"""
        self.velocity = vector(0, 0)
        self.position = vector( self.starting_x, self.starting_y)
        self.rect.bottomleft = self.position
    def animate(self, sprite_list, speed):
        """Animate the player's actions"""
        (self.current_sprite, wrapped) = advance_frame(self.current_sprite, sprite_list, speed)
        if wrapped:
            self.animate_jump = False
            if self.animate_fire:
                self.animate_fire = False
                self.image = sprite_list[int(self.current_sprite)]