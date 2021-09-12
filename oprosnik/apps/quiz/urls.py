from django.urls import path

from . import views

urlpatterns = [
	path('admin/quiz/add', views.QuizeAdmin.AddQuiz.as_view()),
	path('admin/quiz/del', views.QuizeAdmin.DelQuiz.as_view()),
	path('admin/quiz/question/add',  views.QuizeAdmin.AddQuestion.as_view()),
	path('admin/quiz/question/del', views.QuizeAdmin.DelQuestion.as_view()),

	path('user/get_active_quiz', views.QuizeUser.GetActiveQuiz.as_view()),
	path('user/take_quiz', views.QuizeUser.TakeQuizQuestions.as_view()),
	path('user/get_quiz_result', views.QuizeUser.GetQuizQuestions.as_view()),
]