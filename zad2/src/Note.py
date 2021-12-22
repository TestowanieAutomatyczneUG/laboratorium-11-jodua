class Note:
    def __init__(self, name: str, note: float) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        # isinstance nie przepuści NoneType object
        # if name is None:
        #     raise ValueError("Provide a name")
        if name == "":
            raise ValueError("Name is empty")
        if not isinstance(note, float):
            raise TypeError("Note must be float")
        if note < 2 or note > 6:
            raise ValueError("Number must be in range <2,6>")
        self._name = name
        self._note = note

    @property
    def name(self):
        return self._name

    @property
    def note(self):
        return self._note
