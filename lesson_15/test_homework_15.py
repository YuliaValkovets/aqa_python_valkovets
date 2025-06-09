import pytest

from lesson_15.homework_15 import romb, Rhombus


@pytest.mark.parametrize('value',[1,100,10000])
def test_side_a_valid_length(value):
    romb = Rhombus()
    romb.side_a = value
    assert value == romb.side_a

@pytest.mark.parametrize('value', [-150, -1, 0])
def test_side_a_invalid_length(value):
    with pytest.raises(ValueError) as exp_info:
        romb = Rhombus()
        romb.side_a = value
    assert str(exp_info.value) == 'The length of the side must be greater than 0'


@pytest.mark.parametrize('value', [1, 90, 179])
def test_angle_b_valid_value(value):
    romb = Rhombus()
    romb.angle_a = value
    assert value == romb.angle_a


@pytest.mark.parametrize('value', [-1, 0, 180, 200])
def test_angle_b_invalid_value(value):
    with pytest.raises(ValueError) as exp_info:
        romb = Rhombus()
        romb.angle_a = value
    assert str(exp_info.value) == 'The angle "a" should be between 0 and 180'


@pytest.mark.parametrize('value_a, value_b',[
    (1,179),
    (90,90),
    (179, 1)
])
def test_right_calc_angle_b(value_a, value_b):
    romb = Rhombus()
    romb.angle_a = value_a
    assert value_b == romb.angle_b


def test_angle_b_cannot_be_set_manually():
    with pytest.raises(AttributeError) as exp_info:
        romb = Rhombus()
        romb.angle_b = 80
    assert str(exp_info.value) == 'The angle "b" should be set automatically'

