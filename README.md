# Secret Santa Generator

A python script for generating secret santas and emailing participants a
message populated with the pairing information using SendGrid's python API.

## Usage

To use this python script you should run the script and pass your santas.json
file as the only argument.

```shell-session
$ python santas.py <filename.yaml>
```

## Making Your santas.yaml file

The santas.yaml file contains your SendGrid login information, a list of your santas, your message you want to send and the subject line for that message. The message should contain two python format string spots {0} (santa) and {1} (recipient). Only the santa will get the generated email.

An example is provided below:

```
sendgrid_info:
  uname: UNAME
  pwd: PWD

santas:
  - name: Santa 1
    email: wow@such.com
  - name: Foo Bar Santa
    email: foo@bar.com

letter_form:
  from_address: My Name <myname@email.com>
  subject: Santa Is So Secret
  message: |
    <p>Hello {0},</p>
    <p>You are the secret santa of <b>{1}</b></p>
    <p>From,</p>
    <p>A Python Script That Generates These Emails</p>
```
