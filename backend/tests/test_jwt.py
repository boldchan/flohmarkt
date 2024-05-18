from datetime import datetime
from datetime import timezone
from unittest.mock import patch

import core.security
from core.security import create_access_token


def test_create_access_token(monkeypatch):
    class MockSetting:
        SECRET_KEY = "a_secret"
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = 10

    monkeypatch.setattr("core.security.settings", MockSetting())
    with patch("core.security.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(
            2024, 5, 18, 13, 8, 2, 277569, tzinfo=timezone.utc
        )

        assert core.security.datetime.now() == datetime(
            2024, 5, 18, 13, 8, 2, 277569, tzinfo=timezone.utc
        )

        test_data = {"sub": "someemai1@gmai1.com"}
        expected = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzb21lZW1haTFAZ21haTEuY29tIiwiZXhwIjoxNzE2MDM4MjgyfQ.hFRUCqIMu12ns8OukQiZ5NFyxLdeZcWULnL_1UyzMi0"
        assert create_access_token(test_data) == expected
