# print
print "hello world"

# classes
class Person(object):
    def __init__(self, name, company):
        self.name = name
        self.company = company
        
    def say_hello(self):
        return "Hello, my name is {0} and I work at {1}".format(self.name, self.company)