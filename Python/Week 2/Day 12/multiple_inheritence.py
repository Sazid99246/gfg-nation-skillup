# User function Template for python3
# Implement Student, Faculty and PhdStudent classes here
class Student:
    def __init__(self, sid, deptid):
        self.sid = sid
        self.deptid = deptid

    def get_info(self):
        return f"StudentID:{self.sid} DepartmentID:{self.deptid}"


class Faculty:
    def __init__(self, eid, deptid):
        self.eid = eid
        self.deptid = deptid

    def get_info(self):
        return f"EmployeeID:{self.eid} DepartmentID:{self.deptid}"


class PhDStudent(Student, Faculty):
    def __init__(self, sid, eid, deptid):
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)

    def get_info(self):
        return f"StudentID:{self.sid} EmployeeID:{self.eid} DepartmentID:{self.deptid}"


s = Student(101, 42)
print(s.get_info())
f = Faculty(555, 42)
print(f.get_info())
p = PhDStudent(101, 555, 42)
print(p.get_info())
