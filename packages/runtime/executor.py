from typing import Dict, List, Tuple
from . import Executor
from packages.core.engine import Engine
from packages.core.types import Agent, Task, Result
import logging

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, task_id: str) -> Result:
        result = self.engine.execute_task(task_id)
        logger.info(f'Task {task_id} executed')
        return result

    def register_agent(self, agent_id: str, agent: Agent):
        self.engine.register_agent(agent_id, agent)
        logger.info(f'Agent {agent_id} registered')

    def unregister_agent(self, agent_id: str):
        self.engine.unregister_agent(agent_id)
        logger.info(f'Agent {agent_id} unregistered')

    def assign_task(self, task_id: str, task: Task):
        self.engine.assign_task(task_id, task)
        logger.info(f'Task {task_id} assigned')

    def unassign_task(self, task_id: str):
        self.engine.unassign_task(task_id)
        logger.info(f'Task {task_id} unassigned')