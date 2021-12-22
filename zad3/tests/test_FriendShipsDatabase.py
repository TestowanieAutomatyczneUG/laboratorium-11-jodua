from unittest import TestCase
from unittest.mock import MagicMock
from assertpy import assert_that
from assertpy.assertpy import assert_warn
from src.FriendShipsDatabase import FriendShipsDatabase


class TestFriendShipsDatabase(TestCase):
    def setUp(self) -> None:
        self.temp_fs_db = FriendShipsDatabase(None, None)
        self.temp_fs_db.database.friendships = {
            "Marek": ["Karol", "Tomasz"],
            "Janek": [],
            "Karol": ["Marek", "Tomasz"],
            "Tomasz": ["Marek", "Karol"]
        }

    def test_add_person(self) -> None:
        # Mock db_insert method
        db_insert = MagicMock()
        # Set return_value for db_insert method
        person = "Wojtek"
        db_insert.return_value = person
        # Create new FriendShipsDatabase object with mocked method
        fs_database = FriendShipsDatabase(db_insert, None)
        # Add person to database
        fs_database.addPerson(person)
        # Check if local database contains person
        assert_that(fs_database.database.friendships).contains("Wojtek")

    def test_add_person_db_insert_called(self) -> None:
        db_insert = MagicMock()
        person = "Wojtek"
        db_insert.return_value = person
        fs_database = FriendShipsDatabase(db_insert, None)
        fs_database.addPerson(person)
        db_insert.assert_called_with("Wojtek")

    def test_add_person_connection_error(self) -> None:
        db_insert = MagicMock()
        person = "Wojtek"
        db_insert.side_effect = ConnectionError
        fs_database = FriendShipsDatabase(db_insert, None)
        assert_that(fs_database.addPerson).raises(
            ConnectionError).when_called_with(person)

    def test_make_friends(self) -> None:
        db_make_friends = MagicMock()
        person1 = "Wojtek"
        person2 = "Marek"
        db_make_friends.return_value = ["Wojtek", "Marek"]
        fs_database = FriendShipsDatabase(None, db_make_friends)
        fs_database.database.friendships = {
            "Wojtek": [],
            "Marek": []
        }
        fs_database.makeFriends(person1, person2)
        assert_that(fs_database.database.friendships.get(
            "Wojtek")).contains("Marek")

    def test_make_friends_mock_called(self) -> None:
        db_make_friends = MagicMock()
        person1 = "Wojtek"
        person2 = "Marek"
        db_make_friends.return_value = ["Wojtek", "Marek"]
        fs_database = FriendShipsDatabase(None, db_make_friends)
        fs_database.database.friendships = {
            "Wojtek": [],
            "Marek": []
        }
        fs_database.makeFriends(person1, person2)
        db_make_friends.assert_called_once()

    def test_make_friends_connection_error(self) -> None:
        db_make_friends = MagicMock()
        person1 = "Wojtek"
        person2 = "Marek"
        db_make_friends.side_effect = ConnectionError
        fs_database = FriendShipsDatabase(None, db_make_friends)
        fs_database.database.friendships = {
            "Wojtek": [],
            "Marek": []
        }
        assert_that(fs_database.makeFriends).raises(
            ConnectionError).when_called_with(person1, person2)

    def test_are_friends(self) -> None:
        assert_that(self.temp_fs_db.areFriends("Marek", "Karol")).is_true()

    def test_are_not_friends(self) -> None:
        assert_that(self.temp_fs_db.areFriends("Marek", "Janek")).is_false()

    def test_get_friends_list(self) -> None:
        friends_lists = self.temp_fs_db.getFriendsList("Marek")
        assert_that(len(friends_lists)).is_equal_to(2)

    def test_get_friends_list_none(self) -> None:
        friends_lists = self.temp_fs_db.getFriendsList("Unknown")
        assert_that(friends_lists).is_none()
