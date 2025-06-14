from django.test import TestCase
from django.urls import reverse
from .models import Person

class PersonFormTests(TestCase):

    def test_person_form_get(self):
        response = self.client.get(reverse('person_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    def test_person_form_post_valid(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
        }
        response = self.client.post(reverse('person_create'), data)
        # After POST, it redirects to success
        self.assertRedirects(response, reverse('success'))
        # Check the person was created in DB
        self.assertEqual(Person.objects.count(), 1)
        person = Person.objects.first()
        self.assertEqual(person.first_name, 'John')
        self.assertEqual(person.last_name, 'Doe')

    def test_person_form_post_invalid(self):
        data = {
            'first_name': '',  # missing required field
            'last_name': 'Doe',
        }
        response = self.client.post(reverse('person_create'), data)
        self.assertEqual(response.status_code, 200)

        # 🧠 Manually extract the form from the response context
        form = response.context['form']

        # ✅ Check the form is invalid
        self.assertFalse(form.is_valid())

        # ✅ Ensure the error is related to 'first_name'
        self.assertIn('first_name', form.errors)
        self.assertEqual(form.errors['first_name'], ['This field is required.'])

        # ✅ Ensure nothing was saved in the DB
        self.assertEqual(Person.objects.count(), 0)
