#==============================================================================
#Damian Ziobro - Object Tracking build script

cmake_minimum_required(VERSION 2.6)
project(cpp11FeaturesTest)

set(CMAKE_INSTALL_PREFIX /usr)
ADD_DEFINITIONS(-std=c++11 -pthread)

#source of project
set(SRC

#cpp11FeaturesTest.cpp
promiseTest.cpp
)

#==============================================================================
#compilation and installation project

add_executable(${PROJECT_NAME} ${SRC})
install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION bin)

#==============================================================================
