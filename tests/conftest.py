from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-15T10:30:00"},
        {"id": 2, "state": "PENDING", "date": "2023-01-10T12:15:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-20T08:45:00"},
        {"id": 4, "state": "CANCELED", "date": "2023-01-05T14:20:00"},
        {"id": 5, "state": "EXECUTED", "date": "2023-01-20T08:45:00"},
    ]
