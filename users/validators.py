from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if any(char.isalpha() for char in password) and any(
            char.isdigit() for char in password
        ):
            return
        raise ValidationError(
            "Le mot de passe doit contenir au moins une lettre et un nombre",
            code="password_no_letters",
        )

    def get_help_text(self):
        return "Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule et un nombre."
