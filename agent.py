"""Compatibilidad: el código vive en el paquete `orchestra_agents`. Este módulo se
conserva para quien añade esta carpeta a `sys.path` e importa `agent`
directamente."""

from orchestra_agents.agent import *  # noqa: F401,F403
from orchestra_agents.agent import AutonomousAgent  # noqa: F401
