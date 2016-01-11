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

## Configuration
whatsapp-photo-frame needs whatsapp credentials. They are stored in `config.py`. Obtain them using `yowsup-cli registration` tool.
