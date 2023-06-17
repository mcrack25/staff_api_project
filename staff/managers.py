from django.db import models
from django.db.models import Value as V
from django.db.models.functions import Concat


class StaffManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
                _fullname=Concat('lname', V(' '), 'fname', V(' '), 'sname')
            )
