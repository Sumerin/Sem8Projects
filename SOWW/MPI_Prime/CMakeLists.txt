cmake_minimum_required(VERSION 3.14)
project(SOWW)

find_package(MPI REQUIRED)

include_directories(${MPI_INCLUDE_PATH})

set(CMAKE_CXX_STANDARD 14)

add_executable(SOWW main.cpp)
target_link_libraries(SOWW ${MPI_LIBRARIES})

if(MPI_COMPILE_FLAGS)
    set_target_properties(SOWW PROPERTIES
            COMPILE_FLAGS "${MPI_COMPILE_FLAGS}")
endif()

if(MPI_LINK_FLAGS)
    set_target_properties(SOWW PROPERTIES
            LINK_FLAGS "${MPI_LINK_FLAGS}")
endif()