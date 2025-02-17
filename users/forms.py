from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        # 自定义使用哪个模型和哪些字段来创建和更新用户
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

        widgets = {
            'password': forms.PasswordInput(),
        }
