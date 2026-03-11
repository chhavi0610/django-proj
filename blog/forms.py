from django import forms
from .models import Post

class PostForm(forms.ModelForm):

   class Meta:
      
      model = Post
      fields = ["title", "content"]

   def validate_title(self):

        title = self.cleaned_data.get("title")

        if len(title) < 6:
            raise forms.ValidationError("Title must be at least 6 characters")

        return title
