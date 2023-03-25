import sys
import random
import asyncio
sys.path.append('/home/srihari/wa/pypassiveuvm/src/sv')
import unittest
from sv_mailbox import sv_mailbox
from sv_int import sv_int

class TestMailbox(unittest.TestCase):


    def test_try_put_try_get_num(self):
        mb = sv_mailbox(0, sv_int())
        for x in range(1,10):
            a = sv_int()
            a.value = x
            result = mb.try_put(a)
            self.assertEqual(result, 1)
            self.assertEqual(mb.num(), x)
        for x in range(1,10):
            b = sv_int()
            result = mb.try_get(b)
            self.assertEqual(result,1)
            self.assertEqual(x,b.value)
            self.assertEqual(mb.num(), 9-x)

    def test_bound(self):
        for x in range(1,10):
            mb = sv_mailbox(x, sv_int())
            for y in range(0,x):
                a = sv_int()
                a.value = y
                result = mb.try_put(a)
                self.assertEqual(result, 1)

            for i in range(0,5):
                a = sv_int()
                result = mb.try_put(a)
                self.assertEqual(result, 0)

            for y in range(0,x):
                b = sv_int()
                result = mb.try_get(b)
                self.assertEqual(result,1)
                self.assertEqual(y,b.value)

            for i in range(0,5):
                a = sv_int()
                result = mb.try_get(a)
                self.assertEqual(result, 0)

class TestAsyncIOMailbox(unittest.IsolatedAsyncioTestCase):

    async def put_at_time(self,x):
        mb.put(a)
        return 

    async def get_after(self, mb, x, b):
        time =
        await asyncio.sleep(x)
        mb.get(b)
        return time

    async def test_get_after_put_num(self):
        a = sv_int()
        mb = sv_mailbox(1, sv_int())
        mb.put(a)
