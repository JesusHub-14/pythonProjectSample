import json
from datetime import datetime
import pandas

class AccessRequest:
    def __init__(self, idDocument, fullName):
        self.__name = fullName
        self.__idDocument = idDocument
        justnow = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self, value):
        self.__name = value

    @property
    def idDocument(self):
        return self.__idDocument
    @Name.setter
    def idDocument(self,value):
        self.__idDocument = value