Submoduletest
=============
### Native addon to illustrate issue with node/node-gyp/npm (v0.6.15)

The purpose of this repository is to illustrate an issue (specifically,
issue [3113](https://github.com/joyent/node/issues/3113) with v0.6.15 of node.

Issue Description
-----------------
When building a native addon that includes a vendored C++ library with its
own gyp file, `npm install . -g` will fail to compile the addon, stating
that the library's gyp file does not exist.  This occurs
even though `node-gyp build` can produce a successful build in the
source directory.

Steps to reproduce
------------------
```
$ git clone https://github.com/mattness/submoduletest.git && cd submoduletest

$ node-gyp
  Usage: node-gyp <command> [options]

  where <command> is one of:
    - build - Invokes `make` and builds the module
    - clean - Removes any generated build files and the "out" dir
    - configure - Generates a Makefile for the current module
    - rebuild - Runs "clean", "configure" and "build" all at once
    - install - Install node development files for the specified node version.
    - list - Prints a listing of the currently installed node development files
    - remove - Removes the node development files for the specified version

  for specific command usage and options try:
    $ node-gyp <command> --help

node-gyp@0.3.11  /Users/matt/local/lib/node_modules/node-gyp

$ node --version
v0.6.15

$ npm --version
1.1.16

$ node-gyp configure
info it worked if it ends with ok 
spawn python [ '/Users/matt/.node-gyp/0.6.15/tools/gyp_addon',
  'binding.gyp',
  '-I/Users/matt/projects/submoduletest/build/config.gypi',
  '-f',
  'make' ]
info done ok 

$ node-gyp build
info it worked if it ends with ok 
spawn make [ 'BUILDTYPE=Release', '-C', 'build' ]
  CXX(target) Release/obj.target/something/libsomething/something.o
  LIBTOOL-STATIC Release/something.node
  CXX(target) Release/obj.target/bindings/binding.o
  SOLINK(target) Release/bindings.node
  SOLINK(target) Release/bindings.node: Finished
info done ok 

$ sudo npm install . -g

> submoduletest@0.1.0 install /Users/matt/local/lib/node_modules/submoduletest
> node-gyp rebuild

info it worked if it ends with ok 
spawn python [ '/Users/matt/.node-gyp/0.6.15/tools/gyp_addon',
  'binding.gyp',
  '-I/Users/matt/local/lib/node_modules/submoduletest/build/config.gypi',
  '-f',
  'make' ]
Traceback (most recent call last):
  File "/Users/matt/.node-gyp/0.6.15/tools/gyp_addon", line 38, in <module>
    rc = gyp.main(gyp_args)
  File "/Users/matt/.node-gyp/0.6.15/tools/gyp/pylib/gyp/__init__.py", line 471, in main
    options.circular_check)
  File "/Users/matt/.node-gyp/0.6.15/tools/gyp/pylib/gyp/__init__.py", line 111, in Load
    depth, generator_input_info, check, circular_check)
  File "/Users/matt/.node-gyp/0.6.15/tools/gyp/pylib/gyp/input.py", line 2289, in Load
    depth, check)
  File "/Users/matt/.node-gyp/0.6.15/tools/gyp/pylib/gyp/input.py", line 433, in LoadTargetBuildFile
    includes, depth, check)
  File "/Users/matt/.node-gyp/0.6.15/tools/gyp/pylib/gyp/input.py", line 361, in LoadTargetBuildFile
    includes, True, check)
  File "/Users/matt/.node-gyp/0.6.15/tools/gyp/pylib/gyp/input.py", line 208, in LoadOneBuildFile
    raise Exception("%s not found (cwd: %s)" % (build_file_path, os.getcwd()))
Exception: libsomething/something.gyp not found (cwd: /Users/matt/local/lib/node_modules/submoduletest) while loading dependencies of binding.gyp while trying to load binding.gyp
ERR! Error: `gyp_addon` failed with exit code: 1
    at Array.0 (/Users/matt/local/lib/node_modules/npm/node_modules/node-gyp/lib/configure.js:242:18)
    at EventEmitter._tickCallback (node.js:192:40)
ERR! not ok

npm ERR! submoduletest@0.1.0 install: `node-gyp rebuild`
npm ERR! `sh "-c" "node-gyp rebuild"` failed with 1
npm ERR! 
npm ERR! Failed at the submoduletest@0.1.0 install script.
npm ERR! This is most likely a problem with the submoduletest package,
npm ERR! not with npm itself.
npm ERR! Tell the author that this fails on your system:
npm ERR!     node-gyp rebuild
npm ERR! You can get their info via:
npm ERR!     npm owner ls submoduletest
npm ERR! There is likely additional logging output above.
npm ERR! 
npm ERR! System Darwin 11.3.0
npm ERR! command "node" "/Users/matt/local/bin/npm" "install" "." "-g"
npm ERR! cwd /Users/matt/projects/submoduletest
npm ERR! node -v v0.6.15
npm ERR! npm -v 1.1.16
npm ERR! code ELIFECYCLE
npm ERR! message submoduletest@0.1.0 install: `node-gyp rebuild`
npm ERR! message `sh "-c" "node-gyp rebuild"` failed with 1
npm ERR! errno {}
npm ERR! 
npm ERR! Additional logging details can be found in:
npm ERR!     /Users/matt/projects/submoduletest/npm-debug.log
npm not ok
```

Desired result
--------------
`sudo npm install . -g` installs the submoduletest addon globally without error.
