"""Compatibilidad: el código vive en el paquete `orchestra_agents`. Este módulo se
conserva para quien añade esta carpeta a `sys.path` e importa `orchestrator`
directamente."""

from orchestra_agents.orchestrator import *  # noqa: F401,F403
from orchestra_agents.orchestrator import AgentOrchestrator, TaskDelegation  # noqa: F401
