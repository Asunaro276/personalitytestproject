from django.db import models


class PersonalityModel(models.Model):
    class Meta:
        db_table = "personality"

    answer = models.IntegerField(verbose_name='answer', blank=True)
