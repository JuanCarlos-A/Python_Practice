print("This code will executed !Always no matter what")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}!"

if __name__ == "__main__":
    print("This code will only be executed when test.py is run directly not when it is being imported")
    person = Person('David')
    print(person.greet())
    print(f'runing test file so __name__  of test file is {__name__}')