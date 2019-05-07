# python_crud

## Simple CRUD api to practice Python

A rest webservice in Python that can operate over text files as resources.

**Minimum requirements**:

  - [ ] Create a text file with some contents stored in a given path.
  - [ ] Read the contents of a text file under the given path.
  - [ ] Update the contents of a text file.
  - [ ] Delete the file that is stored under a given path.
 
 
**Further capabilities**:

  - [ ] If no path is given, a default path under system temp will be used.
  - [ ] Retrieve the total number of files in the given path.
  - [ ] Retrieve the average characters per file.
  - [ ] Retrieve the average word length per file.
  - [ ] Retrieve the total number of bytes in the given path.


**Ensuring that**:

  - [ ] Full test coverage.
  - [ ] Code is refactored and readable.


### Development

- Environment and dependencies managed by [`pipenv`](https://docs.pipenv.org/en/latest/).
  - Install `pipenv`: `pip3 install pipenv` or `brew install pipenv`
  - To install deps from existing `Pipfile`: `pipenv install`
  - To create new project env: `pipenv --three`
  - To enter dev environment: `pipenv shell`
  - To install new project dependency: `pipenv install <dep>` (`--dev` for eg test package)

- To run tests (in the `pipenv shell`): `pytest`
