# Notes


- why is namespace `__name__ __main__` created  ?
- `w+` ?
- `r` ?
- http://127.0.0.1:5000 ?
- how to navigate to `bin` dir?

### Tips

##### Vim commands

`i` - insert

`yy` - yank (copy)

`p` - paste

`dd` - delete current line


##### dev env errors

- xcode needs to be updated

- python installed but not linked, run `brew link python3`
- Error `Error: Permission denied @ dir_s_mkdir - /usr/local/Frameworks`
- check permissions, run  `ls -lh /usr/local`
- change permissions, run `sudo mkdir /usr/local/Frameworks` then `sudo chown $(whoami):admin /usr/local/Frameworks`
- run `brew link python3` again. Result `Linking /usr/local/Cellar/python/3.7.3... 1 symlinks created`

- run `pipenv shell`

##### hidden branches 😩 

 - run, `git branch -a`
 
 #### test
 
 each one is isolated, so basically nothing is created and carried over to the next test.
 
 the number in the tests
 
 - must define the route
 - must delete the file
 - must return user feedback
 - must get json data to get name etc
 - find out how to delete py files
 - must read the test and check every other tests and requests etc.
 
 
 # must remember!
 
 the api never makes requests, only handles it!!
 
 in this app the tests act as the user and therefore try out each end point 
 
 must import os module, use this to delete
 
