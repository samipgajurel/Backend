from django.db import models
from accounts.models import User

class Feedback(models.Model):
    intern = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedback_received'
    )
    supervisor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedback_given'
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.intern.username}"
