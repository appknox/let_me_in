#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: admin.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-11-25
"""

from django.contrib import admin

from let_me_in.core.models import User

admin.site.register(User)
