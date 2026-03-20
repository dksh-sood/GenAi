from typing import TypedDict

class Person(TypedDict):
  name : str
  age : str

new_person: Person = {'name':'daksh','age':'21'}
print(new_person)