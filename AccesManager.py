import json
from .AccessManagementException import AccessManagementException
from .AccessRequest import AccessRequest

class AccessManager:
    def __init__(self):
        pass

    def validatedni(self, dni):
        if len(self.dni) > 1 and len(self.dni) < 10:
            dni_letter = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
                          'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K',
                          'E')

            id_card = ""
            letter = ""

            for i in self.dni:
                for j in dni_letter:
                    if i == j:
                        letter += i

            for i in self.dni:
                if i != letter:
                    id_card += i

            i = int(id_card) % 23
            letter = dni_letter[i]

            if letter == (self.dni[-1]):
                return True

        return False


    def ReadaccessrequestfromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise AccessManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise AccessManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            idDoc = DATA["id"]
            name = DATA["name"]
            req = AccessRequest(idDoc, name)
        except KeyError as e:
            raise AccessManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateDNI(idDoc):
            raise AccessManagementException("Invalid DNI")

        # Close the file
        return req