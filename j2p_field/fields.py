
import types

from j2p.JASYPT import J2PEngine

from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class J2PDecryptionFieldException(Exception):
    pass


class J2PWrapper(object):

    def __init__(self, password):
        self.j2p_engine = J2PEngine(password)

    def encrypt(self, plaintext):
        # return self.j2p_engine.encrypt(plaintext)

        raise NotImplementedError("J2P does not support encryption, only decryption")

    def decrypt(self, ciphertext):
        """
        Assumes that the ciphertext is encoded in base 64.

        :param ciphertext: base64 encoded ciphertext
        :return: plaintext decryption
        """
        return self.j2p_engine.decrypt(ciphertext)


class J2PEncryptedFieldMixin(object):

    decrypt_only = True
    enforce_max_length = False

    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        if hasattr(settings, 'J2P_PASSWORD'):
            self.password = settings.J2P_PASSWORD

        else:
            raise ImproperlyConfigured('You must set settings.J2P_PASSWORD')

        self.decrypt_only = kwargs.get('decrypt_only', True)
        self.enforce_max_length = kwargs.get('enforce_max_length', False)

        self._cryptor = J2PWrapper(self.password)
        super(J2PEncryptedFieldMixin, self).__init__(*args, **kwargs)

    def cryptor(self):
        return self._cryptor

    def get_internal_type(self):
        return 'TextField'

    def to_python(self, value):
        if value is None or not isinstance(value, types.StringTypes):
            return value

        try:
            value = self.cryptor().decrypt(value)
        except Exception:
            pass

        # return super(J2PEncryptedFieldMixin, self).to_python(value)
        return value

    def get_prep_value(self, value):
        # value = super(J2PEncryptedFieldMixin, self).get_prep_value(value)

        if value is None or value == '':
            return value

        if isinstance(value, types.StringTypes) and not self.decrypt_only:
            try:
                value = self.cryptor().encrypt(value)
            except Exception:
                pass

        return str(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)

            if self.enforce_max_length:
                if value and hasattr(self, 'max_length') and self.max_length and len(value) > self.max_length:
                    raise ValueError('Field {0} max_length={1} encrypted_len={2}'.format(self.name,
                                                                                         self.max_length,
                                                                                         len(value)))

        return value


class J2PEncryptedTextField(J2PEncryptedFieldMixin, models.TextField):
    pass


class J2PEncryptedCharField(J2PEncryptedFieldMixin, models.CharField):
    pass









