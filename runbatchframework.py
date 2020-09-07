from fileparser.fileparser import FileConfigParser


class RunBatchFramework:
    """
    Parses the config file and creates batch environment
    """
    def __init__(self, inputfilepath: str):
        self.inputfilepath = inputfilepath

    def parseinputfile(self) -> None:
        filepath = self.inputfilepath
        print("Parse input file ::"+filepath)

    def processfile(self) -> None:
        print("call processor + transform")

    def persistdata(self) -> None:
        print("call DAO")


if __name__ == "__main__":
    #runbatch = RunBatchFramework("./appflow.yaml")
    parser = FileConfigParser("./appflow.yaml")
    configmodel = parser._parseconfigfile()
