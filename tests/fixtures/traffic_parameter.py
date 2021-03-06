import pytest


@pytest.fixture
def default():
    return {
        'weekday_schedule': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.7, 0.9, 0.9, 0.6,
                             0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.8,
                             0.7, 0.3, 0.2, 0.2],
        'saturday_schedule': [0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.5, 0.5, 0.5, 0.5,
                              0.5, 0.5, 0.5, 0.5, 0.6, 0.7, 0.7, 0.7, 0.7, 0.5,
                              0.4, 0.3, 0.2, 0.2],
        'sunday_schedule': [0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.4, 0.4, 0.4, 0.4,
                            0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
                            0.3, 0.3, 0.2, 0.2]
    }


@pytest.fixture
def correct():
    return {
        'sensible_heat': 5,
        'weekday_schedule': [0.1, 0.1, 0.1, 0.1, 0.2, 0.4, 0.7, 0.9, 0.9, 0.6,
                             0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.8,
                             0.7, 0.3, 0.2, 0.2],
        'saturday_schedule': [0.5, 0.1, 0.1, 0.1, 0.2, 0.4, 0.7, 0.9, 0.9, 0.6,
                              0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.8,
                              0.7, 0.3, 0.2, 0.2],
        'sunday_schedule': [0.6, 0.1, 0.1, 0.1, 0.2, 0.4, 0.7, 0.9, 0.9, 0.6,
                            0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.8,
                            0.7, 0.3, 0.2, 0.2]
    }


@pytest.fixture
def incorrect():
    return {
        'sensible_heat': 'ten',
        'too_short': [0.1, 0.1, 0.1, 0.1, 0.2, 0.4, 0.7, 0.9, 0.9, 0.6,
                      0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.8,
                      0.7, 0.3],
        'too_long': [0.5, 0.1, 0.1, 0.1, 0.2, 0.4, 0.7, 0.9, 0.9, 0.6,
                     0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.8,
                     0.7, 0.3, 0.2, 0.2, 0.3, 0.2],
        'non_fractional': [0.6, 0.1, 0.1, 0.1, 0.2, 0.4, 0.7, 0.9, 0.9, 0.6,
                           0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9, 0.9, 0.8, 0.8,
                           0.7, 0.3, 0.2, 2]
    }
