from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User

class Fragment(models.Model):
    '''
    シフトのコマ1つ1つ。希望も、確定版もここで管理
    '''

    start = models.DateTimeField('開始', )
    end = models.DateTimeField('終了', )
    member = models.ForeignKey(User, on_delete=PROTECT, )
    fixed = models.BooleanField('確定', default=False, )

