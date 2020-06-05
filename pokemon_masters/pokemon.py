
import time
import os


from pok_functions import config
from pok_functions import turn
from pok_functions import game_over
from pok_functions import intro



intro()
trainer_one, trainer_two = config()
time.sleep(.5)
turn(trainer_one, trainer_two)
game_over()