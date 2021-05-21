# Set the minimum version of CMake that can be used
# To find the cmake version run
# $ cmake --version
cmake_minimum_required(VERSION 3.5) 

# Set the project name
project (added.out)

# Add an executable
add_executable(added.out add_code.cpp)

target_link_libraries(added.out ${CMAKE_CURRENT_SOURCE_DIR}/libs/test.out)