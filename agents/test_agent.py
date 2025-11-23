import asyncio
async def generate_tests(task: str, code: str) -> str:
    """
    Simulated test-generation agent.

    In a real system, this agent would inspect `task` and `code` and
    create tests that reflect the expected behaviour.

    Here we:
    - use `task` in a header comment,
    - use `code` (e.g. its length) just to demonstrate that parameters
      are not ignored.
    """
    print("[test_agent] Generating tests for task:", task)
    print("[test_agent] Current code length:", len(code))
    await asyncio.sleep(0.1)

    tests = f'''"""
Auto-generated test suite for task:
{task}

The tests assume a FastAPI app object named `app`
defined in user_code.py.
"""

import math
from fastapi.testclient import TestClient
from user_code import app

client = TestClient(app)


def test_add_basic_integers():
    response = client.get("/add", params={{"a": 1, "b": 2}})
    assert response.status_code == 200
    assert response.json()["result"] == 3


def test_add_basic_floats_no_round():
    response = client.get("/add", params={{"a": 1.1, "b": 2.2}})
    assert response.status_code == 200
    # No rounding requested, expect full precision sum (within a tolerance)
    result = response.json()["result"]
    assert math.isclose(result, 3.3, rel_tol=1e-9)


def test_add_with_round_flag():
    response = client.get("/add", params={{"a": 1.111, "b": 2.222, "do_round": True}})
    assert response.status_code == 200
    # When do_round is True, result should be rounded to 2 decimal places
    result = response.json()["result"]
    assert result == 3.33


def test_add_missing_argument():
    # Missing required query parameter b -> FastAPI should return 422
    response = client.get("/add", params={{"a": 1}})
    assert response.status_code == 422
'''
    return tests

# This will fail because your initial FastAPI code does not throw HTTP 400 if b is missing.