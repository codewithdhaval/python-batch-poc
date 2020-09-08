import yaml
from appconfigmodel import ParseFileModel


class AppConfigParser:
    """
    Parses the appconfig file
    create a model that stores all the information about parsing the file
    """
    def __init__(self, configfile_relativepath: str):
        self.configfile_relativepath = configfile_relativepath

    def _parseappconfig(self) -> ParseFileModel:
        with open(self.configfile_relativepath) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            #print(data)
            for items in data: # list from yaml
                for filereaderkey in items: #dictionary/map from list items
                    if filereaderkey == "filereader":
                        print(f"{filereaderkey} -> {items[filereaderkey]}")
                        for key in items[filereaderkey]:
                            if key == "delimiter":
                                print(f"Delimiter :: {items[filereaderkey][key]}")
                                delimiter = items[filereaderkey][key]
                            if key == "linetokenizer":
                                print(f"lineTokenizer :: {items[filereaderkey][key]}")
                                linetokenizer = items[filereaderkey][key]
                            if key == "skiplines":
                                print(f"SkipLines ::{items[filereaderkey][key]}")
                                skiplines = items[filereaderkey][key]
                            if key == "lastrecordprefix":
                                print(f"SkipLines ::{items[filereaderkey][key]}")
                                lastrecordprefix = items[filereaderkey][key]
                            if key == "comitsize":
                                print(f"comitsize ::{items[filereaderkey][key]}")
                                comitsize = items[filereaderkey][key]
                            if key == "rowmappermodel":
                                print(f"rowmappermodel ::{items[filereaderkey][key]}")
                                rowmappermodel = items[filereaderkey][key]

                        fileparsemodel = ParseFileModel(delimiter, linetokenizer, skiplines, lastrecordprefix, comitsize, rowmappermodel)
        return fileparsemodel