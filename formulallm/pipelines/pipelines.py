import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents import executor_agent, fixer_agent, interpreter_agent, userproxy_agent
from autogen import GroupChat, GroupChatManager
from formula.formula_program import *

local_llm_config={
    "config_list": [
        {
            "model": "NotRequired", # Loaded with LiteLLM command
            "api_key": "NotRequired", # Not needed
            "base_url": "http://0.0.0.0:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None # Turns off caching, useful for testing different models
}

code = load("/home/zhang0311/FormulaLLMPY/examples/data/MappingExample.4ml")

task = f"First read the following code written in a DSL called formula to understand the syntax. \nThen perform the tasks according to the user's instruction! \n\n{code}"



groupchat = GroupChat(
    agents=[userproxy_agent, fixer_agent, executor_agent, interpreter_agent],
    messages=[],
    max_round=10,
    send_introductions=True,
    allowed_or_disallowed_speaker_transitions = {
        fixer_agent: [userproxy_agent, executor_agent],
        executor_agent: [userproxy_agent]
    },
    speaker_transitions_type="allowed"
)

manager = GroupChatManager(
    groupchat=groupchat, llm_config=local_llm_config
)

groupchat_result = userproxy_agent.initiate_chat(
    manager,
    message=task,
)
