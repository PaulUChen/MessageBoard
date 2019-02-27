# -*- coding: utf-8 -*-

from django import forms
from .models import BoardMessage
from django.core.exceptions import ValidationError

class BoardForm(forms.Form):
    title = forms.CharField(max_length=20, initial='')
    content = forms.CharField(widget=forms.Textarea)
    #author = forms.CharField(max_length=20,initial='')
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 20:
            raise forms.ValidationError('字數不足20')
        return content

    class Meta:
        model = BoardMessage
        fields = ['title', 'content',]

