import asyncio

async def generate_code(task: str) -> str:
    # 在真实系统中，这里会调用 Claude / Cursor / 其他 LLM API
    # 这里我们只返回一段可以被 pytest 测的简单代码
    await asyncio.sleep(0.1)
    code = '''def add(a: int, b: int) -> int:
    return a + b
'''
    return code
