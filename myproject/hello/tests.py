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
        self.assertRedirects(response, reverse('success'))
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
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertEqual(form.errors['first_name'], ['This field is required.'])
        self.assertEqual(Person.objects.count(), 0)
    def this(self):
        data = {
            'first_name': '',  # missing required field
            'last_name': 'Doe',
        }
        response = self.client.post(reverse('person_create'), data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertEqual(form.errors['first_name'], ['This field is required.'])
        self.assertEqual(Person.objects.count(), 0)
        

 
