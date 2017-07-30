from django import forms


class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField()

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
 
 

