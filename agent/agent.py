from google.adk.agents.llm_agent import Agent

from . import prompts
from tools.git_docs_builder import generate_documentation
from tools.diagram_generator import generate_diagram, get_valid_node_types
from agent.callbacks.preprocess import normalize_json_inputs

root_agent = Agent(
    model='gemini-2.5-flash',
    name='ccagent',
    description="""CCAgent (Code Chronicler Agent) analyzes source code repositories
    'to automatically generate technical documentation and architecture diagrams.
    """,
    instruction=prompts.CCAGENT_PROMPT,
    tools=[generate_documentation, generate_diagram, get_valid_node_types],
    before_agent_callback=normalize_json_inputs,
)





