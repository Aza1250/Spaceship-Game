# With this line of code we say that each enemy will be moving down,
# towards the player at a specific speed (currently: 1).
self.y = self.y - 1

# In order to continuously increase our timer by 1, we place it inside
# of the loop tab.
timer = timer + 1
# Once the timer has reached 120, we build a new enemy projectile, making
# the enemy shoot at our player.
if timer == 120:
  enemyProjectile = object_new('obj_enemy_projectile')
  # The same way we attached our player's projectile to the player's
  # position, we do the same with the enemy projectile.
  enemyProjectile.x = self.x
  enemyProjectile.y = self.y
  # We reset the timer to be equal to 0, in order to make sure that the
  # enemy keeps shooting at us. Otherwise the enemy would shoot only once,
  # and the timer would keep rising infinitely, passing our requirement
  # to shoot every time it reaches 120.
  timer = 0

# We continuously check if our player's projectile has ever hit the enemy.
# If that ever happens and they collide, we remove 1 health from the enemy.
# Besides checking for normal projectiles collisions, we also check for
# the left and right shotgun projectiles below.
if collision_check(self, 'obj_projectile'):
  projectile = collision_check(self, 'obj_projectile')
  destroy(projectile)
  health = health - 1

if collision_check(self, 'obj_left_shotgun'):
  projectile = collision_check(self, 'obj_left_shotgun')
  destroy(projectile)
  health = health - 1

if collision_check(self, 'obj_right_shotgun'):
  projectile = collision_check(self, 'obj_right_shotgun')
  destroy(projectile)
  health = health - 1
  
