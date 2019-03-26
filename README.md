# BSPZIP-Toe
Cross references VMF contents for clean packing into your BSP!

This python script allows you to specify a VMF file, asset directory and output file to print a list of **ONLY USED ASSESTS** for BSPZIP to use.
![alt text](https://i.imgur.com/ru3CMrD.png)
> *map in above image has 3 custom textures, the file on the right is packed with BSPZIPWalker and the one on the left is packed with BSPZIP-Toe custom asset directory has 1097 files*

# Setup
- Replace "C:\path\to\custom_assets" with the folder that *contains* your materials/models/sound folders

- C:\path\to\BSPZIPTiptoe.exe
  - $path\$file.$ext "C:\path\to\custom_assets" $path\$file-filelist.txt
  
- use the BSPZIP shipped with the game you are working with

- C:\Program Files (x86)\Steam\steamapps\common\yourgamehere\bin\bspzip.exe
  - -addorupdatelist $path\$file.bsp $path\$file-filelist.txt $path\$file.bsp -game $gamedir