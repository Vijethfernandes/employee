from django import forms
from emp_app.models import add_emp

class Add_emp(forms.ModelForm):
    class Meta:
        model=add_emp
        fields=['name','dog','subject','phone','description']