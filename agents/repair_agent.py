import asyncio

async def repair_code(code: str, report: str) -> str:
    # 在真实系统中，会把 report 丢给 LLM 让它修改代码
    # 这里我们假装“修复”就是返回一个肯定能过的版本
    await asyncio.sleep(0.1)
    fixed_code = '''def add(a: int, b: int) -> int:
    # 修复版：保证返回整数
    return int(a) + int(b)
'''
    return fixed_code
