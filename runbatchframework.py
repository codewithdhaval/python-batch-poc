import importlib

from fileparser import configmodel
from fileparser.fileparser import FileConfigParser
from filereader.flatfilereader import FileItemReader
from transform.filetransform import FileTransformer


class RunBatchFramework:
    """
    Parses the config file and creates batch environment
    """
    def __init__(self):
        self.configmodel = None

    def createconfigmodel(self) -> configmodel:
        parser = FileConfigParser("./appflow.yaml")
        self.configmodel = parser._parseconfigfile()

    def readfile(self) -> list:
        fileiteamreader = FileItemReader(self.configmodel)
        return fileiteamreader._doRead()

    def transform(self, listofitems: list) -> list:
        transformresults = FileTransformer(self.configmodel)
        return transformresults._transform(listofitems)

    def process(self) -> None:
        print("call DAO")

    def persistdata(self) -> None:
        print("call DAO")


if __name__ == "__main__":
    runbatch = RunBatchFramework()
    runbatch.createconfigmodel()
    listofitems = runbatch.readfile()
    listoffiltereditems = runbatch.transform(listofitems)
