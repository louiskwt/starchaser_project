from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Member(models.Model):
    EMPTY = "NONE"
    FEMALE = "F"
    MALE = "M"
    STUDENT = "S"
    TEACHER = "T"

    YES = "Y"
    NO = 'N'

    BIO = 'biology'
    CHN = 'chinese'
    ENG = 'english'
    CHIST = 'c-hist'
    HIST = 'hist'
    IELTS = 'ielts'
    MATH = "math"
    CHEM = "chem"
    IT = "it"
    LS = "ls"
    SAT = "sat"
    ALV = "a-level"
    UNI = "uni"

    SUBJECTS_CHOICES = [
        (BIO, "DSE-生物"),
        (CHN, "DSE-中文"),
        (ENG, "DSE-英文"),
        (CHIST, "DSE-中史"),
        (HIST, "DSE-世史"),
        (IELTS, "IELTS"),
        (MATH, "DSE-數學"),
        (CHEM, "DSE-化學"),
        (IT, "DSE-資訊科技"),
        (LS, "DSE-通識"),
        (SAT, "SAT"),
        (ALV, "A-Level"),
        (UNI, "大專補習")
    ]

    ROLE_CHOICES = [
        (STUDENT, "學生"),
        (TEACHER, "導師"),
        (EMPTY, "--請選擇--")
    ]

    GENDER_CHOICES = [
        (FEMALE, '女'),
        (MALE, '男'),
    ]

    YES_NO_CHOICES = [
        (YES, '是'),
        (NO, '否')
    ]
    class MemberTier(models.TextChoices):
        FREE = "FREE", _('一般會員')
        PAID = "PAID", _('星級會員')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True, null=True)
    phone_num = models.CharField(max_length=8, blank=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default=EMPTY, null=False)

    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default=EMPTY, null=False)

    status = models.CharField(max_length=56, blank=True, null=False)
    description = models.TextField()
    member_type = models.CharField(max_length=4, choices=MemberTier.choices, default=MemberTier.FREE)

    active = models.CharField(max_length=3, choices=YES_NO_CHOICES, default=YES, null=False)

    subject = models.CharField(max_length=8, choices=SUBJECTS_CHOICES, default=EMPTY, null=False)

    def __str__(self):
        return f'Profile for user {self.user.username}'