from django import forms


class RegisterAndLoginForm(forms.Form):
    email = forms.EmailField(label="Почта:")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль:")


class NewProfileForm(forms.Form):
    name = forms.CharField(label="Имя")
    surname = forms.CharField(label="Фамилия")
    father = forms.CharField(label="Отчество")
    gender = forms.TypedChoiceField(widget=forms.RadioSelect, choices=((1, "Мужской"), (2, "Женский")), label="Пол",
                                    initial=1)
    ages = forms.DateField(label="Дата рождения", widget=forms.SelectDateWidget)
    message_places = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                               choices=((1, "Telegram"), (2, "VK"), (3, "Email")),
                                               label="Места оповещения")
