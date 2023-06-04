import os

import pytest
from src.channel import Channel

API_KEY = os.getenv('API_KEY')

@pytest.fixture
def id():
    return 'UCMCgOm8GZkHp8zJ6l7_hIuA'



