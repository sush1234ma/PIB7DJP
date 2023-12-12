from django import forms     # 9.1         # 9. creating the forms in app level using python file

     # by creating the forms insering the data to the structure of the table created in modes
# class studentform(forms.Form):   # 9.2
#     student_id = forms.IntegerField()   # create the same feild  as in model
#     student_name = forms.CharField()
#     course = forms.CharField()
#     jdate = forms.DateField()

# creating a form using models
from django.forms import ModelForm                 # 10
from Hello.models import students                              # 10.1

class studentform(ModelForm):                                  # 10.2
    class Meta:
        model = students    # students is the  class name that created in models
        # fields = 'all'   (or)  we can import all the fields or else we can use all
        fields = ['student_id','student_name', 'course', 'jdate']
        labels = {'student_id': 'id', 'student_name':'name','course': 'course', 'jdate': 'joining date'}

# creating the form to add
form = studentform()                                  # class name of the forms


