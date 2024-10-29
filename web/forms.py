from django import forms


class ContactFormModelForm(forms.Form):
    customer_email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Ingrese su correo"}
        ),
        error_messages={
            "invalid": "Por favor, introduce una dirección de correo válida."
        },
    )
    customer_name = forms.CharField(
        max_length=64,
        label="Nombre",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ingrese su nombre"}
        ),
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Escriba su mensaje aquí",
                "rows": 4,
            }
        ),
    )
