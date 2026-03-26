import sys
import os
from unittest.mock import patch
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from hello import main


def test_main_prints_greeting_with_datetime(capsys):
    fake_now = datetime(2026, 1, 15, 10, 30, 0)
    with patch("hello.datetime") as mock_dt:
        mock_dt.now.return_value = fake_now
        main()
    output = capsys.readouterr().out
    assert "Hello!" in output
    assert "2026-01-15 10:30:00" in output
