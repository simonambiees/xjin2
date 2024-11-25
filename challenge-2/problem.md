# Trust My Files

- Namespace: picoctf/18739f24
- ID: trust-my-files
- Type: custom
- Category: Forensics
- Points: 1
- Templatable: no
- MaxUsers: 0

## Description

Everyone has their opinions on Donald Trump winning a second term. You work for a large media outlet, and one day receives a file from an anonymous source, claiming they have damaging information on President-elect Trump. You decide to take a look to find the secrets.

Download the file {{url_for("latest_scandal.tar.gz", "here")}}.

## Details

## Hints

- Download the file and start analysing. Look at the files for hints...

## Solution Overview

Download `latest_scandal.tar.gz` and unzip it. Analysing the content of the resulting image can yield two files. One of which, when unzipped, has the flag.

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

Test ability to navigate file structure

## Attributes

- author: Xiao (Simon) Jin
- organization: CMU
- event: 18739 F24 CTF DEV 2
