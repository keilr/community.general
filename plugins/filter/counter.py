# -*- coding: utf-8 -*-
# Copyright (c) 2021, Remy Keil <remy.keil@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.module_utils.common._collections_compat import Sequence
from collections import Counter


def counter(sequence):
    ''' Count elements in a sequence. Returns dict with count result. '''
    if not isinstance(sequence, Sequence):
        raise AnsibleFilterError('First argument for counter must be a sequence (str or list). %s is %s' %
                                 (sequence, type(sequence)))

    for element in sequence:
        try:
            hash(element)
        except TypeError:
            raise AnsibleFilterError('Sequence elements must be hashable (int, float or str). %s is %s.' %
                                     (element, type(element)))

    result = dict(Counter(sequence))
    return result


class FilterModule(object):
    ''' Ansible counter jinja2 filters '''

    def filters(self):
        filters = {
            'counter': counter,
        }

        return filters
