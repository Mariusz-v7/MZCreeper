import os
from pyquery import PyQuery   
import re

def get_attr(label, attr, label_index):
    ret = []

    if label == 'id':
        id_ = attr.attr['id']

        r = id_
        r = re.findall(r'\d+', r)[-1]
        ret.append(r)
    if label == 'No':
        r = attr('img').attr['src']
        #r = r[-6:-4]
        r = re.findall(r'\d+', r)[-1]
        ret.append(r)
    if label == 'Name':
        r = attr.text()
        ret.append(r)
    if label == 'Attribute':
        r = attr('span').text()
        ret.append(r)
    if label == 'Change':
        imgs = attr('img')
        if len(imgs) == 2:
            #trener lub oboz
            
            r1 = attr('img:first-child').attr['src']
            r1 = r1.split('/')
            r1 = r1[-1]
            if r1 == 'coach.png':
                ret.append('coach')
            elif r1 == 'training_camp.png':
                ret.append('camp')
            else:
                ret.append(r1)
            #
            img = attr('img:last-child')
        else:
            img = attr('img')

        r1 = img('img').attr['src']
        r1 = re.findall(r'\d+', r1)[-1]

        ret.append(r1)

    return ret

def parse():
    trainings = os.listdir("training_reports")
    for training in trainings:
        #driver.get("squad/"+squad+"/squad.html")
        file_path = "training_reports/"+training

        days_names = ["weekly", "monday", "tuesday", "wednesday", "thurstay", "friday", "saturday"]
        for d in range(1, 7):
            if not os.path.exists(file_path+"/report_"+days_names[d]+".html"):
                continue
            if os.path.exists(file_path+"/report_"+days_names[d]+".txt"):
                continue

            file_ = open(file_path+"/report_"+days_names[d]+".html")
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
            j = 0
            for row in table.items():
                i = 0
                players.append([])
                players[j].append(get_attr(labels[i], row, i))
                for attr in row('td').items():
                    i += 1
                    players[j].append(get_attr(labels[i], attr, i))
                j += 1



            file_ = open(file_path+"/report_"+days_names[d]+".txt", "w")
            for player in players:
                i = 0
                for atr in player:
                    if len(atr) == 0:
                        i += 1
                        continue
                    file_.write(labels[i]+": ")
                    if len(atr) == 2:
                        file_.write(atr[0]+", "+atr[1]+"\r\n")
                    elif len(atr) == 1:
                        file_.write(atr[0]+"\r\n")
                    i += 1

                file_.write('\r\n\r\n')
            file_.close()
 
