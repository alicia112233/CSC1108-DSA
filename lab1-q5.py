class Student:
    def __init__(self, name, studentNumber):
        self.name = name
        self.studentNumber = studentNumber
        self.score = []
        
    def addScore(self, subjectCode, examScore):
        self.score.append([subjectCode, examScore])

    def getBestExamScore(self):
        if (len(self.score) == 0):
            return None
        
        bestScore = self.score[0][1]
        bestScoreIndex = 0

        for i in range(1, len(self.score)):
            if self.score[i][1] > bestScore:
                bestScore = self.score[i][1]
                bestScoreIndex = i
        return self.score[bestScoreIndex]

    def getFailedModules(self):
        failedModules = []
        for i in range(0, len(self.score)):
            if self.score[i][1] < 40:
                failedModules.append(self.score[i][0])
        return failedModules
    
    def printScores(self):
        output = self.name + " {"

        for i in range(0, len(self.score)):
            if i is not len(self.score) - 1:
                output += "Subject: %s, Score: %d, " %(self.score[i][0], self.score[i][1])
            else:
                output += "Subject: %s, Score: %d" %(self.score[i][0], self.score[i][1])
        
        output += " }"
        return output
    
name = input("Enter student name: ")
studentNumber = input("Enter student number: ")
student = Student(name, studentNumber)

for i in range(5):
    subjectCode = input("Enter subject code: ")
    examScore = int(input("Enter exam score: "))
    student.addScore(subjectCode, examScore)

print("\n" + student.name, student.studentNumber)
print("Best exam score: ", student.getBestExamScore())
print("Failed modules: ", student.getFailedModules())
print("Subject Scores: ", student.printScores())
