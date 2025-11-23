import asyncio

async def generate_code(task: str) -> str:
    """
    Simulated code-generation agent.

    In a real system, this would send `task` to Claude (or another LLM)
    and receive source code back.

    Here we intentionally return an *imperfect* FastAPI service so that
    tests will fail and trigger the repair loop.
    """
    print("[code_agent] Generating initial FastAPI implementation for task:")
    print("            ", task)
    await asyncio.sleep(0.1)

    code = f'''"""
Task: {task}

This is the INITIAL (buggy) implementation produced by the code agent.
The /add endpoint ignores the do_round flag in this version.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
def add(a: float, b: float, do_round: bool = False):
    \"\"\"Add two numbers. Intentionally ignores do_round flag (bug).\"\"\"
    result = a + b
    # BUG: do_round is never used here
    return {{"result": result}}
'''
    return code

# LLMs like Claude/OpenAI often output FastAPI examples that lack:
# missing Pydantic model
# no input validation
# wrong parameter type
# no error handling
# no async endpoint
# no tests

# Your test suite can now fail for real reasons:
# missing type checks
# endpoint not async
# wrong structure
# unexpected HTTP status codes
