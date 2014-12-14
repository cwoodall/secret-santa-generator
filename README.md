# Secret Santa Generator

A python script for generating secret santas and emailing participants a
message populated with the pairing information using SendGrid's python API.

## Usage

To use this python script you should run the script and pass your santas.json
file as the only argument.

> $ python santas.py <filename.json>

## Making Your santas.json file

The santas.json file contains your SendGrid login information, a list of your santas, your message you want to send and the subject line for that message. The message should contain two python format string spots {0} (santa) and {1} (recipient). Only the santa will get the generated email.

An example is provided below:

```
{
    "sendgrid_info": {
        "uname": "SENDGRID_USERNAME",
        "pwd": "SENDGRID_PASSWORD"
    },
    "santas": [
        {
            "name": "Name 1",
            "email": "email1@email.com"
        },
        {
            "name": "Name 2",
            "email": "email2@email.com"
        },
        {
            "name": "Name 3",
            "email": "email3@email.com"
        },
        {
            "name": "Name 4",
            "email": "email4@email.com"
        },
    ],
    "subject": "Example",
    "message": "<p>Hello {0},</p><p>You are the secret santa of <b>{1}</b></p>"
    "from_address": "My Name <myname@email.com>",
}
```
