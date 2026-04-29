"""Initial migration for analytics models."""

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=200)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True)),
                ('referrer', models.URLField(blank=True, null=True)),
                ('user_role', models.CharField(blank=True, default='',
                 help_text='Role of the authenticated user (ADMIN, RECRUITER, USER) or empty for anonymous', max_length=20)),
                ('visited_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-visited_at'],
            },
        ),
    ]
