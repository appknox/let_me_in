#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: dbapi.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-02-09
"""

from let_me_in.core.models import User


def create_user(email, name, referrer):
    user = User(email=email, name=name, referrer=referrer)
    user.save()
    return user


def get_user_by_email(email):
    """
    docstring for get_user_by_email
    """
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def get_user_by_uuid(uuid):
    """
    docstring for get_user_by_email
    """
    try:
        return User.objects.get(uuid=uuid)
    except (User.DoesNotExist, ValueError):
        return None
