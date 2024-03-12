from defenition import RUN, STOP, GENERATE, RUN_ONE_STEP, CLEAN, MOUSEBUTTONUP, MOUSEBUTTONDOWN, QUIT, WHITE
from defenition import event, display, sys, NAME
from defenition import Surface
from Classes import Transmission, Button, Table


def processing_event():
    for ev in event.get():
        if ev.type == QUIT:
            close_prog()
        if ev.type == MOUSEBUTTONDOWN:
            Table.last_ev = ev
            for button in Button.list:
                button.press_down()
        if ev.type == MOUSEBUTTONUP:
            for button in Button.list:
                button.press_up()


def processing_own_events():
    # распределение общих событий
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
        Transmission.gl_status = STOP


def upload_file():
    i = 1
    while i <= 100:
        try:
            file = open(f'data{i}.txt', 'x')
            break
        except FileExistsError:
            i += 1
    else:
        print('Не удалось создать файл')
        return
    for table in Table.tables:
        file.write('[\n')
        for string in table.matrix:
            file.write(', '.join([str(elem) for elem in string]))
            file.write('\n')
        file.write(']')
    file.close()
    print('Файл выгружен.\n Для просмотра закройте программу')


def open_file():
    try:
        file = open(NAME, 'r')
    except FileNotFoundError as exc:
        print(exc)
        return
    try:
        mas1 = file.readlines()
        size = len(mas1)
        i = -2
        for line in mas1:
            i += 1
            mas2 = line.split(', ')
            if i == -1 or i == size - 2:
                continue
            j = -1
            for elem in mas2:
                j += 1
                if elem[0] == '0':
                    Table.tables[0].matrix[i][j] = 0
                else:
                    Table.tables[0].matrix[i][j] = 1
    except IndexError as exc:
        print(exc, '\nРазмер открываемого файла превышает размер таблицы')
        return
    print('Файл открыт успешно')


def to_run():
    Transmission.gl_status = RUN


def to_clean():
    Transmission.gl_status = CLEAN
    Transmission.paint_stop = True


def to_generate():
    Transmission.gl_status = GENERATE
    Transmission.paint_stop = True


def to_one_step():
    Transmission.gl_status = RUN_ONE_STEP
    Transmission.paint_stop = True


def to_stop():
    Transmission.gl_status = STOP


def rendering(window, sprites):
    for sprite in sprites:
        sprite.render(window)
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
