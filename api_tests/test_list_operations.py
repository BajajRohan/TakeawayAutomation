import json
import logging
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.token import Token
from config.test_data import *
from restapi.list_operations import ListOperations
from selenium.webdriver.support import expected_conditions as EC

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename=__name__+'.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class TestListOperations:
    """This class implements api tests for TMDB list operations."""

    def setup_class(self):
        """Setup method for list api tests"""
        self.token_obj = Token()
        self.request_token_response = self.token_obj.generate_request_token()
        self.request_token = json.loads(self.request_token_response.text)['request_token']
        self.list_operations = ListOperations()

    def teardown_class(self):
        """Teardown method for list api tests"""
        try:
            logger.info('Removing list %s after test run' % list_id)
            delete_list_response = self.list_operations.delete_list(list_headers, list_id)
            assert delete_list_response.status_code == 200, 'Delete list operation failed'
            delete_list_response_text = json.loads(delete_list_response.text)
            assert delete_list_response_text['status_message'] == 'The item/record was deleted successfully.', 'Delete list status message mismatch'
        except Exception as e:
            logger.error('Exception encountered while deleting list %s' % e)

    def test_create_request_token(self):
        """Test to verify request token generation"""
        try:
            logger.info('Test to verify request token generation')
            assert self.request_token_response.status_code == 200, 'token generation failed'
            access_token_response_text = json.loads(self.request_token_response.text)
            assert access_token_response_text['status_message'] == 'Success.', 'Create request token status message mismatch'
        except Exception as e:
            logger.error('Exception encountered while generating request token %s' % e)

    def test_approve_request_token(self):
        """Test to approve request token via UI"""
        logger.info('Test to approve request token via UI')
        driver = webdriver.Chrome(f'{os.getcwd()}/lib/chromedriver')
        driver.get(f'{moviedb_ui_url}/login')
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('login_button').click()
        driver.get(f'{moviedb_ui_url}/auth/access?request_token={self.request_token}')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.k-button.k-primary')))
        driver.find_element_by_class_name('k-button.k-primary').click()

    def test_create_access_token(self):
        """Test to verify access token generation"""
        try:
            logger.info('Test to verify access token generation')
            access_token_response = self.token_obj.generate_access_token(self.request_token)
            access_token = json.loads(access_token_response.text)['access_token']
            global list_headers
            list_headers = {'authorization': f'Bearer {access_token}',
                            'content-type': 'application/json;charset=utf-8'}
            assert access_token_response.status_code == 200, 'token generation failed'
            access_token_response_text = json.loads(access_token_response.text)
            assert access_token_response_text['status_message'] == 'Success.', 'Create access token status message mismatch'
        except Exception as e:
            logger.error('Exception encountered while generating access token %s' % e)

    def test_create_list(self):
        """Test to verify list creation"""
        try:
            logger.info('Test to verify list creation')
            create_list_response = self.list_operations.create_list(list_headers)
            assert create_list_response.status_code == 201, 'Create list operation failed'
            create_list_response_text = json.loads(create_list_response.text)
            assert create_list_response_text['status_message'] == 'The item/record was created successfully.', 'Create list status message mismatch'
            global list_id
            list_id = create_list_response_text['id']
            logger.info('List with id %s created' % list_id)
        except Exception as e:
            logger.error('Exception encountered while creating list %s' % e)

    def test_update_list(self):
        """Test to verify list updation"""
        try:
            logger.info('Test to verify list updation')
            update_list_response = self.list_operations.update_list(list_headers, list_id)
            assert update_list_response.status_code == 201, 'Update list operation failed'
            update_list_response_text = json.loads(update_list_response.text)
            assert update_list_response_text['status_message'] == 'The item/record was updated successfully.', 'Update list status message mismatch'
        except Exception as e:
            logger.error('Exception encountered while updating list %s' % e)

    def test_add_item_to_list(self):
        """Test to verify addition of items to list"""
        try:
            logger.info('Test to verify addition of items to list')
            add_item_response = self.list_operations.add_item_to_list(list_headers, list_id)
            assert add_item_response.status_code == 200, 'Addition of item to list operation failed'
            add_item_response_text = json.loads(add_item_response.text)
            assert add_item_response_text['status_message'] == 'Success.', 'Addition of items to list status message mismatch'
        except Exception as e:
            logger.error('Exception encountered while adding item to list %s' % e)

    def test_update_list_item(self):
        """Test to verify updation of an item in the list"""
        try:
            logger.info('Test to verify updation of an item in the list')
            add_item_response = self.list_operations.update_item_in_list(list_headers, list_id)
            assert add_item_response.status_code == 200, 'Updation of item to list operation failed'
            add_item_response_text = json.loads(add_item_response.text)
            assert add_item_response_text['status_message'] == 'Success.', 'Updation of list item status message mismatch'
        except Exception as e:
            logger.error('Exception encountered while updating list item %s' % e)

    def test_remove_item_from_list(self):
        """Test to verify removal of items from list"""
        try:
            logger.info('Test to verify removal of items from list')
            add_item_response = self.list_operations.remove_item_from_list(list_headers, list_id)
            assert add_item_response.status_code == 200, 'Deletion of item to list operation failed'
            add_item_response_text = json.loads(add_item_response.text)
            assert add_item_response_text['status_message'] == 'Success.', 'Removal of list items status message mismatch'
        except Exception as e:
            logger.error('Exception encountered while removing item from list %s' % e)

    def test_clear_list(self):
        """Test to verify clearing of list"""
        try:
            logger.info('Test to verify clearing of list')
            clear_list_response = self.list_operations.clear_list(list_headers, list_id)
            assert clear_list_response.status_code == 200, 'Clear list operation failed'
            clear_list_response_text = json.loads(clear_list_response.text)
            assert clear_list_response_text['status_message'] == 'Success.', 'Clear list status message mismatch'
        except Exception as e:
            logger.error('Exception encountered while updating list %s' % e)

    def test_create_list_invalid_input(self):
        """Test to verify creation of list with invalid input"""
        try:
            logger.info('Test to verify creation of list with invalid input')
            create_workflow_response = self.list_operations.create_list_invalid_input(list_headers)
            assert create_workflow_response.status_code == 422, 'Create workflow operation with invalid input expected to fail'
        except Exception as e:
            logger.error('Exception encountered during creation of list with invalid input %s' % e)

    def test_create_list_invalid_header(self):
        """Test to verify list creation with invalid header"""
        try:
            logger.info('Test to verify list creation with invalid header')
            create_workflow_response = self.list_operations.create_list()
            assert create_workflow_response.status_code == 401, 'Create list operation with invalid header expected to fail'
        except Exception as e:
            logger.error('Exception encountered during creation of list with invalid header %s' % e)
