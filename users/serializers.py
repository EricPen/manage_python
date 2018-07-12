#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 10:11
# @Author  : qiaoyu

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
