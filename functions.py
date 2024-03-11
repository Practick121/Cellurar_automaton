from defenition import RUN, STOP, GENERATE, RUN_ONE_STEP, CLEAN, MOUSEBUTTONUP, MOUSEBUTTONDOWN, QUIT, WHITE
from defenition import event, mouse, display, sys
from defenition import Surface
import defenition
from Classes import Transmission, Button, Table


def processing_event():
    for ev in event.get():
        if ev.type == QUIT:
            close_prog()
        if ev.type == MOUSEBUTTONDOWN:
            for button in Button.list:
                button.press_down()
        if ev.type == MOUSEBUTTONUP:
            for button in Button.list:
                button.press_up()


def processing_mouse_events():
    if mouse.get_pressed():
        pass


def processing_own_events():
    if Transmission.gl_status == RUN and Transmission.delay_timer.is_out():
        Table.status = RUN
        Transmission.delay_timer.wind_up()
    elif Transmission.gl_status == RUN_ONE_STEP:
        Table.status = RUN
        Transmission.gl_status = STOP
    elif Transmission.gl_status == GENERATE:
        Table.status = GENERATE
        Transmission.gl_status = STOP
    elif Transmission.gl_status == STOP:
        Table.status = STOP
    elif Transmission.gl_status == CLEAN:
        Table.status = CLEAN


def upload_file():
    i = 1
    while i <= 100:
        try:
            file = open(f'data{i}', 'x')
            break
        except FileExistsError:
            i += 1
    else:
        print('Не удалось создать файл')
        return
    for table in Table.tables:
        file.write('[')
        for string in table.matrix:
            file.write(', '.join([str(elem) for elem in string]))
            file.write('\n')
        file.write(']')
    file.close()


def open_file():
    try:
        file = open('data', 'r')
    except FileExistsError:
        print('Не удалось открыть файл')
        return
    file.read()
    file.split('\n')
    for i in range(len(Table.tables[0])):
        for j in range(len(Table.tables[0])):
            Table.tables[0].matrix[i][j] = file[i][j]


def to_run():
    Transmission.gl_status = RUN


def to_clean():
    Transmission.gl_status = CLEAN
    Transmission.paintstop = True


def to_generate():
    Transmission.gl_status = GENERATE
    Transmission.paintstop = True


def to_one_step():
    Transmission.gl_status = RUN_ONE_STEP
    Transmission.paintstop = True


def to_stop():
    Transmission.gl_status = STOP


def rendering(window, sprites):
    for sprite in sprites:
        sprite.render(window)
    display.flip()


def first_rendering(window, sprites):
    rendering(window, sprites)
    display.flip()


def close_prog():
    sys.exit()


def to_maze():
    Transmission.Birth = [3]
    Transmission.Survive = [1, 2, 3, 4, 5]


def to_caves():
    Transmission.Birth = [5, 6, 7, 8]
    Transmission.Survive = [4, 5, 6, 7, 8]


def to_live():
    Transmission.Birth = [3]
    Transmission.Survive = [2, 3]


def create_icon():
    icon = Surface((99, 99))
    icon.fill(WHITE)
    icon.blit(Surface((33, 33)), (33, 0))
    icon.blit(Surface((33, 33)), (66, 33))
    icon.blit(Surface((33, 33)), (0, 66))
    icon.blit(Surface((33, 33)), (33, 66))
    icon.blit(Surface((33, 33)), (66, 66))
    return icon
