
from django.db import models

from j2p_field.fields import J2PEncryptedTextField, J2PEncryptedCharField


class TestingModel(models.Model):
    char_field = J2PEncryptedCharField(max_length=255, null=True, blank=True)
    text_field = J2PEncryptedTextField(null=True, blank=True)

    # class Meta:
    #     app_label = 'testmodel'
