cmake_minimum_required(VERSION 3.13)
project(Zad1 C)

set(CMAKE_C_STANDARD 11)

include_directories(.)
configure_file( Test_data Test_data COPYONLY)

add_executable(Zad1
        main.c)
