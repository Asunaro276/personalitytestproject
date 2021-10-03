import base64
import io
import matplotlib.pyplot as plt
import numpy as np
import pickle
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import QuestionnaireForm
from .models import PersonalityModel
from .personality import make_result, normalize


from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError

@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)


class QuestionnaireView(FormView):
    template_name = "questionnaire.html"
    form_class = QuestionnaireForm
    success_url = 'result'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = QuestionnaireForm(request.POST or None)
        if form.is_valid():
            PersonalityModel.objects.create(**form.cleaned_data)
        data = np.array([int(request.POST[f'answer{i+1}']) for i in range(18)]).reshape((1, -1))
        with open('works/factor_analyzer', 'rb') as fa_file:
            fa = pickle.load(fa_file)
        data_point = np.squeeze(fa.transform(data))
        data_point_norm = normalize(data_point.copy())
        make_result(data_point_norm)
        graph = get_image()
        plt.cla()
        if data_point[0] >= 0 and data_point[1] >= 0:
            personality = 'ビジネスマン'
            explanation = 'あなたは論理的に物事を考えるのが上手で、思いついたことをすぐに行動に移せるビジネスマン向きの性格であると言えます。'
            advice = 'このタイプの人は有能である半面、自分では気づかないうちに正論で人を傷つけてしまうことも。少しだけ相手にペースを合わせることを意識してみるとコミュニケーションをより円滑に進められるかもしれません。'
        elif data_point[0] <= 0 and data_point[1] >= 0:
            personality = 'アイドル'
            explanation = 'あなたは他人への共感能力が高くノリもいい、みんなに好かれるアイドルタイプの性格であると言えます。'
            advice = 'このタイプの人はみんなに好かれる一方で、その場のノリを重視しすぎて忘れっぽいという一面も。行動を起こす前に少し立ち止まって考えてみると普段見逃しているものに気づけるようになるかもしれません。'
        elif data_point[0] <= 0 and data_point[1] <= 0:
            personality = 'カウンセラー'
            explanation = 'あなたは他人への共感能力が高く、物事を冷静に判断できるカウンセラー向きの性格であると言えます。'
            advice = 'このタイプは優しく聞き上手な人が多く親しみやすい反面、自分から積極的に話をするのが苦手なこともしばしば。普段から自分の意見をしっかりと持つことを意識すると他人とのコミュニケーションでも臆することなく意見を言えるようになるかもしれません。'
        else:
            personality = '研究者'
            explanation = 'あなたは論理的かつ冷静な分析が得意な研究者タイプの性格であると言えます'
            advice = 'このタイプの人は一人で仕事をすると著しい結果を出す傾向にある反面、他人とのコミュニケーションにおいてはしばしば何を考えているのかわからないと思われてしまいがち。自身の考察を他人に伝えるのも大切ですが、たまには自分の感情も言葉にしてみるとコミュニケーションがよりうまくいくようになるかもしれません。'

        return render(request, 'result.html', {
            'graph': graph, 'personality': personality, 'explanation': explanation, 'advice': advice
        }
                      )


class ResultView(TemplateView):
    template_name = 'result.html'
    form = QuestionnaireForm


def get_image():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


