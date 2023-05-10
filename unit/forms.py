from django import forms
from .models import LOS, CRPT, DispAck

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control'}))

class DispAckForm(forms.ModelForm):
    class Meta:
        model = DispAck
        fields = [
            'rec_office',
            'ref',
            'user',
        ]
        widgets = {
            'rec_office' : forms.TextInput(attrs={"class":'form-control form-control-sm', "placeholder":'Recipient offices', 'name': 'offices'}),
            'ref' : forms.TextInput(attrs={'class':'form-control form-control-sm', "placeholder":'Reference No', 'name':'ref'}),
           
        }

class LOSForm(forms.ModelForm):
    class Meta:
        model = LOS
        fields = [ 
            'serial',
            'ref',
            # 'originator',
            'sender',
            'receiver_unit',
            # 'main_receiver',
        #   'file',
            'date_of_rec',
            'time_of_rec',
            'action_taken_by',
       ]
        widgets = {
            'serial': forms.NumberInput(attrs={"class":'form-control form-control-sm', "placeholder":'Serial', 'name': 'serial'}),
            'ref' : forms.TextInput(attrs={'class':'form-control form-control-sm', "placeholder":'Reference No', 'name':'ref'}),
            # 'originator' : forms.TextInput(attrs={'class':'form-control form-control-sm', "placeholder":'Originator', 'name':'originator'}),
            'receiver_unit' : forms.SelectMultiple(attrs={'class': 'form-control form-control-sm', 'name':'receiver_unit'}),
            # 'main_receiver' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder':'Receiving Sections', 'name':'main_receiver'}),
        #   'file' : forms.FileInput(attrs={'class':'form-control form-control-sm', 'name':'file'}),
            'date_of_rec': forms.DateInput(attrs={'class':"form-control form-control-sm",'type':'date', 'name':'date_of_rec'}),
            'time_of_rec': forms.TimeInput(attrs={'class':"form-control form-control-sm",'type':'time', 'name':'time_of_rec'}),
            'action_taken_by' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'name':'action_taken_by'})
        }

class CRPTForm(forms.ModelForm):
    class Meta:
        model = CRPT
        fields = [ 
            'serial',
            'ref',
            # 'originator',
            'sender',
            'receiver_unit',
            # 'main_receiver',
        #   'file',
            'date_of_rec',
            'time_of_rec',
            'group',
            'security_grade',
            'action_taken_by',
       ]
        widgets = {
            'serial': forms.NumberInput(attrs={"class":'form-control form-control-sm', "placeholder":'Serial', 'name': 'serial'}),
            'ref' : forms.TextInput(attrs={'class':'form-control form-control-sm', "placeholder":'Reference No', 'name':'ref'}),
            # 'originator' : forms.TextInput(attrs={'class':'form-control form-control-sm', "placeholder":'Originator', 'name':'originator'}),
            'receiver_unit' : forms.SelectMultiple(attrs={'class': 'form-control form-control-sm', 'name':'receiver_unit'}),
            # 'main_receiver' : forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder':'Receiving Sections', 'name':'main_receiver'}),
        #   'file' : forms.FileInput(attrs={'class':'form-control form-control-sm', 'name':'file'}),
            'date_of_rec': forms.DateInput(attrs={'class':"form-control form-control-sm",'type':'date', 'name':'date_of_rec'}),
            'time_of_rec': forms.TimeInput(attrs={'class':"form-control form-control-sm",'type':'time', 'name':'time_of_rec'}),
            'group' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'name':'group'}),
            'security_grade':forms.TextInput(attrs={'class':'form-control form-control-sm', 'name':'security_grade'}),
            'action_taken_by' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'name':'action_taken_by'})
        }
