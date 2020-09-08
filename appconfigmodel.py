
class BatchFileSource:
    def __init__(self, s3client, bucketname, bucketprefix):
        print("Data Source Model")


class ParseFileModel:
    def __init__(self, delimiter: str, linetokenizer: str, skiplines: str, lastrecordprefix: str, comitsize: str, rowmappermodel: str):
        self.delimiter = delimiter
        self.linetokenizer = linetokenizer
        self.skiplines = skiplines
        self.lastrecordprefix = lastrecordprefix
        self.comitsize = comitsize
        self.rowmappermodel = rowmappermodel
