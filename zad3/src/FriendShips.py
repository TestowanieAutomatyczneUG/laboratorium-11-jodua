from typing import Optional


class FriendShips:
    def __init__(self) -> None:
        self.friendships = {}

    def addPerson(self, person: str) -> None:
        if self.friendships.get(person) is not None:
            raise ValueError("Person already exist")
        self.friendships[person] = []

    def makeFriends(self, person1: str, person2: str) -> None:
        if not self.areFriends(person1, person2):
            self.addFriend(person1, person2)
            self.addFriend(person2, person1)

    def getFriendsList(self, person: str) -> Optional[list]:
        return self.friendships.get(person)

    def areFriends(self, person1: str, person2: str) -> bool:
        friends = self.friendships.get(person1)
        if friends is None:
            raise ValueError("Person1 does not exist")
        if person2 in friends:
            return True
        return False

    def addFriend(self, person: str, friend: str) -> None:
        if self.friendships.get(person) is None:
            raise ValueError("Person does not exist")
        if self.friendships.get(friend) is None:
            raise ValueError("Friend does not exist")
        self.friendships.get(person).append(friend)
