# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : NoviceMaster
# @Email   : mrchenbin@126.com
# @Time    : 2021/1/6 17:12 
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        # 调用django的认证系统加密密码
        user.set_password(validated_data['password'])
        user.save()
        return user
