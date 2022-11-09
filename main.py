import pandas as pd
import matplotlib.pyplot as plt
serial_killers = [
    ["Jack the Ripper", 1887, 1888, 5, "Knife Wound, Multilation", "Male"],
    ["Jeffrey Dahmer", 1974, 1991, 17, "Strangulation", "Male"],
    ["Harold Shipman", 1972, 1998, 250, "Morphine Overdose", "Male" ],
    ["John Wayne Gacy", 1978, 1994, 33, "Asphyxiation with garrot", "Male"],
    ["H.H. Holmes", 1983, 1986, 30, "Hanged", "Male"], 
    ['Luis Garavito', 1992, 1999, 147, "Stabbing, Mutilation", "Male"],
    ['Henry Lee Lucas', 1946, 1983, 41, "Stabbing", "Male"],
    ['Aileen Wuornos', 1989, 1990, 7, "Gun Shot", "Female"],
    ['Judias Buenoano', 1971, 1980, 3, "Arsenic Poisoning", "Female"],
    ['Juana Barraza', 2002, 2006, 40, "Strangulation", "Female"],
    ["Jane Toppan or Jolly Jane", 1895, 1901, 31, "Poisoning", "Female"],
    ['Gesche Gottfried', 1813, 1827, 15, "Poisoning", "Female"],
    ['Amelia Dyer', 1869, 1896, 400, "Poison, Starvation, Strangulation","Female"],
    ['kristen Gilbert', 1995, 1996, 4, "Stimulant Injections", "Female"],
    ['Nannie Doss', 1920, 1954, 11, "Rat Poison", "Female"],
    ['Dorotha Puente', 1982, 1988, 9, "Drug Overdose", "Female"],
    ['Miyuki Ishikawa', 1944, 1948, 169, 'Neglect', "Female"],
    

]
headers = [ 
    "Name", 
    "From",
    "To",
    "Victim Count",
    "Modus Operandi",
    "Gender",

] 
skm = pd.DataFrame(serial_killers, columns=headers)


skm['duration'] = 1 + skm['To'].astype(int) - skm['From'].astype(int)


skm['rate'] = skm['Victim Count'] /  skm['duration']


# plot rates by killer (simple for example)

skm['rate'].plot(kind="bar")


# plot rates by killer (simple for example)

