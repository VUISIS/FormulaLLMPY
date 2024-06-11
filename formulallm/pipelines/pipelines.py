# import sys
# import os

# # Add the parent directory to the system path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from agents import executor_agent, fixer_agent, interpreter_agent, userproxy_agent
# from autogen import GroupChat, GroupChatManager
# from formula.formula_program import *

# local_llm_config={
#     "config_list": [
#         {
#             "model": "NotRequired", # Loaded with LiteLLM command
#             "api_key": "NotRequired", # Not needed
#             "base_url": "http://0.0.0.0:4000"  # Your LiteLLM URL
#         }
#     ],
#     "cache_seed": None # Turns off caching, useful for testing different models
# }

# code = load("/home/zhang0311/FormulaLLMPY/examples/data/MappingExample.4ml")

# task = ""



# groupchat = GroupChat(
#     agents=[userproxy_agent, fixer_agent, executor_agent, interpreter_agent],
#     messages=[],
#     max_round=10,
#     send_introductions=True,
#     allowed_or_disallowed_speaker_transitions = {
#         fixer_agent: [userproxy_agent, executor_agent],
#         executor_agent: [userproxy_agent]
#     },
#     speaker_transitions_type="allowed"
# )

# manager = GroupChatManager(
#     groupchat=groupchat, llm_config=local_llm_config
# )

# chat_result = userproxy_agent.initiate_chats(
#     [
#         {
#             "recipient": fixer_agent,
#             "message": f'''
#                         You are provided with a corpus of examples consisting of domain-model pairs written in a DSL called Formula. 
#                         Each example includes:
#                             1. An unsolvable partial model.
#                             2. A least unsatisfiable core condition (unsat core) that explains why the model is unsolvable.
#                             3. A corrected version, where either the constraints in the domain or the components in the model are modified to make the model solvable.
            
#                         Your task is to:
#                             1. Study these examples to learn the syntax of Formula.
#                             2. Understand how the unsat cores explain the unsolvability of the models.
#                             3. Learn how to suggest repairs to the broken DSL models based on this understanding.
                        
#                         When suggesting repairs, prioritize modifying the partial models over the constraints in the domain.
#                         ''',
#              "silent": True
#         },
#         {
#             "recipient": manager,
#             "message": task,
#         },
#     ]
# )