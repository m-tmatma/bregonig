#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from ctypes import *
from bregonig import *

LoadBregonig()

print(BRegexpVersion())
print()

rxp = POINTER(BREGEXP)()
msg = create_string_buffer(BREGEXP_MAX_ERROR_MESSAGE_LEN)

t1 = " Yokohama 045-222-1111  Osaka 06-5555-6666  Tokyo 03-1111-9999 ".encode('ASCII')
t1p = cast(t1, c_void_p)
pattern1 = r"s/(\d\d)-\d{4}-\d{4}/$1-xxxx-xxxx/g".encode('ASCII')
ctr = BSubst(pattern1, t1p, t1p.value + len(t1), byref(rxp), msg)
if ctr > 0:
    if rxp.contents.outp:
        print("after(%d)=%s" % (ctr, string_at(rxp.contents.outp).decode('ASCII')))
        print("length=%d" % (rxp.contents.outendp - rxp.contents.outp))
    else:
        # Result is an empty string.
        print("after(%d)" % ctr)
        print("length=0")

if (rxp):
    BRegfree(rxp)

