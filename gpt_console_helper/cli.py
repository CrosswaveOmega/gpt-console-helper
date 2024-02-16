from gptfunctionutil import SingleCallAsync
from openai import AsyncClient
from gptfunctionutil import GPTFunctionLibrary, AILibFunction, LibParam
import asyncio

import sys
import subprocess
class MyCall(GPTFunctionLibrary):
    @AILibFunction(name="get_unix_help", 
                   description="Provide the user with the bash command or commands that will allow the user to do what they need.",
                   required=['command','help'])
    @LibParam(command="The bash command that will preform what the user needs.",
              help="A paragraph explaining what the command the command will do.")
    async def unix_help(self, help: str,command:str):
        # Wait for a set period of time.
        print('help:',help)
        print(command)
        return command



async def make_query(arg, run=False):
    client = AsyncClient()
    print(f"Querying AI with {arg}.")
    sc=SingleCallAsync(mylib=MyCall(),client=client,timeout=15)

    command=await sc.call_single(arg,"get_unix_help")
    if run:
        print("automatic command run disabled for security.")

        #await runner(command[0][1]['content'])
        

async def run_async():
    

    arg = sys.argv[1]
    autorun = '-r' in sys.argv

    await make_query(arg, run=autorun)

def run_sync():
    if len(sys.argv) < 2 or '-h' in sys.argv:
        print("Usage: how_to <argument> [-r] [-h]")
        print("Ask OpenAI's API how to preform a specific command.")
        print("Options:")
        print("  -r    Run the command automatically if possible.  Currently disabled.")
        print("  -h    Show this help message and exit.")
        sys.exit(1)
    asyncio.run(run_async())

if __name__ == "__main__":
    run_sync()
