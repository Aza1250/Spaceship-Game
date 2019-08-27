# By adding this line of code in the 'loop' section, we say that any
# created projectile will move upwards at a certain speed (currently: 4).
self.y = self.y + 4

# Because our imaginary coordinate system extends beyond our visible screen,
# our computer will actually keep track of all of those projectiles forever.
# To avoid computer lag, we destroy the projectiles that have long
#left our visible screen.
if self.y > 600:
  destroy(self)
