# Unit Tests with Python
Trying out __unittest__ and __git__ implementation on Pycharm.

To-do list:
1. [x] Create a new repository and import it on PyCharm
2. [x] Branch out of master
3. [x] Create a library of functions to test
4. [x] Create the tests
5. [x] Add-commit-push to remote
6. [x] Create a Pull Request on GitHub

This is the approach:
* We create single tests under a child-class of `unittest.TestCase`. The tests compare two propositions, if the comparision isn't `True` the test is failed.
* We can have a `setUp(self)` method that is initialized every time before a test is launched.
