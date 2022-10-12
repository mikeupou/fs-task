from django.db import models


# did not implement a User model based on requirements
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} subscribed at {self.subscribed_at}'
