
import os

from django.test import TestCase
from django.db import models, connection

from j2p_field.models import TestingModel


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "j2p_django_field.settings")


class J2PEncryptedTextFieldTester(TestCase):

    def setUp(self):

        # Assuming test password
        self.encryptions = {
            "asdf": "M/6UDLoCxk26sWW952hIqM94KVP0/JgSejSgV6OCUE8=",
            "I dare you!": "PBKPktGenuLqbTHEcyAuE3mUMCKvp2UFdCOjeTBMLWM=",
            "This is an sms": "XS4g9FrpyoFLxlClteQKYYdsEPZFEpO5xbJqVsQvPMA=",
            "test": "HTvSyhfJlQjRtKP2oufrITtQxClfBZHmf9igfHgg7VU=",
        }

    def get_db_value(self, field, model_id):
        cursor = connection.cursor()
        cursor.execute(
            'select {0} '
            'from j2p_field_testingmodel '
            'where id = {1};'.format(field, model_id)
        )
        return cursor.fetchone()[0]

    def test_char_field_decryption(self):

        for known_plaintext, known_ciphertext in self.encryptions.items():
            model = TestingModel()
            model.char_field = known_ciphertext
            model.save()

            plaintext = self.get_db_value('char_field', model.id)
            self.assertEqual(plaintext, known_plaintext)

    def test_text_field_decryption(self):

        for known_plaintext, known_ciphertext in self.encryptions.items():
            model = TestingModel()
            model.text_field = known_ciphertext
            model.save()

            plaintext = self.get_db_value('text_field', model.id)
            self.assertEqual(plaintext, known_plaintext)




