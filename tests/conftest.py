from typing import Any

import pytest


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": ["authorization"],
    }


@pytest.fixture()
def save_to_tmp():
    """Saves the result object to the filesystem for inspection."""
    def wrapper(output: Any, name: str = "result"):
        with open(f"/tmp/{name}.out.txt", "w") as f:
            f.write(str(output))
    return wrapper
