import pandas as pd
serial_killers = [
    ["Jack the Ripper", 1887, 1888, 5, "Knife Wound, Multilation" ],
    ["Jeffrey Dahmer", 1974, 1991, 17, "Strangulation"],
    ["Harold Shipman", 1972, 1998, 250, "Morphine Overdose" ],
    ["John Wayne Gacy", 1978, 1994, 33, "Asphyxiation with garrot"],
    ["H.H. Holmes", 1983, 1986, 30, "Hanged"], 
    ['Luis Garavito', 1992, 1999, 147, "Stabbing, Mutilation"],
    ['Henry Lee Lucas', 1946, 1983, 41 "Stabbing"]
    

]
headers = [ 
    "Name", 
    "From",
    "To",
    "Victim Count",
    "Modus Operandi"

] 
sk = pd.DataFrame(serial_killers, columns=headers)

serial_killer_ladies = [
    ['Aileen Wuornos', 1989, 1990, 7, "Gun Shot"]
    ['Judias Buenoano', 1971, 1980, 3, "Arsenic Poisoning"]
    ['Juana Barraza', 2002, 2006, 40, "Strangulation"]
    ["Jane Toppan or Jolly Jane", 1895, 1901, 31, "Poisoning"]
    ['Gesche Gottfried', 1813, 1827, 15, "Poisoning"],
    ['Amelia Dyer', 1869, 1896, 400, "Poison, Starvation, Strangulation"],
    ['kristen Gilbert', 1995, 1996, 4 "Stimulant Injections"],
    ['Nannie Doss', 1920, 1954, 11, "Rat Poison"],
    ['Dorotha Puente', 1982, 1988, 9, "Drug Overdose" ],
    ['Miyuki Ishikawa', 1944, 1948, 169, 'Neglect']

]

headers2 = [ 
    "Name", 
    "From",
    "To",
    "Victim Count",
    "Modus Operandi"

] 
skw = pd.DataFrame(serial_killer_ladies, columns=headers2)
