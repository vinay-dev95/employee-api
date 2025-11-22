from pydantic import BaseModel


class Employee(BaseModel):
    empID: int
    empName: str
    empFname: str
    empRole: str
    empBG: str