from django import forms

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
"""
class MultipleSelect(forms.Forms):
	task_selected = forms.CheckboxField()
"""
class TaskRemove(forms.Form):
	title = forms.CharField(label="Title",max_length=100,widget=forms.TextInput(attrs={'required':'true'}))

class TaskUpdateDeadline(forms.Form):
	title = forms.CharField(label="Title",max_length=100,widget=forms.TextInput(attrs={'required':'true'}))
	complete_by = forms.DateTimeField(label="Complete By",input_formats=['%d %b %Y'],widget=forms.DateTimeInput(attrs={'id':"datetimepicker"}))

class TaskUpdateStatus(forms.Form):
	title = forms.CharField(label="Title",max_length=100,widget=forms.TextInput(attrs={'required':'true'}))
	status= forms.ChoiceField(choices=STATUS_CHOICES)
