# It's only can be used in linux
import sys
import os
import stat

project_name = sys.argv[1]

os.mkdir(project_name)
os.chdir(project_name)
os.mkdir('sources')
os.mkdir('debug')


cmakelists = """cmake_minimum_required (VERSION 3.9)
project({%s})
set(CMAKE_CXX_STANDARD 11)
aux_source_directory(./sources/ DIR_SRC)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ./debug/)
add_executable(run ${DIR_SRC})
""" % (project_name)
with open('CMakeLists.txt', 'w') as fcmake:
    fcmake.write(cmakelists)


runc = "cmake . && make && echo '======================' && ./debug/run "
with open('running.sh', 'w') as frun:
    frun.write(runc)
os.chmod('./running.sh', stat.S_IRWXU)


main_content = """#include<iostream>
using namespace std;

int main()
{
    cout<<"Hello World !"<<endl;
}
"""
with open('./sources/main.cpp', 'w') as ff:
    ff.write(main_content)
