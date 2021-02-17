class Person(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return '%s %s' % (self.name, self.surname)
    
    def printname(self):
        print(self)
    
    
class Student(Person):
    def __init__(self, name, surname, topic):
        super(Student, self).__init__(name, surname)
        self.topic = topic
        
    def __str__(self):
        return '%s %s, %s' % (self.name, self.surname, self.topic)
    
    def printname(self):
        print(self)
        

class Teacher(Person):
    def __init__(self, name, surname, course):
        super(Teacher, self).__init__(name, surname)
        self.course = course
        
    def __str__(self):
        return '%s %s teaches %s' % (self.name, self.surname, self.course)
    
    def printname(self):
        print(self)