#!/usr/bin/env python
# Copyright (C) 2010-2014 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import random
import string


def random_string(minimum, maximum=None):
    if maximum is None:
        maximum = minimum

    count = random.randint(minimum, maximum)
    return ''.join(random.choice(string.ascii_letters) for x in xrange(count))


def random_mac():
    """Generates a random MAC address."""
    values = [random.randint(0, 15) for _ in xrange(12)]

    # At least for VirtualBox there's a limitation for the second character,
    # as outlined in the following thread. Thus we handle this.
    # https://forums.virtualbox.org/viewtopic.php?p=85316
    values[1] = int(random.choice('02468ace'), 16)

    return '%x%x:%x%x:%x%x:%x%x:%x%x:%x%x' % tuple(values)


def random_serial(length=None):
    if length is None:
        length = random.randint(8, 20)

    return ''.join(random.choice(string.uppercase + string.digits)
                   for _ in xrange(length))