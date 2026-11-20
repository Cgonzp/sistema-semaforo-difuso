
import pytest

from src.fuzzy_system import FuzzyTrafficController


@pytest.fixture
def controller():
    return FuzzyTrafficController()


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ((20, 25, 40), 60.00),
        ((90, 50, 10), 104.44),
        ((50, 30, 50), 60.00),
        ((10, 10, 90), 15.56),
    ],
)
def test_calculate_returns_expected_result(controller, inputs, expected):
    result = controller.calculate(*inputs)

    assert isinstance(result, float)
    assert result == pytest.approx(expected, abs=0.01)


@pytest.mark.parametrize(
    "inputs",
    [
        (-1, 25, 40),
        (101, 25, 40),
        (20, -1, 40),
        (20, 61, 40),
        (20, 25, 101),
    ],
)
def test_calculate_rejects_out_of_range_values(controller, inputs):
    with pytest.raises(ValueError):
        controller.calculate(*inputs)


@pytest.mark.parametrize(
    "inputs",
    [
        ("texto", 25, 40),
        (20, float("nan"), 40),
        (20, float("inf"), 40),
        (True, 25, 40),
    ],
)
def test_calculate_rejects_invalid_values(controller, inputs):
    with pytest.raises(ValueError):
        controller.calculate(*inputs)


def test_calculate_supports_multiple_consecutive_calls(controller):
    first_result = controller.calculate(20, 25, 40)
    second_result = controller.calculate(90, 50, 10)

    assert first_result == pytest.approx(60.00, abs=0.01)
    assert second_result == pytest.approx(104.44, abs=0.01)
