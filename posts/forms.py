from django import forms
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from posts.models import Post, Tag

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class PostEditForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class PostCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=AutocompleteSelectMultiple(
            Post._meta.get_field('tags'),
            admin.AdminSite()
        )
    )

    class Meta:
        model = Post
        fields = ["title", "content", "is_ready", "tags"]



class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # phone = forms.CharField(validators=[phone_regex])
    phone = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if len(data) != 9:
            raise ValidationError("Phone Is too short")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data