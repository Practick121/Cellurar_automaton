
from defenition import *
from functions import *
from Classes import *

# инициализация

pygame_init()
font.init()
global_display = display.set_mode(GLOBAL_SIZE, FLAGS)
display.set_caption(TITLE)
display.set_icon(create_icon())
global_display.set_alpha(None)
clock_fps = time.Clock()
clock_ips = time.Clock()
is_running = 1
Transmission.Birth = Birth.copy()
Transmission.Survive = Survive.copy()

table = Table()
start_stop = []
mode = []
button_start = ActiveButton((100, 25), (850, 10), RED, 'RUN', BLACK, to_run, mas=start_stop)
button_stop = ActiveButton((100, 25), (850, 60), RED, 'STOP', BLACK, to_stop, mas=start_stop)
button_one_step = Button((100, 25), (850, 110), RED, 'RUN ONE STEP', BLACK, to_one_step)
button_clean = Button((100, 25), (850, 160), RED, 'CLEAN', BLACK, to_clean)
button_generate = Button((100, 25), (850, 210), RED, 'GENERATE', BLACK, to_generate)
button_maze = ActiveButton((100, 25), (850, 260), RED, 'maze', BLACK, to_maze, mas=mode)
button_caves = ActiveButton((100, 25), (850, 310), RED, 'caves', BLACK, to_caves, mas=mode)
button_live = ActiveButton((100, 25), (850, 360), RED, 'live', BLACK, to_live, mas=mode)

button_stop.get_active()
sprites = [table, button_maze, button_caves, button_start, button_stop, button_one_step, button_clean, button_generate,
           button_live]
# спрайты расположены в порядке рендеринга
display.flip()