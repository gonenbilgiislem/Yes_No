from django.db import models

class Support(models.Model):

    PERSON = (
        ('', 'Choose person type'),
        ('Customer', 'Customer'),
        ('Employee', 'Employee'),
    )
    SUBJECT = (
        ('', 'Choose a subject'),
        ('System errors', 'System errors'),
        ('How to do that', 'How to do that'),
        ('Extremely urgent', 'Extremely urgent'),
        ('Suggestions or claims', 'Suggestions or claims'),
    )

    name=models.CharField(max_length=100)
    subject = models.CharField(max_length=50, choices=SUBJECT)
    person = models.CharField(max_length=50, choices=PERSON)
    problem = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name