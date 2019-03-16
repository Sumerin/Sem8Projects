cmake_minimum_required(VERSION 3.13)
project(zad2)

set(CMAKE_CXX_STANDARD 98)

add_executable(zad2 SimpleGraph.c)

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
target_link_libraries(zad2 ${PYTHON_LIBRARIES})
