import unittest
from packages.core import Engine, Agent, Task, Result
from services import orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine()
        agent = Agent('agent_id', 'name')
        task = Task('task_id', 'agent_id', 'data')
        engine.register_agent('agent_id', agent)
        engine.assign_task('task_id', task)
        result = engine.execute_task('task_id')
        orchestrator.Orchestrator().start()
        orchestrator.Orchestrator().stop()
        self.assertIsInstance(result, Result)