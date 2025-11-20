import asyncio

async def generate_tests(code: str) -> str:
    # 在真实系统中，这里会分析 code 并自动生成测试
    await asyncio.sleep(0.1)
    tests = '''import pytest
from target import add

def test_add_positive():
    assert add(1, 2) == 3

def test_add_zero():
    assert add(0, 5) == 5
'''
    return tests
