from django import forms
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name':'Enter First name',
            'last_name':'Enter last name',
            'email':'Enter email',
            'option':'Newsletter option'
        }
        help_texts = {
            'first_name':'Enter characters only'
        }

        error_messages = {
            'first_name':{
                'required':'You cannot move forward without first name'
            },
            'email':{
                'unique':'Email already exists in our subscription list'
            }
        }