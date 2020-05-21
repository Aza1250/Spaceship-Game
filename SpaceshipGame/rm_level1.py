# This is our first room, or you can also think of it as our first level!

# With these lines of code, we create a new Player, based on our object
# script 'obj_player'. You can think of an 'obj_player' as a blueprint.
# In it we define all the features of our player. Here we only 'build'
# that object from the blueprint!
player = object_new('obj_player')

# To actually have our Player on the screen, we need to give him a
# certain position. We say that that we want our player to appear in the
# middle of our screen and set Player's position at the coordinates 0,0.
player.x = 0
player.y = 0

# Here we do the exact same thing as above, except that we create a
# Spawner object from our 'obj_spawner' blueprint! Because we dont
# actually need to see this object, we can set it be outside of our game
# screen, by writing that it's y-coordinate or the vertical position is
# 400.
spawner = object_new('obj_spawner')
spawner.y = 400
