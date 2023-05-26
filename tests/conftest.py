""" Conftest module"""
import pytest

from src.channel import Channel


@pytest.fixture
def channel():
    """Create a Channel instance with a sample channel ID"""
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')
