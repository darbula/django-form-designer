# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_designer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdefinition',
            name='form_template_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='form template', choices=[(b'', 'Default'), (b'html/formdefinition/forms/as_p.html', 'as paragraphs'), (b'html/formdefinition/forms/cisco.html', 'Cisco')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formdefinitionfield',
            name='field_class',
            field=models.CharField(max_length=100, verbose_name='field class', choices=[(b'riteh.core.form_designer.fields.TitleField', 'Title Field'), (b'django.forms.CharField', 'Text'), (b'django.forms.EmailField', 'E-mail address'), (b'django.forms.URLField', 'Web address'), (b'django.forms.IntegerField', 'Number'), (b'django.forms.DecimalField', 'Decimal number'), (b'django.forms.BooleanField', 'Yes/No'), (b'django.forms.DateField', 'Date'), (b'django.forms.ChoiceField', 'Choice'), (b'django.forms.MultipleChoiceField', 'Multiple Choice'), (b'django.forms.FileField', 'File')]),
            preserve_default=True,
        ),
    ]
