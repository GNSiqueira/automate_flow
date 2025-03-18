import os
from app import app

def repositories():
    if os.name == 'nt':  # Windows
        repository = os.path.join(os.getenv('APPDATA'), 'automate_flow')
    else:  # Unix (Linux, macOS)
        repository = os.path.join(os.path.expanduser('~'), '.config', 'automate_flow')
    try:
        repository = 'config'
        if os.path.exists(repository):
            print('existe')
        else:
            os.mkdir(repository)
            os.mkdir(repository + '/image')
            print('agora existe')

        return repository, repository + '/image'

    except ValueError as e:
        print('deu erro: ', e)
        return e, False
def screen_center(larg, alt):
    locate = app.primaryScreen().geometry()
    center_x = (locate.width() - larg) // 2
    center_y = (locate.height() - alt) // 2

    return center_x + locate.x(), center_y + locate.y()
