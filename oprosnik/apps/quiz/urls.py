from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('admin/quiz/add', views.index, name = 'index'),
	path('admin/quiz/edit', views.index, name = 'index'),
	path('admin/quiz/del', views.index, name = 'index'),
	path('admin/quiz/question/add', views.index, name = 'index'),
	path('admin/quiz/question/edit', views.index, name = 'index'),
	path('admin/quiz/question/del', views.index, name = 'index'),

	path('user/get_active_quiz', views.QuizeListView.as_view()),
	path('user/take_quiz', views.index, name = 'index'),
	path('user/get_quiz_result', views.index, name = 'index'),
]