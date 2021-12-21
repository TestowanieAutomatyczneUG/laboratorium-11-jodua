from src.Note import Note
from src.NotesStorage import NotesStorage


class NotesService:
    def __init__(self) -> None:
        self._notes_storage = NotesStorage()

    def add(self, note: Note) -> Note:
        return self._notes_storage.add(note)

    def averageOf(self, name: str) -> float:
        notes_of_name = self._notes_storage.getAllNotesOf(name)
        if notes_of_name:
            return sum(note.note for note in notes_of_name)/len(notes_of_name)
        return 0

    def clear(self) -> bool:
        # return True if cleared
        return self._notes_storage.clear()
