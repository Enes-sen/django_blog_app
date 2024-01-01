from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı",widget=forms.TextInput(attrs={'placeholder':'Kullanıcı Adı'}))
    password = forms.CharField(label="Parola",widget=forms.PasswordInput(attrs={'placeholder':'Parola'}))

class RegiserForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı",widget=forms.TextInput(attrs={'placeholder':'Kullanıcı Adı'}))
    password = forms.CharField(max_length=25,label="Parola",widget=forms.PasswordInput(attrs={'placeholder':'Parola'}))
    confirm = forms.CharField(max_length=25,label="Parola Doğrula",widget=forms.PasswordInput(attrs={'placeholder':'Parola Doğrula'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Paralolar Eşleşmiyor..!")
        
        values = {
            "username": username,
            "password": password,
        }
        return values
        

