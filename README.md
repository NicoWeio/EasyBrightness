## State of the project

This is a small wrapper to more easily control your monitors' brightness.

It was hacked together in a few minutes or hours. This program works for me, but very unreliably (probably my Dell monitors' fault). I do not plan to work on this, but PRs are welcome anyway. 

[ddccontrol](https://github.com/ddccontrol/ddccontrol) is used to send commands to the monitor(s), and you might want to use that or [ddcutil](https://github.com/rockowitz/ddcutil) directly.

## Usage

You probably need to change the I²C addresses in `main.py`.

`./main.py 1:100,2:50` sets monitor 1 to 100% brightness (assuming 100 is the maximum, which is not necessarily the case) and monitor 2 to 50% brightness.
