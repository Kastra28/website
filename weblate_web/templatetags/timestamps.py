# -*- coding: utf-8 -*-
#
# Copyright © 2012–2019 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from django.template import Library
from django.utils import timezone
from django.utils.translation import pgettext

register = Library()


@register.filter
def recently(value):
    now = timezone.now()
    delta = now - value
    if delta.days > 12:
        return pgettext("123 translations ...", "this month")
    if delta.days >= 2:
        return pgettext("123 translations ...", "this week")
    if delta.days == 1:
        return pgettext("123 translations ...", "yesterday")
    if delta.seconds > 10000:
        return pgettext("123 translations ...", "today")
    if delta.seconds > 2000:
        return pgettext("123 translations ...", "recently")
    return pgettext("123 translations ...", "just now")
