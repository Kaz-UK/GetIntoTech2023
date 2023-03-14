# super class
class Person:

    def __init__(self, person_surname, person_forenames, person_address, person_dob, person_ni, person_id):
        self._surname = person_surname
        self._forenames = person_forenames
        self._address = person_address
        self._dob = person_dob
        self._ni = person_ni
        self._id = person_id

    # Returns person's name
    def get_name(self):
        print(f"{self._forenames} {self._surname}")
        return f"{self._forenames} {self._surname}"

    # Change person name
    def set_name(self, new_name_surname, new_name_forenames):
        self._surname = new_name_surname
        self._forenames = new_name_forenames

    # Get person address
    def get_address(self):
        print(self._address)

    # Change person address
    def set_address(self, new_address):
        self._address = new_address

    def get_dob(self):
        print(self._dob)

    def get_ni(self):
        print(self._ni)
