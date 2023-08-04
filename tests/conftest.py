import pytest

from src.channel import Channel


@pytest.fixture(scope="session")
def channel():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')
