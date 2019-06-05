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
