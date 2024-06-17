from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0069_gfk_indexes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prefix',
            old_name='site',
            new_name='scope_id',
        ),
        migrations.AlterField(
            model_name='prefix',
            name='scope_id',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prefix',
            name='scope_type',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('app_label', 'dcim'), ('model__in', ['region', 'sitegroup', 'site', 'location', 'rack'])), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterModelOptions(
            name='prefix',
            options={'ordering': ('name', 'pk'), 'verbose_name': 'Prefix', 'verbose_name_plural': 'Prefixes'},
        ),
        migrations.AlterUniqueTogether(
            name='prefix',
            unique_together={('scope_type', 'scope_id'), ('scope_type', 'scope_id')},
        ),
    ]