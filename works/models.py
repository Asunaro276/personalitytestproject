from django.db import models


class PersonalityModel(models.Model):
    class Meta:
        db_table = "personality"

    answer1 = models.IntegerField(verbose_name='answer1', blank=True)
    answer2 = models.IntegerField(verbose_name='answer2', blank=True)
    answer3 = models.IntegerField(verbose_name='answer3', blank=True)
    answer4 = models.IntegerField(verbose_name='answer4', blank=True)
    answer5 = models.IntegerField(verbose_name='answer5', blank=True)
    answer6 = models.IntegerField(verbose_name='answer6', blank=True)
    answer7 = models.IntegerField(verbose_name='answer7', blank=True)
    answer8 = models.IntegerField(verbose_name='answer8', blank=True)
    answer9 = models.IntegerField(verbose_name='answer9', blank=True)
    answer10 = models.IntegerField(verbose_name='answer10', blank=True)
    answer11 = models.IntegerField(verbose_name='answer11', blank=True)
    answer12 = models.IntegerField(verbose_name='answer12', blank=True)
    answer13 = models.IntegerField(verbose_name='answer13', blank=True)
    answer14 = models.IntegerField(verbose_name='answer14', blank=True)
    answer15 = models.IntegerField(verbose_name='answer15', blank=True)
    answer16 = models.IntegerField(verbose_name='answer16', blank=True)
    answer17 = models.IntegerField(verbose_name='answer17', blank=True)
    answer18 = models.IntegerField(verbose_name='answer18', blank=True)
