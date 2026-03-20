from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
  name:str = 'daksh'
  age : Optional[int] = None
  email : EmailStr
  cgpa : float = Field(gt=0, lt=10, default=7, description='A decimal value representing the cgpa of the student')


new_student = {'age' : '21','email':'abc@gmail.com'} ## if we pass age as a str still it give int due to coercing

student = Student(**new_student)

student_dict = dict(student)

print(student)

student_json = student.model_dump_json()
