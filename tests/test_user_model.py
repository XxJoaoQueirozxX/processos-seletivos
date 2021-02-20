import unittest
from app import create_app, db
from app.models import User
from time import sleep


class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(password='teste')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='teste')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='teste')
        self.assertTrue(u.confirm_password('teste'))
        self.assertFalse(u.confirm_password('teste2'))

    def test_password_salts_are_random(self):
        u = User(password='teste')
        u2 = User(password='teste')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_account_confirmation_token(self):
        u = User(email="teste@gmail.com", password="teste")
        u.save()
        self.assertFalse(u.confirmed)
        token = u.generate_confirmation_token()
        self.assertTrue(u.confirm(token))
        self.assertTrue(u.confirmed)
        u.delete()

    def test_confirmation_token_expires(self):
        u = User(email="teste@gmail.com", password="teste")
        u.save()
        self.assertFalse(u.confirmed)
        token = u.generate_confirmation_token(1)
        sleep(2)
        self.assertFalse(u.confirm(token))
        self.assertFalse(u.confirmed)
