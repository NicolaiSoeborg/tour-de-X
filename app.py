from collections import defaultdict
from urllib.parse import quote_plus
from sys import platform
from time import sleep
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from tspy import TSP
from tspy.solvers import TwoOpt_solver

addresses = """
DTU bygning 101, lyngby
Bagsværd Station
Lautrupvang 15, 2750 Ballerup
Nørreport Station
Rævehøjvej 36, 2800 Kongens Lyngby
"""


# ==== DONT TOUCH BELOW ==== #
addresses = [adr for adr in addresses.split("\n") if adr.strip() != ""]
print("Tour:")
for i, adr in enumerate(addresses):
    print(f' {i+1}) {adr}')
start_idx = int(input("\nWhich address should the tour start at? ")) - 1  # because humans
assert 0 <= start_idx < len(addresses), 'Oops, too high or low number?'

URL = "https://www.google.dk/maps/dir/{a}/{b}/"
ext = {'windows': 'exe'}.get(platform, platform)
driver = webdriver.Chrome(f'./chromedriver.{ext}')

# Click the cookie banner
driver.get(URL.format(a="", b=","))
driver.find_element(By.XPATH, '//button[normalize-space()="Acceptér alle"]').click()
sleep(1.5)

def time_str(string):
    """ Super error prone function, deal with it """
    # input is eg: "40 min" or "1 t 34 min"
    if len(string) > 10:
        print(f'Fejl i tid? Tid: {string}')
        return 60
    return eval(string.replace('t', '*60 +').replace('min', ''))  # TODO: dont do this

def get_time_between(a, b):
    driver.get(URL.format(a=quote_plus(a, safe=","), b=quote_plus(b, safe=",")))
    while True:
        try:
            sleep(1)
            driver.find_element(By.XPATH, '//button[normalize-space()="Offentlig transport"]').click()
            break
        except WebDriverException: pass
    while True:
        try:
            sleep(1)
            trip = driver.find_element(By.CLASS_NAME, 'section-directions-trip-description')
            return time_str(trip.text.split("\n")[0])
        except WebDriverException: pass

graph = defaultdict(dict)
N = len(addresses)

for i, adr in enumerate(addresses):
    for j, adr2 in enumerate(addresses):
        print(f"\rCreating graph... ({i*N + j+1} of {N*N})", end='')
        if i == j:
            continue
        if adr in graph[adr2] or adr2 in graph[adr]:
            continue

        assert (adr2 not in graph[adr]) and (adr not in graph[adr2])
        tid = get_time_between(adr, adr2)
        graph[adr][adr2] = tid
        graph[adr2][adr] = tid  # <-- this might not be true, but whatever...

driver.get(f'https://xn--sb-lka.org/?tdr={len(addresses)}')

print("\n... Graph created.\n\nFinding fastest route... (you can close the browser)")

# Insert fake node:
start_node = addresses[start_idx]
graph['fake'][start_node] = 1
for node in graph.keys():
    if node in ['fake', start_node]:
        continue
    graph[node]['fake'] = 1

# Create distance matrix:
M = np.ndarray(shape=(N,N), dtype=float)

for i, adr in enumerate(addresses):
    for j, adr2 in enumerate(addresses):
        if i == j:
            M[i,j] = np.inf
        else:
            M[i,j] = graph[adr][adr2]

tsp = TSP()
tsp.read_mat(M)

print("Solving using 2-opt heuristic for TSP:")
two_opt = TwoOpt_solver(initial_tour='NN', iter_num=100)
two_opt_tour = tsp.get_approx_solution(two_opt)

for idx in range(len(two_opt_tour)-1):
    a = addresses[two_opt_tour[idx]]
    b = addresses[two_opt_tour[idx+1]]
    print(f'From: {a}')
    print(f'To..: {b}')
    print('Time: {} min'.format(graph[a][b]))
    print('')
