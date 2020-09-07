from rowmapper.rowmapmodel import RowMapModel


class BatchFileSource:
    def __init__(self, s3client, bucketname, bucketprefix):
        print("Data Source Model")


class ParseFileModel:
    def __init__(self, delimiter: str, linetokenizer: str, skiplines: str, comitsize: str, rowmapper):
        print("::::::: ParseFile Model :::::::")
        self.delimiter = delimiter
        self.lineokenizer = linetokenizer
        self.skiplines = skiplines
        self.comitsize = comitsize
        self.rowmapper = rowmapper
