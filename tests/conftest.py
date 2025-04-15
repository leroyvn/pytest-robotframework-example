import os

import pytest


@pytest.fixture(scope="session")
def robot_outputdir():
    """
    If Robot is installed and the pytest-robotframework plugin is loaded, return
    Robot's output root directory. Otherwise, return None.
    """
    try:
        from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
    except ModuleNotFoundError:
        return None

    try:
        return BuiltIn().get_variable_value("${OUTPUT DIR}")
    except RobotNotRunningError:
        return None


@pytest.fixture(scope="function")
def function_outputdir(robot_outputdir, request):
    """
    Generate an output directory for the current test case.
    """
    rootdir = robot_outputdir if robot_outputdir is not None else request.config.rootdir
    return os.path.join(rootdir, request.node.name)
