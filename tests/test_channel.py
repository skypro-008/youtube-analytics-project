from src.channel import Channel
import pytest


@pytest.fixture()
def expl1():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


def test_channel_init(expl1):
    assert expl1.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'


def test_print_info(expl1):
    assert expl1.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'


def test_to_json():

    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert vdud.to_json('vdud.json')== None