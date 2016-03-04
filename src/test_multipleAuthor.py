"""
:Description: Testing pytest to ensure proper author tests are picked up
:Reviewer: Some Name
:Author: Module Author

"""

import pytest

pytestmark = [pytest.mark.author("Author1"),
	      pytest.mark.t_area("TEST1"),
	      pytest.mark.req("REQ-0001"),
	      pytest.mark.mat4]


def setup_module():
    """
    :Description: Setup for the module
    """
    pass

def teardown_module():
    """
    :Description: Teardown for module
    """
    pass

@pytest.mark.mat6
@pytest.mark.author("Author2")
@pytest.mark.t_type("Normal")
def test_one():
    """
    Something happens
    """
    pass

@pytest.mark.mat3
@pytest.mark.author("Author3")
@pytest.mark.t_type("Normal")
def test_two():
    """
    Something is wrong
    """
    return False


@pytest.mark.mat6
@pytest.mark.author("Author2")
@pytest.mark.t_type("Normal")

def test_three():
    """
    Something happens
    """
    pass

def test_five():
    """ 
    Something
    """
    pass

def test_alpha():
    """
    Testing other methods of defining pytestmark
    """
    pass

@pytest.mark.mat3
@pytest.mark.author("Author4")
@pytest.mark.t_type("Normal")
def test_four():
    """
    Something is wrong
    """
    return False
