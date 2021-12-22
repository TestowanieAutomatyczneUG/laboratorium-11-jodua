from typing import Optional
from src.FriendShips import FriendShips


class FriendShipsDatabase:
    def __init__(self, db_insert, db_make_friends) -> None:
        self.database = FriendShips()
        self.db_insert = db_insert
        self.db_make_friends = db_make_friends

    def addPerson(self, person1: str) -> None:
        try:
            from_database = self.db_insert(person1)
        except ConnectionError:
            raise
        if from_database:
            return self.database.addPerson(from_database)

    def makeFriends(self, person1: str, person2: str) -> None:
        try:
            from_database = self.db_make_friends(person1, person2)
        except ConnectionError:
            raise
        if from_database:
            return self.database.makeFriends(from_database[0], from_database[1])

    def getFriendsList(self, person: str) -> Optional[list]:
        return self.database.getFriendsList(person)

    def areFriends(self, person1: str, person2: str) -> bool:
        return self.database.areFriends(person1, person2)
