import unittest
from packages.core import Engine, Agent, Task, Result

class TestCore(unittest.TestCase):
    def test_engine(self):
        engine = Engine()
        agent = Agent('agent_id', 'name')
        task = Task('task_id', 'agent_id', 'data')
        engine.register_agent('agent_id', agent)
        engine.assign_task('task_id', task)
        result = engine.execute_task('task_id')
        self.assertIsInstance(result, Result)

    def test_agent(self):
        agent = Agent('agent_id', 'name')
        task = Task('task_id', 'agent_id', 'data')
        result = agent.execute_task(task)
        self.assertIsInstance(result, Result)

    def test_task(self):
        task = Task('task_id', 'agent_id', 'data')
        status = task.get_status()
        self.assertIsInstance(status, dict)