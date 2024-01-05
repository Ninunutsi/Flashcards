from django.forms import ModelForm
from .models import FlashCard
from django import forms
from django.contrib.auth.models import User


class FlashCardForm(ModelForm):
	class Meta:
		model = FlashCard
		fields = ['category', 'front_native', 'back_translation', 'native_language', 'creator', 'known']
