# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import j2p_field.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestingModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_field', j2p_field.fields.J2PEncryptedCharField(max_length=255, null=True, blank=True)),
                ('text_field', j2p_field.fields.J2PEncryptedTextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
