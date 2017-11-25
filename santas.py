import yaml
import random
from itertools import tee, izip
import sendgrid
import sys

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

if len(sys.argv[1:]) != 1:
    print("Error: Wrong number of arguments, please call as ./santas.py santa_file.yaml")
    sys.exit(0)

file_name = sys.argv[1]
data = []
santas_yaml = {}
with open(file_name) as santa_file:
    try:
        santas_yaml = yaml.load(santa_file.read())
    except:
        print("Error: Invalid data santas!")
        sys.exit(0)

sg_login = santas_yaml["sendgrid_info"]
santas = santas_yaml["santas"]
form = santas_yaml["letter_form"]
from_addr = form["from_address"]
subject = form["subject"]
message = form["message"]

sg = sendgrid.SendGridClient(sg_login["uname"], sg_login["pwd"])

#Shuffle them santas
random.shuffle(santas)

# The santa list is circular. For 3 santas
# 0 -> 1
# 1 -> 2
# 2 -> 0
santas.append(santas[0])
santa_pairs = []
for santa, santaee in pairwise(santas):
    santa_pairs.append((santa, santaee))
    email_msg = sendgrid.Mail()
    email_msg.add_to('{0} <{1}>'.format(santa['name'], santa['email']))
    email_msg.set_subject(subject)
    email_msg.set_html(message.format(santa['name'], santaee['name']))
    email_msg.set_text(message.format(santa['name'], santaee['name']))
    email_msg.set_from(from_addr)
    status, msg = sg.send(email_msg)
    print status
    print msg
    print message.format(santa['name'], santaee['name'])

with open("santas_backup.txt", "w") as f:
    for santa_pair in santa_pairs:
        f.write("{} -> {}\n".format(santa_pair[0]["name"], santa_pair[1]["name"]))
