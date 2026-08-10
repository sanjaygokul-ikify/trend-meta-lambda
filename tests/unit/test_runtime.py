import unittest
from services import orchestrator

class TestRuntime(unittest.TestCase):
    def test_orchestrator(self):
        orchestrator.Orchestrator().start()
        orchestrator.Orchestrator().stop()