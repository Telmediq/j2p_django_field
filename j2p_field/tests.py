
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

    def set_db_value(self, char_field=None, text_field=None):
        """
        Insert the simple model into the database without using the model structure.
        This circumvents the encryption/decryption of the model.

        :param char_field:
        :param text_field:
        :return:
        """
        char_field = 'null' if char_field is None else str(char_field)
        text_field = 'null' if text_field is None else str(text_field)

        cursor = connection.cursor()

        query = 'insert into j2p_field_testingmodel (char_field, text_field) values (\'{0}\', \'{1}\');'
        cursor.execute(query.format(char_field, text_field))

    def test_char_field_decryption(self):

        # Set encrypted content in the database
        for known_plaintext, known_ciphertext in self.encryptions.items():
            self.set_db_value(char_field=known_ciphertext)

        # Get objects out of the DB using the model (should decrypt)
        test_models = TestingModel.objects.all()
        plaintexts = self.encryptions.keys()

        for model in test_models:
            cf = model.char_field
            self.assertIn(cf, plaintexts)

    def test_text_field_decryption(self):

        # Set encrypted content in the database
        for known_plaintext, known_ciphertext in self.encryptions.items():
            self.set_db_value(text_field=known_ciphertext)

        test_models = TestingModel.objects.all()
        plaintexts = self.encryptions.keys()

        for model in test_models:
            tf = model.text_field
            self.assertIn(tf, plaintexts)




