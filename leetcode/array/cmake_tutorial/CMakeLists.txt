cmake_minimum_required (VERSION 3.14)
project (Demo)

# Adds the Sources subfolder of the Yoctopuce C++ library.
add_subdirectory (yoctolib_cpp/Sources/ compiled_yoctolib)
add_executable (demo dummy_code.cxx)

# Links the executable to the Yoctopuce C++ library (YoctoLib).
target_link_libraries (demo LINK_PUBLIC YoctoLib)
