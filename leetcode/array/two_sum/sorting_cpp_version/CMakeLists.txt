cmake_minimum_required(VERSION 3.14)

Project(TwoSumSort)
configure_file(two_sum.h.in two_sum.h)
add_executable(TwoSum two_sum.cxx)
