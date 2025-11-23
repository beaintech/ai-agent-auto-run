import asyncio
from agents.code_agent import generate_code
from agents.test_agent import generate_tests
from agents.run_agent import run_tests
from agents.repair_agent import repair_code

MAX_RETRY = 3


async def main() -> None:
    task = "Build a simple FastAPI math service with an /add endpoint that optionally rounds the result."
    print("[orchestrator] Starting Agentic Testing System (mock)...")
    print("[orchestrator] Task:", task)

    # 1. Generate initial code (intentionally imperfect)
    code = await generate_code(task)

    # 2. Generate tests based on the task and current code
    tests = await generate_tests(task, code)

    # 3. Run tests + repair loop
    attempt = 0
    while attempt <= MAX_RETRY:
        print(f"[orchestrator] Running tests (attempt {attempt + 1})...")
        success, report = await run_tests(code, tests)

        if success:
            print("[orchestrator] All tests passed. Final version is ready (mock).")
            print("---------- FINAL TEST REPORT ----------")
            print(report)
            break

        print("[orchestrator] Tests failed. Beginning automatic repair...")
        print("---------- FAILING TEST REPORT ----------")
        print(report)

        # 4. Repair code based on failing tests
        code = await repair_code(task, code, tests, report)
        attempt += 1

    if not success:
        print("[orchestrator] Multiple repairs failed. Human intervention required.")
        print("---------- LAST REPORT ----------")
        print(report)


if __name__ == "__main__":
    asyncio.run(main())