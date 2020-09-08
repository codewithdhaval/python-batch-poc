import importlib
from typing import Any

from fileparser.configmodel import ParseFileModel
from rowmapper.rowmapmodel import RowMapModel


class FileItemReader:
    """
    lineMapper maps line to model
    """
    def __init__(self, configmodel: ParseFileModel):
        self.configmodel = configmodel

    def _doRead(self) -> list:
        """
        return rowmapper model
        :return:
        """
        listofrefineditems = []
        with open("./associatedetails.dat", "r") as freader:
            lines = freader.readlines()
            for line in lines:
                listofrefineditems.append(line)
        return listofrefineditems

