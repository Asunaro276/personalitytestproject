from django.urls import path

from .views import QuestionnaireView, ResultView


urlpatterns = [
    path('', QuestionnaireView.as_view(), name='questionnaire'),
    path('result/', ResultView.as_view(), name='result'),
]
