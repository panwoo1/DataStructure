'''
    Code by Chan-Su Shin (신찬수, 한국외대, 컴전학부)
    자료구조및실습 수업용 코드
    실시간으로 hash.csv를 읽어 그래프를 그려주는 코드
    2020-05-07
'''
import matplotlib.pyplot as plt
import pandas as pd
import random
from matplotlib.animation import FuncAnimation
import math

plt.style.use('seaborn')
csv_filename = "hash.csv"

def animate_csv(i):
    data = pd.read_csv(csv_filename)
    x = data['operations']
    coll = [y/x for x, y in zip(x, data['collisions'])]
    comp = [y/x for x, y in zip(x, data['comparisons'])]
    s_comp = [y/max(x,1) for x, y in zip(data['succ_search'], data['succ_comp'])]
    f_comp = [y/max(x,1) for x, y in zip(data['fail_search'], data['fail_comp'])]

    plt.cla()
    plt.plot(x, coll, label="collsions/operations")
    plt.plot(x, comp, label="comparisons/operations")
    plt.plot(x, s_comp, label="comparisons/successful_searches")
    plt.plot(x, f_comp, label="comparisons/unsuccessful_searches")
    plt.xlabel("number of operations")
    plt.ylabel("average time")
    plt.legend(loc="upper left")
    plt.tight_layout()

# FuncAnimation 함수를 찾아보고 공부할 것!
# animate_csv 함수를 0.6초마다 호출해서 실행해 주는 함수
ani = FuncAnimation(plt.gcf(), animate_csv, interval=600)

plt.tight_layout()
plt.show()