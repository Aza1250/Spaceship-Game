# By adding this line of code in the 'loop' section, we say that any
# created asteroid will move downwards at a certain speed (currently: 1).
self.y = self.y - 1

# Here we check if our asteroid (indicated by the 'self', because we are
# now inside of a asteroid blueprint) collides with a player's projectile.
# Once that happens, we destroy both the one specific projectile and
# asteroid that came in contact with each other. We do that for a normal
# projectile, as well as shotgun specific projectiles as you can see below.
if collision_check(self, 'obj_projectile'):
  projectile = collision_check(self, 'obj_projectile')
  destroy(projectile)
  # We also need to make sure to not forget to add points to our score,
  # for each destroyed asteroid (currently 1 point).
  game.score = game.score + 1
  destroy(self)

if collision_check(self, 'obj_left_shotgun'):
  projectile = collision_check(self, 'obj_left_shotgun')
  destroy(projectile)
  game.score = game.score + 1
  destroy(self)

if collision_check(self, 'obj_right_shotgun'):
  projectile = collision_check(self, 'obj_right_shotgun')
  destroy(projectile)
  game.score = game.score + 1
  destroy(self)

# For the same reason as our projectiles that are long off our visible
# screen, we remove any passed asteroids as well.
if self.y < -400:
  destroy(self)
