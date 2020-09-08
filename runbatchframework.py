import importlib

from fileparser import configmodel
from fileparser.fileparser import FileConfigParser
from rowmapper.rowmapmodel import RowMapModel


class RunBatchFramework:
    """
    Parses the config file and creates batch environment
    """
    def __init__(self):
        self.configmodel = None

    def createconfigmodel(self) -> configmodel:
        parser = FileConfigParser("./appflow.yaml")
        self.configmodel = parser._parseconfigfile()

    '''
        def readfile(self) -> None:
        filepath = self.inputfilepath
        print("Parse input file ::"+filepath)
    '''

    def transform(self, line: str) -> None:
        tokens = line.split("|")
        module_ = importlib.import_module("rowmapper.rowmapmodel")
        class_ = getattr(module_, self.configmodel.rowmappermodel)(tokens)
        return class_

    def process(self) -> None:
        print("call DAO")

    def persistdata(self) -> None:
        print("call DAO")


if __name__ == "__main__":
    runbatch = RunBatchFramework()
    runbatch.createconfigmodel()
    with open("./associatedetails.dat", "r") as freader:
        line = freader.readline()
        while line != "":
            linemapper = runbatch.transform(line)
            print(f"{linemapper.name} - {linemapper.addr} - {linemapper.salary}")
            line = freader.readline()
