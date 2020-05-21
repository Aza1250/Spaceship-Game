# Because we want for our game to be fun, we want to randomize where
# our shields, asteroids and enemies spawn. In order to do that, we have
# to use a different set of utilities that are not normally included.
# We use the word 'import' to bring over the utilites necessary to make
# our game more random.
import random

# In order to time our spawns, we continuously increase the timers of
# our objects. We do this to spawn our objects at certain intervals,
# each interval being specific to that object.
asteroidTimer = asteroidTimer + 1
shieldTimer = shieldTimer + 1
enemyTimer = enemyTimer + 1
shotgunTimer = shotgunTimer + 1

# Once the timers for our objects reach their specific values (60 for
# asteroids, 240 for shields and 300 for enemies), we create those objects.
if asteroidTimer == 60:
  # We use the 'random.randint' function to get a random number within the
  # range of numbers (in our case that's between -200 and 200).
  asteroidOffset = random.randint(-200, 200)
  asteroid = object_new('obj_asteroid')
  # Once we get that random number, we add it to the default spawn positions
  # of our objects to build them in always different places on the screen!
  asteroid.x = self.x + asteroidOffset
  asteroid.y = self.y + asteroidOffset
  asteroidTimer = 0

# We proceed to do the exact same thing for all of our different objects!
if shieldTimer == 240:
  shieldOffset = random.randint(-200, 200)
  shield = object_new('obj_shield')
  shield.x = self.x + shieldOffset
  shield.y = self.y + shieldOffset
  shieldTimer = 0

# We do the exact same thing to our shotgun powerups as well!
if shotgunTimer == 240:
  shotgunOffset = random.randint(-200, 200)
  shotgun = object_new('obj_shotgun_powerup')
