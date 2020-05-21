# By adding this line of code in the 'loop' section, we say that the
# created projectile will move upwards at a certain speed (currently: 4).
# In order to create a shotgun projectile, we need to spread the projectile
# in the x-direction as well. That's why we change the value of the
# projectile's x coordinate
self.y = self.y + 4
self.x = self.x + 2

# Because our imaginary coordinate system extends beyond our visible screen,
# our computer will actually keep track of all of those projectiles forever.
# To avoid computer lag, we destroy the projectiles that have long
#left our visible screen.
if self.y > 600:
  destroy(self)
