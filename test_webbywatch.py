import logging
import sys

import pytest

from webbywatch import no_changes_found, check_url


def test_no_changes_found(capsys):
    logger = logging.getLogger()
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    logger.setLevel(logging.INFO)
    logger.addHandler(screen_handler)

    no_changes_found("http://www.example.com")
    out, _ = capsys.readouterr()
    assert out == 'Checked http://www.example.com and found no changes\n'


def test_check_url() :
    assert check_url("https://www.example.com", "Example Domain", False) == False
    assert check_url("https://www.example.com", "Hot Lovin", False) == True