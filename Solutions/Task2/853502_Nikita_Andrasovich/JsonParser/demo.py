import parser
import unittest
import tests


class Job:
    def __init__(self, company="", position=""):
        self.company_name = company
        self.position = position


class Person:
    def __init__(self, name="", age=0, job=None, kids=None):
        self.name = name
        self.age = age
        self._calculateIsOld_()

        self.job = job
        self.kids = kids

    def _calculateIsOld_(self):
        if self.age > 60:
            self.isOld = True
        else:
            self.isOld = False

    def greet(self):
        if self.isOld:
            print("Hello, old fella")
        else:
            print("Greetings")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(tests.tests_suite())
    return suite


if __name__ == '__main__':
    tests_result = unittest.TextTestRunner(verbosity=0).run(suite())

    if not tests_result.wasSuccessful():
        exit(1)

    kevin_the_kid = Person("Kevin", 13, None, None)

    duck_hunter = Job("CuackDuck Co.", "Hunter")
    oliver_the_teen = Person("Oliver", 19.5, duck_hunter, None)

    sony_programmer = Job("Sony", "Programmer")
    johny_the_daddy = Person("John", 45, sony_programmer, [
        kevin_the_kid, oliver_the_teen])

    json = parser.to_json(johny_the_daddy)
    print("Json:\n"+json, end="\n\n")

    restored_johny = parser.from_json(json, globals())
    print("Is Johny old: " + str(restored_johny.isOld), end="\n")
    print("How many kids does Johny have: " +
          str(len(restored_johny.kids)), end="\n")
    print("Where does Johny work: at " +
          restored_johny.job.company_name, end="\n\n")

    raw_collection_json = parser.to_json([False, True])
    print("Json:\n"+raw_collection_json, end="\n\n")
    print("Collection: " + str(parser.from_json(raw_collection_json, globals)))
