people = []


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def appendPerson(self):
        people.append([self.name, self.age])


people_to_create = int(input("how many people do you want to add? "))

for i in range(people_to_create):
    while True:
        name = input("\nwhat is the name of person #" + str(i + 1) + "? ")
        age = int(input("what is the age of person #" + str(i + 1) + "? "))
        person = Person(name, age)

        print("just to confirm, the person's name is", name,
              "and their age is", age)
        option = input("is this correct? (y/n) ")

        if option == "y":
            person.appendPerson()
            break

print(people)
