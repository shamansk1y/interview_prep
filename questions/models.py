from ckeditor.fields import RichTextField
from django.db import models

class Question(models.Model):
    question_text_en = models.CharField(max_length=250)
    question_text_ru = models.CharField(max_length=250)
    answer_text_en = RichTextField()
    answer_text_ru = RichTextField()
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')
    class Meta:
        verbose_name = 'Question'

    def __str__(self):
        return f'{self.id} - {self.question_text_en}'