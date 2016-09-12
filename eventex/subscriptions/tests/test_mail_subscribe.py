from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Ali Rios', cpf='12345678901',
                    email='ali.rios@gmail.com', phone='21-97190-6677')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de incrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br','ali.rios@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Ali Rios',
            '12345678901',
            'ali.rios@gmail.com',
            '21-97190-6677',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
