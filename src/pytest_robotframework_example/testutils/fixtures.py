from functools import partial

import pytest

from . import check_plugin


@pytest.fixture
def plugin_checker(request):
    """
    Fixture to check if a pytest plugin is loaded and enabled.

    Examples
    --------
    In a pytest case:

    >>> def test_something(plugin_checker):
    ...     if plugin_checker("robotframework"):
    ...         print("robotframework plugin is loaded and enabled.")
    """
    return partial(check_plugin, request.config)


@pytest.fixture
def has_robot(plugin_checker):
    """
    Fixture that returns ``True`` iff the robotframework plugin is loaded and
    enabled in the current session.
    """
    return plugin_checker("robotframework")
