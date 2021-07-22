from django.db import models

# Create your models here.
class Task(models.Model):
    #fields of database
    title = models.CharField('Навзвание', max_length=50)
    task = models.TextField('описание')

    def __str__(self):
        return self.title


    class Meta:

        """
                этот класс просто меняет название нашей задичи(название класса(Task))

        """
        verbose_name = 'Задача'
        verbose_name_plural = 'задачи'








