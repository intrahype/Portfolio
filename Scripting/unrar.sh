#!/bin/bash

#replace source and new directories with local directories before use
#-execdir refers to executing command in defined directory

#must have unrar package installed | sudo apt-get install unrar
#e means extract in current directory
#-o- means do not overwrite already created files


find source_dir/ -name '*.rar' -execdir unrar e -o- {} /new/destination_dir/ \; 