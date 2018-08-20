# Generated by Django 2.1 on 2018-08-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[(1, 'اول ابتدایی'), (2, 'دوم ابتدایی'), (3, 'سوم ابتدایی'), (13, 'دانشگاه')], default='دانشکاه', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(choices=[(6, '۶'), (7, '۷'), (8, '۸'), (9, '۹'), (10, '۱۰'), (11, '۱۱'), (12, '۱۲'), (13, '۱۳'), (14, '۱۴'), (15, '۱۵'), (16, '۱۶'), (17, '۱۷'), (18, '۱۸'), (19, '۱۹'), (20, '۲۰'), (21, '۲۱'), (22, '۲۲'), (23, '۲۳'), (24, '۲۴'), (25, '۲۵'), (26, '۲۶'), (27, '۲۷'), (28, '۲۸'), (29, '۲۹'), (30, '۳۰')], default=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.URLField(default='someone@company.com', max_length=36),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='نیما', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'مرد'), ('female', 'زن'), ('other', 'سایر')], default='male', max_length=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='محمدیان', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(choices=[('تهران', 'تهران'), ('اصفهان', 'اصفهان'), ('فارس', 'فارس'), ('خراسان', 'خراسان'), ('مرکزی', 'مرکزی'), ('چهارمحال و بختیاری', 'چهارمحال و بختیاری'), ('سمنان', 'سمنان'), ('آزربایجان شرقی', 'آزربایجان شرقی'), ('مازندران', 'مازندران'), ('گیلان', 'گیلان'), ('قم', 'قم'), ('همدان', 'همدان'), ('کرمانشاه', 'کرمانشاه'), ('کرمان', 'کرمان'), ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('خوزستان', 'خوزستان'), ('آزربایجان غربی', 'آزربایجان غربی'), ('قزوین', 'قزوین')], default='تهران', max_length=32),
        ),
        migrations.AlterField(
            model_name='profile',
            name='referral_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]