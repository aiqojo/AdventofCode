# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2021.2.1\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2021.2.1\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Day_4.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/Day_4.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Day_4.dir/flags.make

CMakeFiles/Day_4.dir/main.cpp.obj: CMakeFiles/Day_4.dir/flags.make
CMakeFiles/Day_4.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Day_4.dir/main.cpp.obj"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\Day_4.dir\main.cpp.obj -c "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\main.cpp"

CMakeFiles/Day_4.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Day_4.dir/main.cpp.i"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\main.cpp" > CMakeFiles\Day_4.dir\main.cpp.i

CMakeFiles/Day_4.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Day_4.dir/main.cpp.s"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\main.cpp" -o CMakeFiles\Day_4.dir\main.cpp.s

# Object files for target Day_4
Day_4_OBJECTS = \
"CMakeFiles/Day_4.dir/main.cpp.obj"

# External object files for target Day_4
Day_4_EXTERNAL_OBJECTS =

Day_4.exe: CMakeFiles/Day_4.dir/main.cpp.obj
Day_4.exe: CMakeFiles/Day_4.dir/build.make
Day_4.exe: CMakeFiles/Day_4.dir/linklibs.rsp
Day_4.exe: CMakeFiles/Day_4.dir/objects1.rsp
Day_4.exe: CMakeFiles/Day_4.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Day_4.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Day_4.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Day_4.dir/build: Day_4.exe
.PHONY : CMakeFiles/Day_4.dir/build

CMakeFiles/Day_4.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Day_4.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Day_4.dir/clean

CMakeFiles/Day_4.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4" "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4" "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\cmake-build-debug" "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\cmake-build-debug" "C:\Users\gian\Documents\AdventofCode\AdventofCode2021\Day 4\cmake-build-debug\CMakeFiles\Day_4.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Day_4.dir/depend
