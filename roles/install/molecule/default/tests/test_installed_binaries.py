import pytest


@pytest.fixture(scope='module', params=['openshift-install'])
def installed_binary(request, host):
    return host.file('/usr/local/bin/{}'.format(request.param))


def test_binary_installed(installed_binary):
    # before making sure the binary is executable for all users,
    # make sure it exists
    assert installed_binary.exists


@pytest.mark.parametrize('mode', ['0o001', '0o010', '0o100'])
def test_binary_executable(installed_binary, mode):
    # param is string so the output makes sense, eval it back to an int
    # input is the three individual execute bits so the test output
    # make it clear which is wrong.
    assert installed_binary.mode & eval(mode)
