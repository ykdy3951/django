from django import forms
from .models import Board


class WriteForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label='제목'
    )
    contents = forms.CharField(
        error_messages={
            'required': '게시글을 입력해주세요.'
        },
        label='게시글명'
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        contents = cleaned_data.get('contents')

        if not(title and contents):
            if title is None:
                self.add_error('title', '값이 없습니다.')
            if contents is None:
                self.add_error('contents', '값이 없습니다.')
