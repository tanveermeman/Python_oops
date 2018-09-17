class student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def get_number_of_marks(self):
        return len(self.marks)

    def get_total_sum_of_marks(self):
        return sum(self.marks)

    def maximum_marks(self):
        return max(self.marks)

    def minimum_marks(self):
        return min(self.marks)

    def average_marks(self):
        return  self.get_total_sum_of_marks()/self.get_number_of_marks()

    def add_marks(self, marks):
        self.marks.append(marks)

    def remove_marks(self, index):
        del self.marks[index]
student = student ("tanveer", [23, 45, 56, 76])
number = student.get_number_of_marks()
print(f"student [number of marks : {number}]")
print(student.name)

sum_of_marks = student.get_total_sum_of_marks()
print(sum_of_marks)

max = student.maximum_marks()
print(max)

min = student.minimum_marks()
print(min)

average = student.average_marks()
print(average)

student.add_marks(90)

print(student.marks)

student.remove_marks(4)

print(student.marks)