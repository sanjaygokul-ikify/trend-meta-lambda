from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class Agent:
    agent_id: str
    name: str

@dataclass
class Task:
    task_id: str
    agent_id: str
    data: str

@dataclass
class Result:
    result_id: str
    task_id: str
    data: str