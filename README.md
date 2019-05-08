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

### Interacting with the webservice

Using `[curl](https://www.lifewire.com/example-uses-of-the-linux-curl-command-4084144)`:

```sh
# in one terminal window
$ python api.py

# in another terminal window
$ curl -X POST localhost:5000/create --data '{"path":"~/crud-files","name":"test-file","contents":"hello"}'
Entry 'test-file' created.
$ echo $?
0
$ ls $HOME/crud-files/
test-file
$ cat $HOME/crud-files/test-file
hello

$ curl localhost:5000/read --data '{"path":"~/crud-files","name":"test-file"}'
hello

$ curl -X POST localhost:5000/update --data '{"path":"~/crud-files","name":"test-file","contents":"goodbye"}'
Entry 'test-file' updated.
$ echo $?
0
$ cat $HOME/crud-files/test-file
goodbye

$ curl localhost:5000/delete --data '{"path":"~/crud-files","name":"test-file"}'
Entry 'test-file' deleted.
$ echo $?
0
$ ls $HOME/crud-files/

```

### Development

- Environment and dependencies managed by [`pipenv`](https://docs.pipenv.org/en/latest/).
  - Install `pipenv`: `pip3 install pipenv` or `brew install pipenv`
  - To install deps from existing `Pipfile`: `pipenv install`
  - To enter dev environment: `pipenv shell`
  - To install new project dependency: `pipenv install <dep>` (`--dev` for eg test package)

- To run tests (in the `pipenv shell`): `pytest`
