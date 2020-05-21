# In most of our objects, we need to give them an image to actually see
# them on our game screen. We can do that by using 'sprites'. A sprite is
# simply an image that we use for our objects!
sprite = sprite_new('spr_player')

# We also set the 'parameters' of our objects. A parameter is simply a
# characteristic of our objects! In the case of our Player blueprint, we
# want to make sure that our Player always has 5 health when it's created.
# We use the following code to create a new variable that does that!
health = 5

# And here we also create the ammo counter variable to keep track of how
# many shotgun uses we have left! Because we dont have a shotgun yet when
# we start the game, the value of the counter is equal to 0.
ammoCounter = 0

# A variable is exactly what it's name suggests! It is simply a
# characteristic of our objects that we can change!
