from unittest.mock import patch
from src.get_any_url import get_url
import requests


def test_get_url_with_200():
    # Arrange
    test_url = 'https://notachancethisisarealurl.com'
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html><p>Hello World</p></html>'
        # Act
        response = get_url(test_url)
        # Assert
        assert response.status_code == 200
        assert response.text == '<html><p>Hello World</p></html>'
        mock_get.assert_called_once_with(test_url)


def test_get_url_with_404():
    # Arrange
    test_url = 'https://notachancethisisarealurl.com'
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = (
            requests.exceptions.HTTPError('404')
        )
        # Act
        response = get_url(test_url)
        # Assert
        assert response == 'HTTP error occurred: 404'
