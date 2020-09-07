class FileItemReader:
    """
    lineMapper maps line to model
    """
    def __init__(self, linestoskip: str, lineMapper: str, arrayoflinestoskip: str):
        self.linestoskip = linestoskip
        self.arrayoflinestoskip = arrayoflinestoskip

    def doRead(self) -> None:
        """
        return rowmapper model
        :return:
        """
        # line = readline()
        # line is header or footer or comment, skip it
        print("Read the file- line by line")

    def mapline(self):
        print("map the line to rowmapper")
        # new rowmapper object and pass the delimited token in sequence
