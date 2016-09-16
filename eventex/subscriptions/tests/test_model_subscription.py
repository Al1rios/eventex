from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ali Rios',
            cpf='12345678901',
            email='ali.rios@gmail.com',
            phone='21-971906677'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        '''Subscription must have an auto created_at atrr.'''
        self.assertIsInstance(self.obj.created_at, datetime)
