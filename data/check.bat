@echo off
for /l %%i in (1, 1, 10) do (
    checker.exe testcase%%i.in testcase%%i.out > report%%i.log
)
