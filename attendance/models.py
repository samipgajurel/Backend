from django.db import models
from accounts.models import User

class Attendance(models.Model):
    intern = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    date = models.DateField()
    present = models.BooleanField(default=True)
    marked_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='attendance_marked'
    )

    class Meta:
        unique_together = ('intern', 'date')

    def __str__(self):
        return f"{self.intern.username} - {self.date}"
