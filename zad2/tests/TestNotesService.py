from unittest import TestCase
from unittest.mock import MagicMock, patch
from assertpy import assert_that
from src.Note import Note
from src.NotesService import NotesService
from src.NotesStorage import NotesStorage


class TestNotesService(TestCase):
    def setUp(self) -> None:
        self.ns = NotesService()

    def test_add_note_is_instance(self) -> None:
        note = Note("Note1", 3.5)
        with patch.object(NotesStorage, 'add', MagicMock(return_value=note)) as mock_ns_add:
            assert_that(self.ns.add(note)).is_instance_of(Note)

    def test_add_note_is_equal_object(self) -> None:
        note = Note("Note1", 2.5)
        with patch.object(NotesStorage, 'add', MagicMock(return_value=note)) as mock_ns_add:
            assert_that(self.ns.add(note)).is_equal_to(note)

    def test_clear_notes(self) -> None:
        with patch.object(NotesStorage, 'clear', MagicMock(return_value=True)) as mock_ns_clear:
            assert_that(self.ns.clear()).is_true()

    def test_average_of(self) -> None:
        with patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[
                Note("sth", 3.0), Note("sth", 4.0), Note("sth", 2.0)])) as mock_ns_getAllNotesOf:
            assert_that(self.ns.averageOf('sth')).is_equal_to(3.0)

    def test_clear_average_of_empty(self) -> None:
        with patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[])) as mock_ns_getAllNotesOf:
            assert_that(self.ns.averageOf('sth')).is_equal_to(0)
