import pandas as pd
serial_killers = [
    ["Jack the Ripper", 1887, 1888, 5 ],
    ["Jeffrey Dahmer", 1974, 1991, 17 ],
    ["Harold Shipman", 1972, 1998, 250 ],
    ["John Wayne Gacy", 1978, 1994, 33],
    ["H.H. Holmes", 1983, 1986, 30], 

]
headers = [ 
    "Name", 
    "From",
    "To",
    "Victim Count",

] 
sk = pd.DataFrame(serial_killers, columns=headers)
print(sk)