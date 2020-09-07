import yaml


class FileConfigParser:
    def __init__(self, configfile_relativepath: str):
        self.configfile_relativepath = configfile_relativepath

    def _parseconfigfile(self):
        with open(self.configfile_relativepath) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print(data)
