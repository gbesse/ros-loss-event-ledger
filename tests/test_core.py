import unittest,math
from ros_loss_event_ledger.core import run
class DomainTests(unittest.TestCase):
 def test_incremental_not_max(self):self.assertEqual(run({'events':[dict(id='a',time=1,lost={'t':2}),dict(id='b',time=2,lost={'t':3})]})['observed_incremental_losses'],{'t':5})
 def test_dedupe_and_conflict(self):
  x=run({'events':[dict(id='a',time=1,lost={'t':2}),dict(id='a',time=1,lost={'t':2}),dict(id='a',time=1,lost={'t':3})],'coverage_complete':True});self.assertEqual(x['duplicate_events'],['a']);self.assertFalse(x['complete']);self.assertEqual(x['observed_incremental_losses'],{'t':2})
 def test_silence_unknown(self):self.assertFalse(run({'events':[]})['complete'])
