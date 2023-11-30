class User:
    firstname: str
    lastname: str
    age: int

    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

