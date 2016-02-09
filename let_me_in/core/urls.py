#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: urls.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-02-09
"""

from let_me_in.core.views import register

from django.conf.urls import url


urlpatterns = [
    url(r'^register$', register)
]
