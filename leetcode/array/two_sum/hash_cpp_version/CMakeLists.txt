cmake_minimum_required(VERSION 3.10)

# set the project name
project(TwoSum)

#configure_file(two_sum.h.in two_sum.h)
#target_include_directories(Tutorial PUBLIC
#                           "${PROJECT_BINARY_DIR}"
#                           )

# add the executable
add_executable(TwoSumCpp two_sum.cxx)
