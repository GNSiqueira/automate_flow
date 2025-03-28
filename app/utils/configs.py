import os
import json

class Configs:
    @staticmethod
    def repositoryComputer():
        if os.name == 'nt':  # Windows
            repository = os.path.join(os.getenv('APPDATA'), 'automate_flow')
        else:  # Unix (Linux, macOS)
            repository = os.path.join(os.path.expanduser('~'), '.config', 'automate_flow')

        return repository

    @staticmethod
    def repositories():
        repository = Configs.repositoryComputer()
        try:
            # if not os.path.exists(repository):
            #     os.makedirs(repository, exist_ok=True)
            #     os.makedirs(os.path.join(repository, 'image'), exist_ok=True)
            if os.path.exists(os.path.join('automate_flow', 'streams.json')):
                repository = 'automate_flow'
                return repository

            elif os.path.exists(os.path.join(repository, 'streams.json')):
                return repository

            elif os.path.exists(os.path.join(repository, 'config.json')):
                with open(os.path.join(repository, 'config.json'), 'r') as f:
                    config = json.load(f)

                if os.path.exists(config[0]):
                    return os.path.join(config[0], 'automate_flow')

            else:
                return False

        except Exception as e:
            print('Erro ao criar repositório:', e)
            return None

    @staticmethod
    def repositoriesImage():
        repo = Configs.repositories()
        return os.path.join(repo, 'image') if repo else None

    @staticmethod
    def existRepository():
        return os.path.exists(Configs.repositories())

    @staticmethod
    def existRepositoryImage():
        return os.path.exists(Configs.repositoriesImage())

    @staticmethod
    def screenshot():
        count = 0
        repository_image = Configs.repositoriesImage()

        if repository_image is None:
            print("Erro: Caminho do repositório é inválido")
            return None, None

        while os.path.exists(os.path.join(repository_image, f"screenshot{count}.png")):
            count += 1

        return repository_image, count

    @staticmethod
    def arquivo_escrita(arquivo):
        with open(os.path.join(Configs.repositories(), 'streams.json'), 'w') as f:
            json.dump(arquivo, f, indent=2)
        return True

    @staticmethod
    def arquivo_leitura() -> list:
        with open(os.path.join(Configs.repositories(), 'streams.json'), 'r') as f:
            config = json.load(f)
        return config

    @staticmethod
    def computador():
        repository = Configs.repositoryComputer()
        os.makedirs(repository, exist_ok=True)
        os.makedirs(os.path.join(repository, 'image'), exist_ok=True)
        with open(os.path.join(repository, 'streams.json'), 'w') as f:
            json.dump([], f, indent=2)

    @staticmethod
    def local():
        repository = 'automate_flow'
        os.makedirs(repository, exist_ok=True)
        os.makedirs(os.path.join(repository, 'image'), exist_ok=True)
        with open(os.path.join(repository, 'streams.json'), 'w') as f:
            json.dump([], f, indent=2)

    @staticmethod
    def diferente(path):
        repository = Configs.repositoryComputer()
        os.makedirs(repository, exist_ok=True)
        with open(os.path.join(repository, 'config.json'), 'w') as f:
            json.dump([path], f, indent=2)

        repository = os.path.join(path, 'automate_flow')
        os.makedirs(repository, exist_ok=True)
        os.makedirs(os.path.join(repository, 'image'), exist_ok=True)
        with open(os.path.join(repository, 'streams.json'), 'w') as f:
            json.dump([], f, indent=2)

    @staticmethod
    def existente(path):
        repository = Configs.repositoryComputer()
        os.makedirs(repository, exist_ok=True)
        with open(os.path.join(repository, 'config.json'), 'w') as f:
            json.dump([path], f, indent=2)

