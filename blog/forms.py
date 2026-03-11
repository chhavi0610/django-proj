from django import forms
from .models import Post

class PostForm(forms.ModelForm):

   class Meta:
      
      model = Post
      fields = ["title", "content"]

   def validate_title(self):

        title = self.cleaned_data.get("title")

        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters")

        return title
