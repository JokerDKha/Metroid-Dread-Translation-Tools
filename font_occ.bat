python3 .\tools\scripts\font.py create --ttf-path "fonts\LexendGiga-Bold.ttf" --charset-path ".\temp\us_english.txt" --gtbl-path ".\temp\occ_glyphtable.buct" --bfnt-path-fmt ".\temp\occ_{}.bfont" --mtxt-path ".\temp\occ_atlas.bctex" --mtxt-width 4096 --mtxt-height 2048 --gtbl-path-ingame "system/fonts/symbols/occ_glyphtable.buct" --mtxt-path-ingame "system/fonts/textures/occ_atlas.bctex" --18 .\temp\us_english.txt --18-useicon --30 .\temp\us_english.txt --30-useicon --38 .\temp\us_english.txt --38-useicon --50 .\temp\us_english.txt 
.\tools\bin\mtxttool.exe -ig .\temp\occ_atlas.png -t .\temp\occ_atlas.bctex .\temp\origin\Romfs\textures\system\fonts\textures\chc_atlas.bctex
python3 .\tools\scripts\btxt.py -cb us_english.txt -p %cd%\temp\us_english.txt

set FONTDIR=temp\010093801237C000\romfs\system\fonts
set TEXTDIR=temp\010093801237C000\romfs\system\localization
set SYMDIR=%FONTDIR%\symbols
set TEXDIR=temp\010093801237C000\romfs\textures\system\fonts\textures
set PATCHDIR=Patch-Translation
md %SYMDIR%
md %TEXDIR%
md %TEXTDIR%
md %PATCHDIR%

move ".\temp\occ_glyphtable.buct" %SYMDIR%
move ".\temp\occ_*.bfont" %FONTDIR%
move ".\temp\occ_atlas.bctex" %TEXDIR%
move ".\us_english.txt" %TEXTDIR%
move ".\temp\010093801237C000" %PATCHDIR%

ren ".\Patch-Translation\010093801237C000\romfs\system\fonts\occ_18.bfont" occ_20.bfont
ren ".\Patch-Translation\010093801237C000\romfs\system\fonts\occ_30.bfont" occ_32.bfont
ren ".\Patch-Translation\010093801237C000\romfs\system\fonts\occ_38.bfont" occ_42.bfont
ren ".\Patch-Translation\010093801237C000\romfs\system\fonts\occ_50.bfont" occ_52.bfont
