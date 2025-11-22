import asyncio

async def generate_code(task: str) -> str:
    # In a real system, this would call Claude / Cursor / other LLM APIs
    # Here we only return a simple code snippet that can be tested by pytest
    await asyncio.sleep(0.1)
    code = '''def add(a: int, b: int) -> int:
    return a + b
'''
    return code
