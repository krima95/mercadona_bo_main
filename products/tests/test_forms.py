import pytest
from django.contrib.auth.models import User
from products.forms import CreateUserForm


@pytest.mark.django_db
def test_create_user_form_valid_data():
    # Créez un dictionnaire de données valides pour le formulaire
    data = {
        "username": "testuser",
        "password1": "password123!",
        "password2": "password123!",
    }
    form = CreateUserForm(data=data)

    # Vérifiez que le formulaire est valide
    assert form.is_valid()

    # Enregistrez l'utilisateur dans la base de données
    form.save()

    # Vérifiez que l'utilisateur a été créé
    assert User.objects.filter(username="testuser").exists()


@pytest.mark.django_db
def test_create_user_form_invalid_data():
    # Créez un dictionnaire de données invalides pour le formulaire
    data = {
        "username": "testuser",
        "password1": "password123!",
        "password2": "differentpassword",
    }
    form = CreateUserForm(data=data)

    # Vérifiez que le formulaire n'est pas valide
    assert not form.is_valid()

    # Assurez-vous qu'aucun utilisateur n'a été créé
    assert not User.objects.filter(username="testuser").exists()
