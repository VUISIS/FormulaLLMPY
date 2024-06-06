from pythonnet import load
load("coreclr")
import os, glob
import clr
from typing import Optional

process_path = glob.glob(os.path.expanduser('~') + r'/.dotnet/tools/.store/vuisis.formula*/**/VUISIS.Formula*.dll', recursive=True)

clr.AddReference(process_path[0])

from Microsoft.Formula.CommandLine import CommandInterface, CommandLineProgram
from System.IO import StringWriter
from System import Console

sink = CommandLineProgram.ConsoleSink()
chooser = CommandLineProgram.ConsoleChooser()
ci = CommandInterface(sink, chooser)

sw = StringWriter()
Console.SetOut(sw)
Console.SetError(sw)

def run_command(cmd: str):
    pr = True
    if ("$wait" in cmd) or ("$unload" in cmd):
        pr = False
        cmd = cmd[1:]

    if not ci.DoCommand(cmd):
        raise Exception("Command failed.")
    
    output = sw.ToString()
    output = output[:-5]
    sw.GetStringBuilder().Clear()

    if pr: 
        print(output)

def load(file_path: str) -> str:
    run_command("$unload *")
    file = os.path.abspath(file_path)
    file_txt = ""
    if os.path.isfile(file):
        f = open(file, 'r')
        try:
            file_txt = f.read()
        finally:
            f.close()
        run_command("load " + file_path)
    return file_txt

def query(model: str, goals: str):
    run_command("query " + model + " " + goals)

def apply(transformstep: str):
    run_command("apply " + transformstep)

def confhelp():
    run_command("confhelp")

def core(module_name: str):
    run_command("core " + module_name)

def delete(var: str):
    run_command("del " + var)

def details(modname: str):
    run_command("det " + modname)

def downgrade(module_name: str):
    run_command("downgrade " + module_name)

def exit():
    run_command("exit")

def extract(id: str, n: str = 0, output_name: str = 0):
    """Extract and print the nst. solution from solved task with the id

    Args:
        id (str): The id of the task we want to extract from the list of tasks.
        n (str): The id of the solution we want to extract from the set of solutions to the task
        output_name (str): The name of the file where the output is saved.
    
    Returns:
        str: A line specifying the solution number 
        followed by lines of solution completing the partial model.
    """
    run_command("extract " + id + " " + n + " " + output_name)

def generate(modname: str):
    run_command("generate " + modname)

def help():
    run_command("help")

def interactive(on_off: bool):
    if on_off:
        run_command("interactive on")
    else:
        run_command("interactive off")

def list(option: Optional[str] = None):
    """Display tasks status

    Returns:
        str: Including environment variables, programs in file root, programs in env root, 
             and a form of all tasks
    """
    if option == None:
        run_command("list")
    else:
        run_command("list " + option)

def p(progname: str):
    run_command("print " + progname)

def proof(id: str, term: Optional[str] = None):
    if term == None:
        run_command("proof " + id)
    else:
        run_command("proof " + id + " " + term)

def reload(prog: str):
    run_command("reload " + prog)

def render(modname: str):
    run_command("render " + modname)

def save():
    run_command("save")

def set(var: str, term: Optional[str] = None):
    if term == None:
        run_command("set " + var)
    else:
        run_command("set " + var + " " + term)

def solve(partial_model: str, max_sols: str, goals: str):
    """Try to complete the paritial model that conforms to the goal, 
       and come up with [max_sols] number of solutions. 
       Note that the max_sols is default to 1

       An example call of this function: solve pm 1 Mapping.conforms

    Args:
        partial_model (str): The name of the partial model we want to complete.
        max_sols (str): The max number of solutions the program needs to find. Default = 1
        goals (str): The goal we want the partial model to conform to. 
                     Format it like this: <domain>.conforms
    
    Returns:
        str: "Started solve task with Id <id>."
    """
    run_command("solve " + partial_model + " " + max_sols + " " + goals)

def stats(taskid: str, rule: Optional[str] = None):
    if rule == None:
        run_command("stats " + taskid)
    else:
        run_command("stats " + taskid + " " + rule)

def truth(taskid: str, term: Optional[str] = None):
    if term == None:
        run_command("truth " + taskid)
    else:
        run_command("truth " + taskid + " " + term)

def tunload(id: str):
    run_command("tunload " + id)

def types(modname: str):
    run_command("types " + modname)

def unload(prog: str):
    run_command("unload " + prog)

def verbose(on_off: bool):
    if on_off:
        run_command("verbose on")
    else:
        run_command("verbose off")

def wait(on_off: bool):
    if on_off:
        run_command("wait on")
    else:
        run_command("wait off")

def watch(on_off: str):
    run_command("watch " + on_off)

run_command("$wait on")

run_command("$unload *")