from appconfigmodel import ParseFileModel


class FileItemReader:
    """
    Reads records from the file
    Applies filters and conditions from appconfig
    """
    def __init__(self, configmodel: ParseFileModel):
        self.configmodel = configmodel
        self.lineskiptrack = 0

    def _doRead(self) -> list:
        listofrefineditems = []
        with open("./batchfile.dat", "r") as freader:
            lines = freader.readlines()
            for line in lines:
                if self.skiplines(self.configmodel.skiplines):
                    continue
                if self.islastrecord(self.configmodel.lastrecordprefix, line):
                    return listofrefineditems
                listofrefineditems.append(line)
        return listofrefineditems

    def skiplines(self, linestoskip: int) -> bool:
        if linestoskip == self.lineskiptrack:
            return False
        self.lineskiptrack += 1
        return True

    def islastrecord(self, recordprefix: str, line: str):
        if line.startswith(recordprefix):
            return True
        return False