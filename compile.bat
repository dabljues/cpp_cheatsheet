@echo off
python merge.py & pandoc cheatsheet.md -o cheatsheet.pdf --listings -H style.tex -N --toc