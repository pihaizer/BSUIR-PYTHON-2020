from singleton import SingletonTemplate
from collections import defaultdict
import unittest
import tests


class UserPreferencesDatabase(metaclass=SingletonTemplate):
    prefs = defaultdict(list)

    def add_preference(self, user: str, *preferences: str):
        self.prefs[user] += preferences

    def get_user_preferences(self, user: str):
        return self.prefs.get(user, list())


def save_preferences():
    prefsDB = UserPreferencesDatabase()

    print("Saving George's preferences")
    prefsDB.add_preference("George", "Pork", "Green vegies", "Cream deserts")

    print("Saving Leon's preferences", end="\n\n")
    prefsDB.add_preference("Leon", "Sea food", "Small portions")


def print_preferences():
    prefsDB = UserPreferencesDatabase()

    print("George loves", end=" ")
    print(", ".join(prefsDB.get_user_preferences("George")).lower())

    print("Leon loves", end=" ")
    print(", ".join(prefsDB.get_user_preferences("Leon")).lower())


def suite():
    suite = unittest.TestSuite()
    suite.addTest(tests.tests_suite())
    return suite


if __name__ == '__main__':
    tests_result = unittest.TextTestRunner(verbosity=0).run(suite())

    if not tests_result.wasSuccessful():
        exit(1)

    save_preferences()
    print_preferences()
