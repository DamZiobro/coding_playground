cmake_minimum_required(VERSION 2.6)

ENABLE_TESTING()

FIND_PACKAGE(GTest REQUIRED) 
INCLUDE_DIRECTORIES(${GTEST_INCLUDE_DIRS})
INCLUDE_DIRECTORIES(${GMOCK_INCLUDE_DIRS})

# sources exclusive for test executables
SET(SRC
    TennisTest.cpp
)

message ("     ---> Configuring unit tests executables: ${TEST_PROJECT_NAME}")
ADD_EXECUTABLE(${TEST_PROJECT_NAME} ${SRC})
TARGET_LINK_LIBRARIES(${TEST_PROJECT_NAME} ${GTEST_BOTH_LIBRARIES} gmock gmock_main pthread testTDDLib)

ADD_TEST(test ${TEST_PROJECT_NAME})
add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND}
  DEPENDS ${TEST_PROJECT_NAME})

