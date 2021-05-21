# Set the minimum version of CMake that can be used
# To find the cmake version run
# $ cmake --version
cmake_minimum_required(VERSION 3.5) 

# Set the project name
project (added.out)

# Add an executable
SET(OBJS
  ${CMAKE_CURRENT_SOURCE_DIR}/libs/test.out
)

ADD_EXECUTABLE(added.out ${OBJS} add_code.cpp)

SET_SOURCE_FILES_PROPERTIES(
  ${OBJS}
  PROPERTIES
  EXTERNAL_OBJECT true
  GENERATED true
)
