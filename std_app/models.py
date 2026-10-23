from django.db import models

# Create your models here
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number = models.IntegerField()
    fees=models.DecimalField(max_digits=10, decimal_places=2)
    course=models.CharField(max_length=50)
    sem=models.IntegerField()
    doj=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Student: {self.name}, Email: {self.email}, Roll Number: {self.roll_number}, Fees: {self.fees}, Course: {self.course}, Semester: {self.sem}, Date of Joining: {self.doj}"