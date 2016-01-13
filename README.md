# whatsapp-photo-frame
A photo-frame showing photos received from whatsapp chats.

## Motivation
My family uses a WhatsApp group chat to share all kinds of photos. This is a great way to stay in touch with them and e.g. see my niece growing up everyday. Sadly my grandmother (82yrs old) is not able to use whatsapp. She does not want to learn this new kind of communication. And I am okay with that. I show her the new photos from time to time. I don't mind doing that but I always thought: Wouldn't it be nice if she would be able to see them right now?

So i grabbed another raspberry pi, installed raspbian, setup yowsup2 + info-beamer and created whatsapp-photo-frame.

## Requirements
* Raspberry Pi w/ raspbian

## Dependencies
* yowsup2
* info-beamer

## Installation
```
sudo apt-get install python-dateutil python-setuptools python-dev libevent-dev ncurses-dev git
# nano setup.py - maybe remove pillow since we do not need that
git clone git://github.com/tgalal/yowsup.git
cd yowsup
nano setup.py
sudo python setup.py install
# exif feature
sudo apt-get install libimage-exiftool-perl perl-doc
sudo pip install pexif
# first start only generates shit
python stack.py
# start in background (temporary solution :p)
nohup python stack.py &
```

## Configuration
whatsapp-photo-frame needs whatsapp credentials. They are stored in `config.py`. Obtain them using `yowsup-cli registration` tool.
