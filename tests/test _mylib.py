import os
import sys

import matplotlib.pyplot as plt
import pytest
import seaborn as sns
from pytest_robotframework import keyword
from robot.api import logger

sns.set_theme()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import mylib  # noqa: E402


@keyword
def execute_func():
    return mylib.func()


@pytest.mark.xfail
def test_fail():
    """
    Check how marks are interpreted.
    """
    assert execute_func() != {"hello": "world"}


@pytest.mark.parametrize("image_index", [0, 1])
def test_image(robot_outputdir, function_outputdir, image_index):
    """
    Demonstrate how to include images in HTML logs. We use the ``function_outputdir``
    fixture to define the directory where to write test products.
    """
    _, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
    os.makedirs(function_outputdir, exist_ok=True)
    filename = os.path.join(function_outputdir, f"image_{image_index}.png")
    plt.savefig(filename)
    plt.close()
    logger.info(
        # Note: we use a relative path in the HTML code to make sure that the
        # report won't break if moved to another location on the hard drive
        f'<img src="{os.path.relpath(filename, robot_outputdir)}">',
        html=True,
    )
    assert True


def test_robot_outputdir(robot_outputdir):
    """
    Demonstrate how the Robot output directory is detected and check how warnings
    are logged in the report.
    """
    logger.warn(f"{robot_outputdir = }")
    assert True
