from rest_framework import serializers

from . models import Quiz, User, Question

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('quiz_title', 'question_text', 'possible_answer', 'question_type')


class UserQuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('user_id', 'quiz_title', 'question_text', 'answer')
