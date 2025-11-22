import asyncio
import os
import subprocess
from tempfile import TemporaryDirectory

async def run_tests(code: str, tests: str):
    # Simulate a complete code and test run using a temporary directory.    await asyncio.sleep(0.1)
    with TemporaryDirectory() as tmpdir:
        target_path = os.path.join(tmpdir, "target.py")
        test_path = os.path.join(tmpdir, "test_target.py")

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(code)

        with open(test_path, "w", encoding="utf-8") as f:
            f.write(tests)

        # run pytest
        try:
            result = subprocess.run(
                ["pytest", "-q", test_path],
                cwd=tmpdir,
                capture_output=True,
                text=True,
                timeout=10
            )
            success = result.returncode == 0
            report = result.stdout + "\n" + result.stderr
            return success, report
        except Exception as e:
            return False, str(e)
