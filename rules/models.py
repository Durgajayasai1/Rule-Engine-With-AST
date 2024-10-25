# rules/models.py
from django.db import models

class Rule(models.Model):
    rule_string = models.CharField(max_length=255, null=False)
    ast = models.TextField(null=False,unique=True)

    def __str__(self):
        return self.rule_string
