# Generated by Django 3.0.3 on 2020-02-21 04:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length of 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automatically cropped 570px by 370px'))])))]))], blank=True, null=True),
        ),
    ]
