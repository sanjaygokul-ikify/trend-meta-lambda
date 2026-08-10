from packages.core import Engine
from packages.utils import logging

class Orchestrator:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        logging.info('Orchestrator started')

    def stop(self):
        logging.info('Orchestrator stopped')