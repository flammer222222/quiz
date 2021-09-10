from django.db import models

# models.Model
class QuizeList(models.Model):
	quiz_title = models.CharField('название опроса', max_length = 200)
	quiz_description = models.CharField('описание опроса', max_length = 200)
	quiz_start = models.DateTimeField('дата старта опроса')
	quiz_end = models.DateTimeField('дата окончания опроса')

class Question(models.Model):
	quiz = models.ForeignKey(QuizeList, on_delete = models.CASCADE)
	question_text = models.TextField('текст вопроса')
	possible_answer = models.TextField('возможные варианты ответа')
	question_type = models.IntegerField('тип вопроса')

class Quiz(models.Model):
	quiz_title = models.ForeignKey(QuizeList, on_delete = models.CASCADE, related_name='+')
	question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='+')


class User(models.Model):
	user_ID = models.IntegerField('ID пользователя') # для идентификации пользователя
	quiz_ID = models.ForeignKey(QuizeList, on_delete = models.CASCADE, related_name='+')
	question_ID = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='+')
	answer = models.IntegerField('ответ на вопрос')

