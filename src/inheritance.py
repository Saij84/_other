class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, numScores, lastName, idNum, scores):
        Person.__init__(self, firstName, lastName, idNum)
        self.numScores = numScores
        self.scores = scores

    def calculate(self):
        score = sum(scores)/numScores
        if score < 40:
            return "T"
        elif 40 <= score < 55:
            return "D"
        elif 55 <= score < 70:
            return "P"
        elif 70 <= score < 80:
            return "A"
        elif 80 <= score < 90:
            return "E"
        elif 90 <= score <= 100:
            return "O"

line = "Ritika Trikha 3648762".split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = 6  # not needed for Python
scores = list(map(int, "100 50 70 60 80 60".split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
