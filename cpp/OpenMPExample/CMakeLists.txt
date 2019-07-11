cmake_minimum_required(VERSION 2.6)

PROJECT(openMPExample)

SET(CMAKE_BUILD_TYPE "Debug")
#SET(CMAKE_CXX_FLAGS_DEBUG "-O0 -g -Wall -Werror")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
SET(CMAKE_INSTALL_PREFIX /usr)

if(CMAKE_COMPILER_IS_GNUCXX)
    add_definitions("-Wall") 
    if(NOT WIN32)
        add_definitions(-fvisibility="hidden")
    endif(NOT WIN32)
endif(CMAKE_COMPILER_IS_GNUCXX)

SET(SRC
main.cpp
)

ADD_EXECUTABLE(${PROJECT_NAME} ${SRC})

install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION bin)
