from unittest import TestCase
from assertpy import assert_that
from src.FriendShips import FriendShips


class TestFriendShips(TestCase):
    def setUp(self) -> None:
        self.temp_friendships = FriendShips()
        self.temp_friendships.friendships = {
            "Marek": ["Karol", "Tomasz"],
            "Janek": [],
            "Karol": ["Marek", "Tomasz"],
            "Tomasz": ["Marek", "Karol"]
        }

    def test_add_person(self) -> None:
        self.temp_friendships.addPerson("Maciej")
        assert_that(self.temp_friendships.friendships).contains("Maciej")

    def test_add_person_already_exist(self) -> None:
        assert_that(self.temp_friendships.addPerson).raises(
            ValueError).when_called_with("Janek")

    def test_add_friend(self) -> None:
        self.temp_friendships.addFriend("Marek", "Janek")
        assert_that(self.temp_friendships.friendships.get(
            "Marek")).contains("Janek")

    def test_add_friend_does_not_exist(self) -> None:
        assert_that(self.temp_friendships.addFriend).raises(
            ValueError).when_called_with("test", "Janek")

    def test_add_friend_does_not_exist2(self) -> None:
        assert_that(self.temp_friendships.addFriend).raises(
            ValueError).when_called_with("Janek", "test")

    def test_get_friends_list(self) -> None:
        result = self.temp_friendships.getFriendsList("Marek")
        assert_that(result).is_equal_to(["Karol", "Tomasz"])

    def test_make_friends_one_way(self) -> None:
        self.temp_friendships.makeFriends("Marek", "Janek")
        assert_that(self.temp_friendships.friendships.get(
            "Marek")).contains("Janek")

    def test_make_friends_or_another(self) -> None:
        self.temp_friendships.makeFriends("Marek", "Janek")
        assert_that(self.temp_friendships.friendships.get(
            "Janek")).contains("Marek")

    def test_are_friends_true(self) -> None:
        assert_that(self.temp_friendships.areFriends(
            "Marek", "Karol")).is_true()

    def test_are_friends_false(self) -> None:
        assert_that(self.temp_friendships.areFriends(
            "Marek", "Janek")).is_false()

    def test_are_friends_does_not_exist(self) -> None:
        assert_that(self.temp_friendships.areFriends).raises(
            ValueError).when_called_with("test", "Janek")
