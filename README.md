# ML-MilitaryExercise
 Machine Learning: A military exercise

## code

After the failed attempt to use reinforcement learning, this experiment was ultimately completed by writing an algorithm based on breadth-first search.

`DQNway.py` and `MEEnv.py` are failed attempts at machine learning. 

`find_path.py` is the code I wrote while trying to solve a pathfinding problem, which I treated as a draft.

## data

The `data` folder contains the data used for the experiments:

`checker.exe` is a simple program that checks scores by `testcase*.out`.

`check.bat` is a batch file that runs `checker.exe` for all `testcase*.in` and `testcase*.out` files (from 1 to 10).

It will execute the following instructions:
```sh
checker.exe testcase1.in testcase1.out > report1.log
checker.exe testcase2.in testcase2.out > report2.log
checker.exe testcase3.in testcase3.out > report3.log
checker.exe testcase4.in testcase4.out > report4.log
checker.exe testcase5.in testcase5.out > report5.log
checker.exe testcase6.in testcase6.out > report6.log
checker.exe testcase7.in testcase7.out > report7.log
checker.exe testcase8.in testcase8.out > report8.log
checker.exe testcase9.in testcase9.out > report9.log
checker.exe testcase10.in testcase10.out > report10.log
```

You can also directly show the log in the command prompt:
```sh
checker.exe testcase1.in testcase1.out
```

