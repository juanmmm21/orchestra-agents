# Orchestra Agents

Un framework modular para el diseño y ejecucion de sistemas multi-agente autonomos basados en el patron de razonamiento ReAct (Thought-Action-Observation). El sistema permite que multiples agentes con roles especializados (como investigadores, redactores y programadores) colaboren entre si delegando tareas y pasandose contexto para resolver metas complejas de infraestructura de Inteligencia Artificial.

## Arquitectura y Componentes Nucleares

El framework consta de dos capas principales de abstraccion:

### 1. Agente Autonomo ReAct (`agent.py`):
*   **Bucle de Razonamiento:** Ejecuta de forma incremental la secuencia de Pensamiento (Thought), Accion (Action, llamada a herramientas) y Observacion (Observation, resultados de herramientas) hasta alcanzar una respuesta final (`Final Answer`).
*   **Registro de Herramientas:** Permite enlazar funciones ejecutables nativas de Python de forma dinamica al catalogo del agente.
*   **Simulacion Cognitiva (Offline Fallback):** Incorpora un motor de simulacion que reproduce el razonamiento y comportamiento del agente paso a paso en base al estado de su bitacora (scratchpad), permitiendo pruebas locales instantaneas sin API Keys.

### 2. Orquestador de Agentes (`orchestrator.py`):
*   **Descomposicion de Tareas:** Divide una meta-tarea global en un grafo ordenado de subtareas estructuradas con dependencias explicitas de ejecucion.
*   **Mensajeria y Contexto (Message Passing):** Coordina la transferencia de informacion. Los resultados obtenidos por los agentes en pasos iniciales son inyectados dinamicamente como contexto en el prompt del agente asignado al siguiente paso.

## Requisitos e Instalacion

*   Python 3.8 o superior
*   Pydantic

Para instalar las dependencias locales, ejecute:

```bash
pip install -r requirements.txt
```

## Pruebas y Verificacion

1.  **Ejecutar Suite de Pruebas Unitarias:**
    ```bash
    python -m unittest test_agents.py
    ```
2.  **Ejecutar Demostracion Multi-Agente:**
    ```bash
    python example.py
    ```
    El script demostrara a un agente investigador (`ResearcherAgent`) realizando busquedas vectoriales sobre `NanoVectorDB` y entregando sus hallazgos a un agente redactor (`WriterAgent`) para consolidar un informe de arquitectura tecnico en formato Markdown.
