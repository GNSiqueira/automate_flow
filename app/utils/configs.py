import os

class Configs:
    @staticmethod
    def __repositories():
        if os.name == 'nt':  # Windows
            repository = os.path.join(os.getenv('APPDATA'), 'automate_flow')
        else:  # Unix (Linux, macOS)
            repository = os.path.join(os.path.expanduser('~'), '.config', 'automate_flow')

        repository = 'config'

        try:
            if not os.path.exists(repository):
                os.makedirs(repository)
                os.makedirs(os.path.join(repository, 'image'))

            return repository
        except Exception as e:
            print('Erro:', e)
            return None

    @staticmethod
    def __repositoriesImage():
        repo = Configs.__repositories()
        return os.path.join(repo, 'image') if repo else None

    @staticmethod
    def existRepository():
        return os.path.exists(Configs.__repositories())

    @staticmethod
    def existRepositoryImage():
        return os.path.exists(Configs.__repositoriesImage())

    @staticmethod
    def screenshot():
        count = 0
        repository_image = Configs.__repositoriesImage()

        if repository_image is None:
            print("Erro: Caminho do repositório é inválido")
            return None, None

        while os.path.exists(os.path.join(repository_image, f"screenshot{count}.png")):
            count += 1

        return repository_image, count
