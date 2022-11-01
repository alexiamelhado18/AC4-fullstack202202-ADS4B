import json

pessoas = [];

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def checkNameInSystem(name):
    if filter(lambda c: c[0] == name, pessoas):
        return f"{name} consta em nosso registro!";
    else:
        return f"{name} não conta em nosso sistema!";

  def registrationOfPeople():
    return json.dumps(pessoas, default=lambda x: x.__dict__)

person1 = Person("Alexia", 21);
person2 = Person("Adelmir", 23)
person3 = Person("Julia", 25);

pessoas.append(person1);
pessoas.append(person2);
pessoas.append(person3);