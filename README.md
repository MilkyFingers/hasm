# HASM
Translates hack assembly to machine code

To use the application on a Unix-like system;
1) Copy the files into some directory and run the following commands (at the root of the dir):

   zip hasm.zip *
   
   echo '#!/usr/bin/python3' | cat - hasm.zip > hasm
   
   chmod +x hasm

3) You should now have an exec called hasm that takes a source file foo.asm (in the current directory) and outputs a file foo.hack
4) To make the application accesible from any directory you can copy it into the /usr/local/bin folder on your system
