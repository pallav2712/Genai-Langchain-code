from typing import TypedDict


class Person(TypedDict): #type dict just define the type of dict element not like #pydantic which raise runtime error if type of element is not followed.
    name: str
    age: int


new_person: Person = {"name": "nitish", "age": "35"}

print(new_person)
