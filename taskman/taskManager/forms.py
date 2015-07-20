from django import forms
from models import Task

STATUS_CHOICES = (("INCOMPLETE","incomplete"),
					("COMPLETE","complete"),)

class TaskCreate(forms.Form):
	title = forms.CharField(label="Title",max_length=100,widget=forms.TextInput(
							attrs={'required':'true',
							'class':'form-control'}))
	details = forms.CharField(label="Details",widget=forms.Textarea(
							attrs={'cols':'80',
							'required':'false',
							'class':'form-control'}))
	complete_by = forms.DateTimeField(label="Complete By",input_formats=['%d %b %Y'],
							widget=forms.DateTimeInput(
								attrs={'id':"datetimepicker",
								'class':'form-control'}))

class MultipleSelect(forms.Form):
	task_selected = forms.ModelMultipleChoiceField(
        queryset = Task.objects.all(),
        widget  = forms.CheckboxSelectMultiple
    )

class TaskRemove(forms.Form):
	title = forms.CharField(label="Title",max_length=100,widget=forms.TextInput(attrs={'required':'true'}))

class TaskUpdateDeadline(forms.Form):
	title = forms.CharField(label="Title",max_length=100,widget=forms.TextInput(attrs={'required':'true'}))
	complete_by = forms.DateTimeField(label="Complete By",input_formats=['%d %b %Y'],widget=forms.DateTimeInput(attrs={'id':"datetimepicker"}))
