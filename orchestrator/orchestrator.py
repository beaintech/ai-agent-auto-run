import asyncio
from agents.code_agent import generate_code
from agents.test_agent import generate_tests
from agents.run_agent import run_tests
from agents.repair_agent import repair_code

MAX_RETRY = 3

async def main():
    print("Starting Agentic Parallel Testing System (mock)...")

    # 1. Generate code
    code = await generate_code("build a simple math API with FastAPI")

    # 2. Generate tests
    tests = await generate_tests(code)

    # 3. Run tests
    success, report = await run_tests(code, tests)

    retry = 0
    while not success and retry < MAX_RETRY:
        print(f"Tests failed, starting automatic repair attempt {retry + 1}...")
        code = await repair_code(code, report)
        success, report = await run_tests(code, tests)
        retry += 1

    if success:
        print("All tests passed, ready for submission (mock).")
    else:
        print("Multiple repairs failed, human intervention required.")
        print("Final report:")
        print(report)

if __name__ == "__main__":
    asyncio.run(main())
