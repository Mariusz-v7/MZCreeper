import os
from pyquery import PyQuery   
import shutil

def get_id(row):
    #id is in player url
    url = row('a').attr['href']
    pid_arg_pos = url.find('pid=')
    pid_end_pos = url.find("&", pid_arg_pos)

    pid = url[pid_arg_pos + 4:pid_end_pos] #+4 because "pid="

    return str(pid)

def parse():
    squads = os.listdir("squad")
    for squad in squads:
        #driver.get("squad/"+squad+"/squad.html")
        file_path = "squad/"+squad

        if os.path.exists(file_path+"/squad.txt"):
            continue

        file_ = open(file_path+"/squad.html")
        html = file_.readlines()

        str_ = ""
        for s in html:
            str_ += s

        parser = PyQuery(str_)
        head = parser('thead>tr>th')
        labels = []
        labels.append('id')
        for label in head.items():
            labels.append(label.text())
        ##
        table = parser('tbody>tr')
        players = []
        i = 0
        for row in table.items():
            players.append([])
            players[i].append(get_id(row))
            for arg in row('td').items():
                #print arg.text()
                players[i].append(arg.text().encode('UTF-8'))
            i += 1


        file_ = open(file_path+"/squad.txt", "w")
        for player in players:
            i = 0
            for atr in player:
                file_.write(labels[i]+": ")
                file_.write(atr+"\r\n")
                i += 1

            file_.write('\r\n\r\n')
        file_.close()