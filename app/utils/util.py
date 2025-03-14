import os

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