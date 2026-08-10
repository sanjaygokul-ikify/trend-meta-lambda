from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from .types import Agent, Task, Result
from .exceptions import AgentNotRegisteredError, TaskNotAssignedError
import logging

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self):
        self.agents = {}
        self.tasks = {}

    def register_agent(self, agent_id: str, agent: Agent):
        self.agents[agent_id] = agent
        logger.info(f'Agent {agent_id} registered')

    def unregister_agent(self, agent_id: str):
        if agent_id in self.agents:
            del self.agents[agent_id]
            logger.info(f'Agent {agent_id} unregistered')
        else:
            raise AgentNotRegisteredError(f'Agent {agent_id} not registered')

    def assign_task(self, task_id: str, task: Task):
        self.tasks[task_id] = task
        logger.info(f'Task {task_id} assigned')

    def unassign_task(self, task_id: str):
        if task_id in self.tasks:
            del self.tasks[task_id]
            logger.info(f'Task {task_id} unassigned')
        else:
            raise TaskNotAssignedError(f'Task {task_id} not assigned')

    def execute_task(self, task_id: str) -> Result:
        if task_id in self.tasks:
            task = self.tasks[task_id]
            agent_id = task.agent_id
            if agent_id in self.agents:
                agent = self.agents[agent_id]
                try:
                    result = agent.execute_task(task)
                    logger.info(f'Task {task_id} executed')
                    return result
                except Exception as e:
                    # Handle the exception instead of propagating it
                    logger.error(f'Unexpected error executing task {task_id}: {e}')
                    raise AgentNotRegisteredError(f'Failed to execute task {task_id}')
            else:
                raise AgentNotRegisteredError(f'Agent {agent_id} not registered')
        else:
            raise TaskNotAssignedError(f'Task {task_id} not assigned')

    def get_agent_status(self, agent_id: str) -> Dict:
        if agent_id in self.agents:
            agent = self.agents[agent_id]
            return agent.get_status()
        else:
            raise AgentNotRegisteredError(f'Agent {agent_id} not registered')

    def get_task_status(self, task_id: str) -> Dict:
        if task_id in self.tasks:
            task = self.tasks[task_id]
            return task.get_status()
        else:
            raise TaskNotAssignedError(f'Task {task_id} not assigned')

class Agent(ABC):
    @abstractmethod
    def execute_task(self, task: Task) -> Result:
        pass

    @abstractmethod
    def get_status(self) -> Dict:
        pass

class Task:
    def __init__(self, task_id: str, agent_id: str, data: str):
        self.task_id = task_id
        self.agent_id = agent_id
        self.data = data
        self.status = 'pending'

    def get_status(self) -> Dict:
        return {'status': self.status}