import importlib
from fileparser.configmodel import ParseFileModel

module_ = importlib.import_module("rowmapper.rowmapmodel")


class FileTransformer:
    def __init__(self, configmodel: ParseFileModel):
        self.configmodel = configmodel

    def _transform(self, listofitems: list) -> list:
        listoffilteredtems = []
        for item in listofitems:
            tokens = item.split(self.configmodel.delimiter) # create a method and do data check
            class_ = getattr(module_, self.configmodel.rowmappermodel)(tokens)
            listoffilteredtems.append(class_)
        return listoffilteredtems