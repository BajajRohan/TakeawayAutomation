import random
import string
import requests
from config.test_data import *


class ListOperations:
    """This class implements logic to implement list operations by calling REST API."""

    def create_list(self, list_headers: str = None):
        """Create list by calling REST API.

        Returns:
            Response object for create list POST request.
        """
        list_name = 'Automated List' + self.random_string(8).lower()
        create_list_payload = "{\"name\":\"%s\",\"iso_639_1\":\"en\"}" % list_name
        return requests.request("POST", url=f'{base_url}/list', headers=list_headers, data=create_list_payload)

    def update_list(self, list_headers: str, list_id: int):
        """Update list by calling REST API.

        Returns:
            Response object for update list PUT request.
        """
        return requests.request("PUT", url=f'{base_url}/list/{list_id}', headers=list_headers, data=update_list_payload)

    def add_item_to_list(self, list_headers: str, list_id: int):
        """Add item to list by calling REST API.

        Returns:
            Response object for add item to list POST request.
        """
        return requests.request("POST", url=f'{base_url}/list/{list_id}/items', headers=list_headers, data=add_item_payload)

    def update_item_in_list(self, list_headers: str, list_id: int):
        """Update item in list by calling REST API.

        Returns:
            Response object for update item in list PUT request.
        """
        return requests.request("PUT", url=f'{base_url}/list/{list_id}/items', headers=list_headers, data=update_item_payload)

    def remove_item_from_list(self, list_headers: str, list_id: int):
        """Remove item from list by calling REST API.

        Returns:
            Response object for remove item from list DELETE request.
        """
        return requests.request("DELETE", url=f'{base_url}/list/{list_id}/items', headers=list_headers, data=update_item_payload)

    def clear_list(self, list_headers: str, list_id: int):
        """Clear list by calling REST API.

        Returns:
            Response object for clear list GET request.
        """
        return requests.request("GET", url=f'{base_url}/list/{list_id}/clear', headers=list_headers)

    def delete_list(self, list_headers: str, list_id: int):
        """Delete list by calling REST API.

        Returns:
            Response object for delete list DELETE request.
        """
        return requests.request("DELETE", url=f'{base_url}/list/{list_id}', headers=list_headers, data={})

    def create_list_invalid_input(self, list_headers: str = None):
        """Create list with invalid input by calling REST API.

        Returns:
            Response object for create list with invalid input POST request.
        """
        return requests.request("POST", url=f'{base_url}/list', headers=list_headers, data={})

    def random_string(self, size: int):
        """Returns a random string of the specified size."""
        return ''.join(random.choice(string.ascii_letters) for _ in range(size))
