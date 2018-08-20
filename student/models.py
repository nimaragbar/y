from django.db import models
from django.utils import timezone

gender_choices = [('male', 'مرد'), ('female', 'زن'), ('other', 'سایر')]
# age_choices = [tuple([i, i]) for i in range(6, 32)]
age_choices = [(6, '۶'), (7, '۷'), (8, '۸'), (9, '۹'), (10, '۱۰'), (11, '۱۱'), (12, '۱۲'), (13, '۱۳'), (14, '۱۴'),
               (15, '۱۵'), (16, '۱۶'), (17, '۱۷'), (18, '۱۸'), (19, '۱۹'), (20, '۲۰'), (21, '۲۱'), (22, '۲۲'),
               (23, '۲۳'), (24, '۲۴'), (25, '۲۵'), (26, '۲۶'), (27, '۲۷'), (28, '۲۸'), (29, '۲۹'), (30, '۳۰')]
# TODO complete the state name in alphabetic order
location_choices = [('تهران', 'تهران'), ('اصفهان', 'اصفهان'), ('فارس', 'فارس'), ('خراسان', 'خراسان'),
                    ('مرکزی', 'مرکزی'), ('چهارمحال و بختیاری', 'چهارمحال و بختیاری'), ('سمنان', 'سمنان'),
                    ('آزربایجان شرقی', 'آزربایجان شرقی'), ('مازندران', 'مازندران'), ('گیلان', 'گیلان'), ('قم', 'قم'),
                    ('همدان', 'همدان'), ('کرمانشاه', 'کرمانشاه'), ('کرمان', 'کرمان'),
                    ('سیستان و بلوچستان', 'سیستان و بلوچستان'),
                    ('خوزستان', 'خوزستان'), ('آزربایجان غربی', 'آزربایجان غربی'), ('قزوین', 'قزوین')]
# Todo complete this level according to the new changes in school level
level_choices = [('اول ابتدایی', 'اول ابتدایی'), ('دوم ابتدایی', 'دوم ابتدایی'), ('سوم ابتدایی', 'سوم ابتدایی'),
                 ('دانشگاه', 'دانشگاه')]


class Profile(models.Model):
    first_name = models.CharField(max_length=200, default='نیما')
    last_name = models.CharField(max_length=200, default='محمدیان')
    gender = models.CharField(max_length=6, default='male', choices=gender_choices)
    age = models.IntegerField(default=6, choices=age_choices)
    level = models.CharField(max_length=32, choices=level_choices)
    password = models.CharField(max_length=32, default='1234')
    referral_code = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=32, default='تهران', choices=location_choices)
    paid = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(default='192.168.1.1')
    register_date = models.DateTimeField(default=timezone.now)
    email = models.URLField(max_length=36, default='someone@company.com')

    # to put profile image:
    profile_image = models.ImageField()

    def __str__(self):
        return "{} {}  -\n{} -\n{} -\n{}".format(self.first_name, self.last_name, self.age, self.location, self.paid)
