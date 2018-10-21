# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    store_key = models.CharField(max_length=300)
    product_name = models.CharField(max_length=300)