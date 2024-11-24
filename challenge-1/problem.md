# Russian Encryption

- Namespace: picoctf/18739f24
- ID: russian-encryption
- Type: custom
- Category: Crypto
- Points: 1
- Templatable: no
- MaxUsers: 0

## Description

Oh no! President Joe Biden will not be running in 2024. You are a highly ranked government official and you have just received this news from your co-workers. At the same time, a Russian spy has been captured by CIA. According to the CIA, they've recovered some photos from the spy's personal belongings. As they were more worried about a potential second Trump term, they've chosen to ignore the photos. The photos have come to your pocession and you suspect there might be important information hiding in plain sight...

Download the scanned images of these photos {{url_for("gibberish.zip", "here")}}.

## Details

## Hints

- Download the file, unzip, and play away. What if the Russian spy uses encryption on these images? I've been told their encryption strategy can be twoo secure, if you know what I mean.

## Solution Overview

Download `gibberish.zip` and unzip it. XOR the two images together will reveal the flag.

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Test basic knowledge of Two Time Pad

## Attributes

- author: Xiao (Simon) Jin
- organization: CMU
- event: 18739 F24 CTF DEV 1
