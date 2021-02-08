# TakeawayAutomation
Project created to cover Takeaway QA Automation Coding Challenge

**Cloning the repo**

The TMDB Takeaway Automation repo having API automation tests for list operations can be cloned from https://github.com/BajajRohan/TakeawayAutomation.git

**Getting started**

To get started, first we need a recent installation of the Python interpreter, which can be downloaded from https://www.python.org/downloads/

**Installing packages**

We would need to install a couple of packages - requests library and pytest which can be done by running the below commands:

pip install -U requests

pip install -U pytest

**Code packages**

**restapi** package: The rest api implementation of the api end points are defined as part of this package

**utils** package: The common utils like generation of reuqest and access tokens are defined as part of this package

**config** package: The test data used for the API automation tests are configurable and defined as part of this package

**api_tests** package: The actual api automation test workflows are defined as part of this package

**Running tests**

The api tests can be run by running the below command from the the cloned repo TakeawayAutomation

pytest -v api_tests/test_list_operations.py

**Logging**

The test logs are recorded as part of the file <test_file_name>.log

**Screenshot of Takeaway tmdb list API tests run**

<img width="1680" alt="Takeaway_test_run" src="https://user-images.githubusercontent.com/3776896/107154205-b0ac6b80-6997-11eb-8ee1-2dcd1153c1dc.png">

