from datetime import date
from django.db import models
from staff.managers import StaffManager


class Department(models.Model):
    title = models.CharField('название подразделения', max_length=254)
    director = models.ForeignKey('staff.Staff', on_delete=models.SET_NULL,
                               blank=True, null=True, related_name="staff", verbose_name='директор')

    class Meta:
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField('название должности', max_length=50)

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'

    def __str__(self):
        return self.title


class Staff(models.Model):
    lname = models.CharField('фамилия', max_length=50)
    fname = models.CharField('имя', max_length=50)
    sname = models.CharField('отчество', max_length=50, null=True, blank=True)
    salary = models.DecimalField('оклад', max_digits=14, decimal_places=0, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL,
                             blank=True, null=True, verbose_name='должность')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   blank=True, null=True, verbose_name='подразделение')
    photo = models.ImageField('фото', upload_to='staff/images', blank=True)
    birth_date = models.DateField('дата рождения', blank=True, null=True)

    objects = StaffManager()

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
        ordering = ('lname', 'fname', 'sname')

    @property
    def fullname(self):
        if hasattr(self, '_fullname'):
            return self._fullname
        return ''

    def age(self):
        if self.birth_date:
            today = date.today()
            return (
                today.year - self.birth_date.year - (
                    (today.month, today.day)
                    < (self.birth_date.month, self.birth_date.day)
                )
            )
        return None

    def __str__(self):
        return self.fullname

