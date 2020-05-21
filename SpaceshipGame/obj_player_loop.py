# COLLISION_CHECK

# In the following if-statements, we do what's known as a collision check
# between our various objects.

# The way an if-statement works is like this ->
# 1) We need to set up an actual comparison. Here we check if a
# player has collided with an asteroid! Because we are inside of an
# 'obj_player' we can use the word "self" to describe a current player.
# As for the asteroid, we just use the name of it's object, which is
# 'obj-asteroid'.

# To make sure we only use the asteroid that came in contact with our
# player, we need to set our 'asteroid' variable to it! How do we do that?
# The result of the collision_check returns it to us!

# Parentheses show us what is known as a 'method call'. A method is
# nothing more than a bunch of code designed to do something specific,
# usually indicated by its name. We call that bunch of code a 'function'.
# Here we give the necessary parameters to the collision_check function,
# which in return gives us either a positive or a negative answer.
if collision_check(self, 'obj_asteroid'):
  # If the function returns us a positive answer, meaning the 2 objects
  # did collide, we then proceed to destroy that specific asteroid
  # and lower the health of our player by 1.
  asteroid = collision_check(self, 'obj_asteroid')
  destroy(asteroid)
  self.health = self.health - 1

# We use the exact SAME idea in the next 2 if-statements, except for
# asteroids, we check for collision with shields, which gives us 1 health
# back and destroys the shield.
if collision_check(self, 'obj_shield'):
  shield = collision_check(self, 'obj_shield')
  destroy(shield)
  health = health + 1

# Or with enemy projectiles, which take away 1 health from the player
# and destroy the enemy projectile.
if collision_check(self, 'obj_enemy_projectile'):
  enemyProjectile = collision_check(self, 'obj_enemy_projectile')
  destroy(enemyProjectile)
  health = health - 1

# Or with shotgun powerups, which let us use more powerful, 3 rocket
# weapon and also remove the used powerup from the screen.
if collision_check(self, 'obj_shotgun_powerup'):
  shotgun = collision_check(self, 'obj_shotgun_powerup')
  destroy(shotgun)
  # With the following line we enable the use of a shotgun, by switching
  # the value of 'shotgun' to 1. We also get 5 additional rounds
  # for the shotgun!
  shotgun = 1
  ammoCounter = ammoCounter + 5

# HEALTH MANAGEMENT

# We use if-statements yet again to check if our health has dropped
# below 0, in which case we move to game over screen and destroy our
# player.
if health <= 0:
  room_set('rm_game_over')
  destroy(self)

# Here we cap our max health at 5, in order to balance the game out.
# We say that if at any point our health is above 5, we want to drop it
# down to 5.
if health > 5:
  health = 5

# KEY INPUT

# In order to shoot from our spaseship, we attach our 'space' key to
# release a projectile everytime we press it. We do that by building a
# new projectile object.
if key_was_pressed('space'):
  # Here we check if we have the shotgun equipped and if there are enough
  # rounds (more than 0) in it!
  if shotgun == 1 and ammoCounter > 0:
    # Because our shotgun shoots 3 projectiles at once, we create those
    # projectiles in here, and give them all a different name.
    # They also use different classes or blueprints, because some of
    # those projectiles also move in the horizontal direction!
    projectile1 = object_new('obj_projectile')
    projectile2 = object_new('obj_left_shotgun')
    projectile3 = object_new('obj_right_shotgun')

    # Here we make sure to attach all 3 projectiles to the position of
    # our spaceship.
    projectile1.x = self.x
    projectile1.y = self.y
    projectile2.x = self.x
    projectile2.y = self.y
    projectile3.x = self.x
    projectile3.y = self.y

    # Everytime we use the shotgun once (pressing the 'space' key once),
    # we will lose 1 round of our ammo!
    ammoCounter = ammoCounter - 1

  else:
    projectile = object_new('obj_projectile')
    # In order for our projectiles to appear going out from the player,
    # we attach its location to the location of our player. Because we
    # are inside of the player blueprint right now, we can use the word
    # 'self' to describe it.
    projectile.x = self.x
    projectile.y = self.y

# In the same manner as above, if we press the 'S' key on the keyboard,
# we print out and show our current game score.
if key_was_pressed('S'):
  print("Score: " + game.score)

# In the same manner as above, if we press the 'S' key on the keyboard,
# we print out and show our current game score.
if key_was_pressed('I'):
  print("Ammo in Shotgun Left: " + ammoCounter)

# In order for our spaceship to move, we need to attach the four of our
# arrow keys to the different movement directions of our player.
if key_is_pressed('down'):
  # By adding or subtracting from our current position, we are able to
  # to move our spaceship around the screen. In order to change how fast
  # we do that, we can change by how much it moves with each press.
  # Right now it is set to 5 pixels.
  self.y = self.y - 5
if key_is_pressed('right'):
  self.x = self.x + 5
if key_is_pressed('left'):
  self.x = self.x - 5
if key_is_pressed('up'):
  self.y = self.y + 5

# Because our imaginary coordinate system extends beyond the visible
# screen, we need to define the borders within which we can move our
# spaceship. If we were to leave this block of code out, our player
# could disappear beyond the borders, where we will no longer be able
# to see it.
if  self.x > 300:
  self.x = 300
if  self.x < -300:
  self.x = -300
if  self.y > 210:
  self.y = 210
if  self.y < -210:
  self.y = -210
