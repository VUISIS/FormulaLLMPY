from autogen import ConversableAgent

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

user_proxy = ConversableAgent(
    name="Administrator",
    system_message = '''Give the task, 
                     and send instructions and feedback so that the user
                     can understand what the DSL model represents,
                     why it is "broken, and how to fix it."
                     ''',
    llm_config = local_llm_config,
    code_execution_config = False, 
    human_input_mode="ALWAYS",
    description = '''User Proxy.
                  Provides instructions and feedback.
                  '''
)

__all__ = ['userproxy_agent']