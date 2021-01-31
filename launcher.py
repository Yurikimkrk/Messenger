import subprocess
from general.variables import TERMINALS_TO_LAUNCH
from time import sleep

PROCESS = []

while True:
    print('Выберите действие: ')
    ANSWER = input('q - выход, s - запустить сервер и клиенты, х - закрыть все окна: ')

    if ANSWER == 'q':
        break
    elif ANSWER == 's':
        PROCESS.append(subprocess.Popen('python server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        sleep(5)
        for terminal in TERMINALS_TO_LAUNCH:
            PROCESS.append(subprocess.Popen(f'python client.py -n {terminal} -p 11111',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ANSWER == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
