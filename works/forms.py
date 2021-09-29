from django import forms

CHOICE = [
    ('5', '非常に当てはまる'),
    ('4', '当てはまる'),
    ('3', 'どちらともいえない'),
    ('2', '当てはまらない'),
    ('1', 'まったく当てはまらない'),
]


class QuestionnaireForm(forms.Form):
    answer1 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer2 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer3 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer4 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer5 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer6 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer7 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer8 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer9 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer10 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer11 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer12 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer13 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer14 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer15 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer16 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer17 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)

    answer18 = forms.ChoiceField(
        label='answer',
        widget=forms.RadioSelect,
        choices=CHOICE,
        required=True)
