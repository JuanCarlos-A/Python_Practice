import test

print(f'runing file main and importing test file so __name__  of test file is {test.__name__}')
person = test.Person("Juan")
greeting = person.greet()
print(greeting)