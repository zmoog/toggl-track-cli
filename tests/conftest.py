from typing import Any

import pytest
from click.testing import Result


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": ["authorization"],
    }


@pytest.fixture()
def save_to_tmp():
    """Saves the result object to the filesystem for inspection."""
    def wrapper(output: Any):
        with open("/tmp/output.txt", "w") as f:
            f.write(str(output))
    return wrapper
