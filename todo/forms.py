from django import forms
from todo.models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'description', 'is_completed',"start_date", "end_date"]


class ToDoUpdateForm(ToDoForm):
    pass
