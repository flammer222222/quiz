from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from . models import Quiz, User
from . serializers import QuizSerializer, QuestionResult,  QuestionSerializer

# для клиента
class QuizeUser(APIView):

	# получения списка активных опросов 
	class GetActiveQuiz(APIView):
		def get(self, request):
			quizList = Quiz.objects.all()
			serializer = QuizSerializer(quizList, many=True)
			return Response({"QuizList": serializer.data})

	# получение пройденных опросов 
	class GetQuizResult(APIView):
		def get(self, request):
			quizList = User.objects.filter(user_id=1).order_by('quiz_title')	
			serializer = QuestionResult(quizList, many=True)
			return Response({"QuizList": serializer.data})

# для админа:
class QuizeAdmin(APIView):

	# добавление опроса
	class AddQuiz(APIView):
		def post(self, request):
			quiz = request.data.get('quiz')
			token = request.data.get('token')
			if token == 'admin':
				serializer = QuizSerializer(data=quiz)
				if serializer.is_valid(raise_exception=True):
					quiz_saved = serializer.save()
				return Response({"success": "Quiz '{}' created successfully".format(quiz_saved.quiz_title)})
			return Response({"fail": "incorrect token"})

	# изменение опроса
	class EditQuiz(APIView):
		def put(self, request):
			quiz = request.data.get('quiz')
			token = request.data.get('token')
			if token == 'admin':
				serializer = QuizSerializer(data=quiz)
				if serializer.is_valid(raise_exception=True):
					Quiz.objects.filter(id=4).update(serializer)
					# quiz_saved = serializer.update()
				return Response({"success": "Quiz '{}' created successfully".format(quiz_saved.quiz_title)})
			return Response({"fail": "incorrect token"})

	# удаление опроса
	class DelQuiz(APIView):
		def delete(self, request):
			quizList = Quiz.objects.all()
			serializer = QuizSerializer(quizList, many=True)
			return Response({"QuizList": serializer.data})

	# добавление вопроса в опросе
	class AddQuestion(APIView):
		def post(self, request):
			question = request.data.get('question')
			token = request.data.get('token')
			if token == 'admin':
				serializer = QuestionSerializer(data=question)
				if serializer.is_valid(raise_exception=True):
					question_saved = serializer.save()
				return Response({"success": "question '{}' created successfully".format(question_saved.question_text)})
			return Response({"fail": "incorrect token"})		


def index():
	return Response()

# авторизация в системе

# изменение опроса


# изменение вопроса в опросе
# удаление вопроса в опросе

# для клиента
# создание пользователя с уникальным id

# прохождение опроса
