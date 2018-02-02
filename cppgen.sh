#!/bin/bash

mkdir $1
cd $1

mkdir sources
mkdir debug

echo 'cmake_minimum_required (VERSION 3.9)' >> CMakeLists.txt
echo "project($1)" >> CMakeLists.txt
echo "set(CMAKE_CXX_STANDARD 11)" >> CMakeLists.txt
echo 'aux_source_directory(./sources/ DIR_SRC)' >> CMakeLists.txt
echo 'set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ./debug/)'>> CMakeLists.txt
echo "add_executable($1 \${DIR_SRC})">> CMakeLists.txt


echo "cmake . && make && echo '========================' && ./debug/$1" >> running.sh
chmod +x running.sh

echo '#include<iostream>' >> main.cpp
echo 'using namespace std;' >> main.cpp
echo -e  >> main.cpp
echo "int main()" >> main.cpp
echo "{" >> main.cpp
echo '    cout<<"Hello World !"<<endl;' >> main.cpp
echo "}">>main.cpp

mv main.cpp ./sources

