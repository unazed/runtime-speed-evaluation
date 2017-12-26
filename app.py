import timeit
import matplotlib.pyplot as plt
from matplotlib.patches import Patch 
import math


try:
    input = raw_input
except NameError:
    pass

iters = int(input("{*} How many functions would you like to compare? "))
variable = input("{*} What is the unique replacement string? ")
startpoint = float(input("{*} What should be the starting integer? "))
endpoint = float(input("{*} What should be the ending integer? "))
step = float(input("{*} How many times should it run? "))
total_number = int(input("{*} How many times should each function run individiually? "))
steps = (endpoint-startpoint)/step

result_map = {
    # (<setup>, <function>, <color>): {
    #   <cycle 1>: <execution time>,
    #   <cycle 2>: <execution time>,
    #   etc.,
    # }
}

for n in range(iters):
    name = input("Name to be put on legend {%d} " % n)
    setup = input("Setup (run once) {%d} " % n) + '\n' or "pass"
    while 1:
        setup_ = input("Setup (run once) {%d} " % n) + '\n'
        if not setup_.strip():
            break
        setup += setup_

    stmt = input("Code {%d} " % n) + '\n'
    while 1:
        stmt_ = input("Code {%d} " % n) + '\n'
        if not stmt_.strip():
            break
        stmt += stmt_

    color = input("Color {%d} " % n)
    result_map[(setup, stmt, color, name)] = {}

for iteration in range(math.ceil(step)):
    for function in result_map:
        result_map[function][iteration] = timeit.timeit(
                setup=function[0].replace(
                        variable,
                        str(math.ceil(steps*iteration))
                ),
                stmt=function[1].replace(
                        variable,
                        str(math.ceil(steps*iteration))
                ),
                number=total_number,
            )
        plt.plot(iteration,
                 result_map[function][iteration],
                 color=function[2],
                 marker='o',
                 linestyle='solid',
            )

plt.ylabel("execution time (seconds)")
plt.xlabel("n iterations")
plt.legend(
    handles=[Patch(color=elem[2], label=elem[3]) for elem in result_map],
    loc="best")
plt.show()
