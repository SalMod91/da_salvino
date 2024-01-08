from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomStaffUser
from .models import Ingredient
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm as AuthPasswordChangeForm
from django.utils.translation import gettext_lazy as _

class StaffUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomStaffUser
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(StaffUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'register_username_id'})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomStaffUser.objects.filter(username=username).exists():
            raise ValidationError("This username is already in use.")
        return username

        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get("password1")
            password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords don't match.")

class CustomPasswordChangeForm(AuthPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].error_messages = {'required': ''}


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'category', 'description', 'image']
    
    
    def clean_image(self):
        """
        This method ensures that if no new image was uploaded in the form, the existing 
        image is maintained. It raises a Validation Error if the uploaded file type is 
        not an Image type.
        
        - If an image is found and it's not of an image file type, it raises a 
          Validation Error.
        - If no new image is uploaded, it retains the existing image (if any). 
          If there's no existing image, it defaults to None.
        """
        image = self.cleaned_data.get('image', False)
        
        if image and hasattr(image, 'content_type'):
            if not image.content_type.startswith('image'):
                raise forms.ValidationError('File type is not supported')
            return image

        # Retain the existing image if no new image is uploaded
        return self.instance.image if self.instance and hasattr(self.instance, 'image') else None
