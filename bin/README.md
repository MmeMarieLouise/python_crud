### The `./bin/test` script explained, line by line.

#### Line 1: `#!/bin/bash`

The first 2 characters (`#!`) are called a 'shebang'. They are used in shell-executed scripts to indicate that the rest of this line is _not code
to be executed_ but rather to set what kind of language is going to be used in the rest of the file so that the right interpreter can be used.

The `/bin/bash` bit afterwards therefore says that this is a file which contains Bash script (basically the same language that you can type as commands
in your terminal) and that the language should be interpreted accordingly.

There is actually a file at the `/bin/bash` location, which is the Bash executable used to run/interpret/execute/etc the rest of the code in the file. You
can do `file /bin/bash` or `ls /bin/bash` to see this in your terminal.


#### Line 4: `DEBUG_MODE=$1`

Here we are setting a variable `DEBUG_MODE` with the value contained in another variable `$1`. In Bash all variables/parameters passed to functions or
programs immediately get assigned to numbered variables.

For example, say you had a program called `cake` which looked like this:

```sh
#!/bin/bash

echo 'The first argument is:' $1
echo 'The second argument is:' $2
```

When I execute that program on the command-line, it would behave like this:

```
$ ./cake chocolate red-velvet
The first argument is: chocolate
The second argument is: red-velvet
```

You can copy `cake` into a file and run it a couple of times to see how it works (don't forget to `chmod +x` the filename to make it executable).
You can use `$3`, `$4` etc to get further arguments.

So on line 2 of our test script, we will assign the first argument passed into the script when it is executed to another variable: one with an easier name
to see than `1`.

#### Line 6-13:

```sh
if [ -z "$DEBUG_MODE" ]; then
  # if in debug mode, start the server, redirect all output
  # away from terminal, and run in background
  python api.py &>/dev/null &
else
  # else, start the server and run in background
  python api.py &
fi
```

Here we have a Bash if/else loop. The standard pattern is `if <blah is true>; then <do one thing>; else <do something else>; fi`. You can write Bash
all on one line like this, but as you can see it gets messy, so it is nice to use some tabbing to keep it readable.

The thing we are checking is true here, is whether the `$DEBUG_MODE` variable does not have a value (when setting a variable in Bash, it doesn't need any punctuation,
when using or checking the variable, you throw a `$` at the beginning). The `-z` flag will return `true` if `$DEBUG_MODE` has **not** been set.

If that is the case then we start our server with `python api.py` _but_ with a little extra thrown on. Since `DEBUG_MODE` is off, we want to run our server quietly.
The `&>` bit says to redirect all server output from the terminal to somewhere else, so that we don't see it printed on the screens, making our test look all messy.
The 'somewhere else' is `/dev/null` which is just a special kind of file where you can send output you don't care about. It is essentially the void. So together `&>/dev/null`
means that all output from the running server should be thrown into the void because we don't care about it.

The very last character `&` makes sure that the server is started _in the background_. This is important, because when you run the server manually in the terminal
(just type `python api.py` in your `pipenv shell`) you will see that it starts... and just sits there until you `ctrl-c` it. We don't want this script to hang forever
at this point, never actually running our tests, so we set the server in the background so that the next lines start running in the foreground.

Our alternative action after the `else` happens when `$DEBUG_MODE` **has** been set. This means we don't want to send server output to the void: we actually
want to see problems when they happen and everything will be printed to the terminal. The command to start the server is the same, and we still want it to run in
the background using `&` so that it doesn't bring everything to a stop.

#### Line 16: `pytest`

This is self-explanatory. It runs the test suite against the server we started on either Line 9 or Line 12.

#### Line 20

```sh
ps aux | awk '/\/api.py/ {print $2}' | xargs kill -9 &>/dev/null
```

Finally on the last line, we are ensuring that the server is killed at the end of the test run. If we don't kill the server, then the next time
we try to use this script to run our tests, the line to start the server will fail since there will already be one active on that port.

`ps aux` gets a list of all running processes. You can run this on your terminal, there might be a lot.

We pipe (`|`, take the _output_ of the command on the left and use it as the _input_ to the command on the right) that result to `awk` which we can use to
filter only our `api.py` server (`awk '/\/api.py/'`). You can play around with this in your terminal. For example, filter only the Chrome related processes
by doing `ps aux | awk '/Chrome/'` (use a different keyword if Chrome is not your browser). 

After filtering for our server, we can then print out certain columns of the `ps aux` output. If you are on a small screen you may not be able to see them, but
there are columns! They are numbered as `$` variables. We want the PID (process ID) for our server, which I happen to know is in column 2: `awk '/\/api.py/ {print $2}'`.
You can play with your Chrome filter to see this: `ps aux | awk '/Chrome/ {print $2}'`. If you have more than one tab open you will probably have a lot of PIDs. You can
change the `$` variable number from 2 to something else to focus on different columns.

Then we send the PID we got from `awk` through another pipe `|` to a thing called `xargs`. `xargs` basically says "I will take the output from the command on the left
(ie; our PID), and use it as an _argument_ (different an input) for the command on my right". The command on the right is `kill -9`, which is what you
use if you want to kill a process dead right now, no questions asked. We would usually run `kill -9 <pid we know about>`, but this time `xargs` has
been told the PID we want, so it will fill in that gap for us: `xargs kill -9`. You may want to skip testing that on your Chrome filter unless you want it to quit immediately.

Finally the last section of that line is one you may recognise: `&>/dev/null`. We send all output from that `kill` command into the void
so it doesn't mess up our pretty test output. `kill` is a silent command when it succeeds, but since we are indiscriminately killing all PIDs (probably no more than 5) which
match the pattern, we may turn up some which don't exist by the time the kill runs. For example, the very section which filters for `api.py` will be a running process
which has a PID. This PID will get added to the list of PIDs to kill, but of course once the filter has finished, the process dies, so there is nothing to kill.
We don't want to hear about `kill` failing on that, so we send it to the void.

You can see this by doing `ps aux | awk '/hello/'` and you will see the `awk /hello/` search as a process. If you try to kill it after searching
(`ps aux | awk '/hello/ {print $2}' | xargs kill -9`) it will fail to do so because it already died by itself.

