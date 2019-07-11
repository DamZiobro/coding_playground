tddCppSkeleton
==============

Skeleton of C++ Test-Driven-Development (TDD) application 

Overview
--------
This script is skeleton of C++ TDD application for usage C++ unit tests based on
CppUTest framework (https://cpputest.github.io/). It allows quickly create own
C++ TDD applications using without wasting time for configuration of build system. 

Prerequisities
--------------
In order to use this skeleton app you need to have installed CppUTest library
in your system. For Debian/Ubuntu operating systems you can easly do it using
following command in your terminal:
```
sudo apt-get install cpputest
```

Build 
-----
Current skeleton has configured build system for sample Calculator application. 
In order to use this build system, you need to got to main directory of the app
and execute following commands: 
```
mkdir build 
cd build 
cmake ..
make
```

Install
-------
In order to install application in your system you need to got o main directory
of the app and execute following commands:
```
cd build 
sudo make install 
```

Usage
-----
After building application you can execute it.
You can do that by going to your build directory and invoking following command
(I assume that you did not changed name of C++ TDD skeleton project): 
```
./src/testTDD
```

If you would like to invoke unit tests for your command you need to invoke
following command: 
```
./tests/testTDD_Tests
```

Code architecture
-----
Main source code of your application should be included in src directory. All
source codes which should be shared between main application and unit tests
executable application shoud be included in LIBRARY_SRC code paths of
src/CMakeLists.txt file. All unit-test-related code is included into tests directory. 

Change project name
-------------------
If you would like to use this C++ TDD skeleton to your own application you only 
need to change PROJECT_NAME variable inside CMakeLists.txt file in main directory
and you can start writing your own TDD

Switch off unit tests (not recommended)
---------------------
If you would like to switch off building unit test application for your C++ TDD
app (it is not recommended as your app will longer not be TDD app) you can use 
following cmake command in your build directory: 
```
cmake -DTESTS=off .. 
```
