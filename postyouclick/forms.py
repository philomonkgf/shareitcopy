from pyexpat import model
from django import forms
from.models import Newuser,NewImage
from django.contrib.auth.forms import UserCreationForm,UserChangeForm



class Create_New_User(UserCreationForm):
    class Meta:
        model = Newuser
        # fields = '__all__'
        fields = ['email','username','bio','first_name','last_name']
        
      
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['password1'].help_text = 'Your password can’t be too similar to your other personal information *Your password must contain at least 8 characters.'
    #     self.fields['email'].widget.attrs['class'] = "col-sm-12 col-form-label col-form-label-sm"
    #     self.fields['username'].widget.attrs['class'] = "col-sm-12 "
    #     self.fields['phone_number'].widget.attrs['class'] = "col-sm-12 "
    #     self.fields['bio'].widget.attrs['class'] = "col-sm-8 "
    #     self.fields['first_name'].widget.attrs['class'] = "col-sm-12 "
    #     self.fields['last_name'].widget.attrs['class'] = "col-sm-12 "
    #     self.fields['password1'].widget.attrs['class'] = "col-sm-12 "
    #     self.fields['password2'].widget.attrs['class'] = "col-sm-12 "
    #     self.fields['password1'].widget.attrs['style'] = 'font-size: 15px'




        
        
        
        
        
        
        
        
# class New_user_signup(Create_New_User):
       
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
       
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('email', css_class='form-group col-md-6 mb-0'),
#                 Column('username', css_class='form-group col-md-6 mb-0'),
                
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('bio', css_class='form-group col-md-6 mb-0'),
#                 Column('first_name', css_class='form-group col-md-4 mb-0'),
#                 Column('last_name', css_class='form-group col-md-2 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('password1', css_class='form-group col-md-6 mb-0'),
#                 Column('password2', css_class='form-group col-md-4 mb-0'),
#                 Column('phone_number', css_class='form-group col-md-2 mb-0'),
#                 css_class='form-row'
#             ),
            
#             Submit('submit', 'Sign in')
#         )
        
        


class Add_image_post(forms.ModelForm):
    
    class Meta:
        model = NewImage
        fields = ['post','post_image','about_post']
        


class Edit_user(UserChangeForm):
    password = None
    class Meta:
        model = Newuser
        fields = ['email','username','bio','first_name','last_name']
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].disabled = True
        