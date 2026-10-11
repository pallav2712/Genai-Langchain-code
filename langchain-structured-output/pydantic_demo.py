from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    name: str = "Pallav"
    age: int | None = None
    email: EmailStr
    cgpa: float = Field(
        gt=0,
        lt=10,
        default=5,
        description="A decimal value representing the cgpa of the student",
    )


new_student = {"age": '32', "email": "abc@gmail.com"}
# this will still work pydantic will convert age to str on its own and its called 
# type coercion

# ek type se dusri type mai convert karna = type casting
#Type casting mein hum actual value ka data type convert karte hain.

# Type hinting mein hum batate hain ki variable ya function se kis type 
# ki value expect ki ja rahi hai.



student = Student(**new_student)

print(type(student))

print(student)

student_dict = student.model_dump()


print(student_dict["age"])

student_json = student.model_dump_json()

print(student_dict)
print(student_json)
