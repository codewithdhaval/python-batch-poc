import appconfigmodel
from fileparser.fileparser import AppConfigParser
from filereader.flatfilereader import FileItemReader
from transform.filetransform import FileTransformer


class RunBatchFramework:
    """
    Maintains and manages flow of entire batch framework
    """
    def __init__(self):
        self.configmodel = None

    def createconfigmodel(self) -> appconfigmodel:
        """
        Parses the appconfig file
        """
        self.configmodel = AppConfigParser("./appconfig.yaml")._parseappconfig()

    def readfile(self) -> list:
        """
        Reads line records from the file
        """
        fileiteamreader = FileItemReader(self.configmodel)
        return fileiteamreader._doRead()

    def transform(self, listofitems: list) -> list:
        """
        Transforms records
        """
        transformresults = FileTransformer(self.configmodel)
        return transformresults._transform(listofitems)

    def process(self, listoftransformeditems: list) -> list:
        print("Logical changes on items from file")

    def persistdata(self) -> None:
        print("call DAO")


if __name__ == "__main__":
    runbatch = RunBatchFramework()
    runbatch.createconfigmodel()
    listofitems = runbatch.readfile()
    listoffiltereditems = runbatch.transform(listofitems)
    for item in listoffiltereditems:
        print(f"Name -{item.name}, City - {item.city}, Salary - {item.salary}")