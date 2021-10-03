from django.urls import path

from .views import QuestionnaireView, ResultView, my_customized_server_error


urlpatterns = [
    path('', QuestionnaireView.as_view(), name='questionnaire'),
    path('result/', ResultView.as_view(), name='result'),
]

handler500 = my_customized_server_error
