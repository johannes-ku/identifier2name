from urllib.request import urlopen
import json
import sys


out = ""
with open ("token.txt", "r") as tokenin:
    token = tokenin.readline()
    with open ("in.txt", "r") as filein:
        grades = filein.readlines()
        for line in grades:
            line_data = line.split(",")
            stud = json.loads(urlopen("https://ois2.ttu.ee/uusois/!uus_ois2.ois_public.get_json?j_code=" + token + "&p_where=tparam0%3D" + line_data[0] +"%26daparam0%3D%26dlparam0%3D%26wparam0%3Dtud_kood%252FS").read().decode("UTF-8"))
            name = stud[1]["andmed"][0]["t_nimi"]
            out += name + (27 - len(name))*" " + line_data[2]
        text_file = open("out.txt", "w")
        text_file.write(out)
