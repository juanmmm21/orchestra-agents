"""ReAct agents and a multi-agent orchestrator with task delegation."""

from .agent import AutonomousAgent
from .orchestrator import AgentOrchestrator, TaskDelegation

__version__ = "0.1.0"

__all__ = ['AutonomousAgent', 'AgentOrchestrator', 'TaskDelegation']
