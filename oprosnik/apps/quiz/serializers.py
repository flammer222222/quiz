from rest_framework import serializers

from . models import Quiz, User, Question

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = "__all__"

class QuizEditSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields = ("quiz_title", "quiz_description", "quiz_end")

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('quiz_title', 'question_text', 'possible_answer', 'question_type')

# class QuestionResult(serializers.ModelSerializer):
# 	question_text = serializers.StringRelatedField()
# 	class Meta:
# 		model = User
# 		fields = ('question_text', 'answer')

class GetQuizQuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('question_text', 'possible_answer', 'question_type')
