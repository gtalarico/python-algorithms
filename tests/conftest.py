import pytest  # noqa
from unittest import mock


@pytest.fixture
def mock_renderer():
    renderer = mock.MagicMock()
    return renderer
