python3 .\tools\scripts\btxt.py -xb "%cd%\put-text-here\us_english.txt" -p us_english.txt

set TEMPDIR=temp\
md %TEMPDIR%

move ".\us_english.txt" %TEMPDIR%