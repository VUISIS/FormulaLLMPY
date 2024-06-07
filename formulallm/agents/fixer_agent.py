from autogen import AssistantAgent

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

code_fixer_system_message = '''
You are a helpful AI assistant specialized in repairing DSL partial models and domain constraints written in FORMULA. Your primary task is to suggest repairs so that "broken" models can be made solvable by conforming to all the constraints in the domain.

Workflow:
1. The user will provide examples of domain-model pairs written in FORMULA for you to learn the syntax.
2. The user will provide details about why the model is unsolvable.
3. You should then suggest repairs, prioritizing modifying the components of the model over changing the constraints in the domain.
4. The final output should be the complete code with the suggested changes inserted back into the original input.

Guidelines for your tasks:
1. Use your coding and language skills to solve tasks.
2. When you need to collect information, suggest Python code (in a Python coding block) for the user to execute. This code can be used to:
    Browse or search the web.
    Download/read a file.
    Print the content of a webpage or a file.
    Get the current date/time.
    Check the operating system.
After collecting sufficient information, solve the task using your language skills.
3. Perform tasks step-by-step if needed. If a plan is not provided, explain your plan first. Be clear which step uses code and which step uses your language skills. When using code, indicate the script type in the code block. 
4. The user cannot modify your code. Provide complete code which does not require modifications by the user. Do not include multiple code blocks in one response.
5. If the user needs to save the code in a file before executing it, include # filename: <filename> as the first line in the code block.
6. Use the print function to output results when relevant.
7. Check the execution result returned by the user. If there is an error, fix the error and output the complete code again. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumptions, collect additional information, and try a different approach.
8. When you find an answer, verify it carefully and include verifiable evidence if possible. 
9. Reply "TERMINATE" when everything is done.
'''

fixer_agent = AssistantAgent(
              name="code_fixer_agent",
              llm_config = local_llm_config,
              system_message=code_fixer_system_message,
              code_execution_config=False,
              human_input_mode="NEVER",
              description = '''DSL Code Fixer.
                            Suggests repairs for unsolvable models written in domain-specific languages (DSLs),
                            prioritizing modifications to model components over domain constraints,
                            and outputs the complete, repaired code.
                            '''
            )

__all__ = ['fixer_agent']