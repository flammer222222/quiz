from django.db import models
from datetime import datetime

# models.Model
class Quiz(models.Model):
	quiz_title = models.CharField('название опроса', max_length = 200)
	quiz_description = models.CharField('описание опроса', max_length = 400)
	quiz_start = models.DateField('дата старта опроса')
	quiz_end = models.DateField('дата окончания опроса')
	def __str__(self):
		 return self.quiz_title

class Question(models.Model):
	quiz_title = models.ForeignKey(Quiz, on_delete = models.CASCADE, related_name='+')
	question_text = models.TextField('текст вопроса')
	possible_answer = models.TextField('возможные варианты ответа')
	question_type = models.IntegerField('тип вопроса')
	def __str__(self):
		 return self.question_text

class User(models.Model):
	user_id = models.IntegerField('ID пользователя') # для идентификации пользователя
	quiz_title = models.ForeignKey(Quiz, on_delete = models.CASCADE, related_name='+')
	question_text = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='+')
	answer = models.TextField('ответ на вопрос')
	def __str__(self):
		 return str(self.user_id)

# entry.authors.add(john, paul, george, ringo)