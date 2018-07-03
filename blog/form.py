from django import  forms



######form表单基础，使用POST方法的表单例子###########

class AddForm(forms.Form):
    first = forms.IntegerField()
    second = forms.IntegerField()




class RegisterForm(forms.Form):
    username = forms.CharField(max_length=8,min_length=6)
    password = forms.CharField(max_length=8,min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder':'请输入密码'}),
                        error_messages={'min_length':'密码长度小于6',
                                        'max_length':'密码长度超过8了'})
    password_repeat = forms.CharField(max_length=8,#min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder':'请再输入密码'}),
                    error_messages = {'min_length': '密码长度小于6'}
                                      )
    email = forms.EmailField()


class LoginForm(forms.Form):
    username111 = forms.CharField(label='用户名',max_length=20,
                               error_messages={'max_length':'不能超过20个字符',})
    password = forms.CharField(label='密码',max_length=20,min_length=6,
    	widget = forms.PasswordInput(attrs={'placeholder': u'请输入密码 '}))

