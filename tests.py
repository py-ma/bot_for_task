import unittest
import main
import states

class Test(unittest.TestCase):
    async def test_start_to_t2(self):
        self.assertEqual(await main.start(states.s.t1()), states.s.t2())

    async def test_waiting_yes(self):
        self.assertEqual(await main.start(states.s.t2()), states.s.t3())

    async def test_choose_pay_method(self):
        self.assertEqual(await main.start(states.s.t3()), states.s.t4())

    async def test_repeat_order(self):
        self.assertEqual(await main.start(states.s.t4()), states.s.t5())

    async def test_fault(self):
        self.assertEqual(await main.start(states.s.tn()), states.s.t2())

    async def test_finish(self):
        self.assertEqual(await main.start(states.s.t5()), states.s.t6())

    async def test_transition(self):
        self.assertEqual(await main.start(states.s.t6()), states.s.t1())


# python -m unittest tests.py
if __name__ == '__main__':
    unittest.tests()
