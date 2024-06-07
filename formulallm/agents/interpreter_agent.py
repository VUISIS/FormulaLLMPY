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

interpreter_agent = ConversableAgent(name = "interpreter_agent", 
                               system_message = '''You are a specialized coding assistant designed to 
                                                help users understand and explain code written in domain-specific languages (DSLs). 
                                                You should provide clear, detailed explanations of code snippets written in DSLs.
                                                In situations where the DSL model is "broken" (unsolvable), 
                                                you should provide clear, detailed explanations of why it is unsolvable.
                                                ''',
                               llm_config = local_llm_config,
                               human_input_mode = "NEVER",
                               code_execution_config = False,
                               is_termination_msg = lambda msg: "Terminate" in msg["content"],
                               description = '''DSL Code Interpreter. 
                                             Provides detailed explanations of code snippets written in domain-specific languages (DSLs) 
                                             and identifies why certain code may be unsolvable.                                            
                                             '''
                               )

__all__ = ['interpreter_agent']