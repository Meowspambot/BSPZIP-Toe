# BSPZIP-Toe
Cross references VMF contents for clean packing into your BSP!

This python script allows you to specify a VMF file, asset directory and output file to print a list of **ONLY USED ASSESTS** for BSPZIP to use.
![alt text](https://i.imgur.com/ru3CMrD.png)
> *map in above image has 3 custom textures, the file on the left is packed with BSPZIPWalker and the one on the right is packed with BSPZIP-Toe custom asset directory has 1097 files*

Currently only Skyboxs, Textures, Models (including their textures) and Sounds are packed.
- Asset types planed for the future are:
  - csgo radars
  - custom overlays (via env_screenoverlay)

# Setup
get the latest release of [BSPZIP-Toe](https://github.com/Meowspambot/BSPZIP-Toe/releases) and place it in your games bin folder.

Use the following presets if you've never packed your BSP before. But if you already use BSPZIPWalker you can just replace the exe and params with the preset below
- C:\path\to\BSPZIP-Toe.exe
  - $path\$file.$ext "C:\path\to\custom_assets" $path\$file-filelist.txt

Make sure you replace "C:\path\to\custom_assets" with the folder that *contains* your materials/models/sound folders.

- C:\Program Files (x86)\Steam\steamapps\common\yourgamehere\bin\bspzip.exe
  - -addorupdatelist $path\$file.bsp $path\$file-filelist.txt $path\$file.bsp -game $gamedir

use the BSPZIP shipped with the game you are working with its usually located in the games bin folder.
