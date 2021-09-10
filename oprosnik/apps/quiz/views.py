from rest_framework.response import Response
from rest_framework.views import APIView
from . models import QuizeList


class QuizeListView(APIView):
    def get(self, request):
        aQuizeList = QuizeList.objects.all()
        return Response({"QuizeList": 'ss'})

def index(request):
	return HttpResponse('hello world')

# для админа:
# авторизация в системе
# добавление опроса
# изменение опроса
# удаление опроса
# добавление вопроса в опросе
# изменение вопроса в опросе
# удаление вопроса в опросе

# для клиента
# создание пользователя с уникальным id
# получения списка активных вопросов
# прохождение опроса
# получение пройденных опросов