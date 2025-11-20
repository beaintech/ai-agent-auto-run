import asyncio
from agents.code_agent import generate_code
from agents.test_agent import generate_tests
from agents.run_agent import run_tests
from agents.repair_agent import repair_code

MAX_RETRY = 3

async def main():
    print("🚀 启动 Agentic 并行测试系统 (mock)...")

    # 1. 生成代码
    code = await generate_code("build a simple math API with FastAPI")

    # 2. 生成测试
    tests = await generate_tests(code)

    # 3. 运行测试
    success, report = await run_tests(code, tests)

    retry = 0
    while not success and retry < MAX_RETRY:
        print(f"❌ 测试失败，开始第 {retry + 1} 次自动修复...")
        code = await repair_code(code, report)
        success, report = await run_tests(code, tests)
        retry += 1

    if success:
        print("✅ 所有测试通过，可以提交（mock）。")
    else:
        print("⚠️ 多次修复失败，请人工介入。")
        print("最终报告：")
        print(report)

if __name__ == "__main__":
    asyncio.run(main())
