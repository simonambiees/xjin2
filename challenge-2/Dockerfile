# References base image by SHA to avoid drift. This is Ubuntu 24.04. You will
# probably want to update the hash when working on a new challenge.
FROM ubuntu@sha256:e3f92abc0967a6c19d0dfa2d55838833e947b9d74edbcb0113e48535ad4be12a AS challenge

# Challenge metadata and artifacts go here. Only root has access
RUN mkdir /challenge && \
    chmod 700 /challenge

# * Copy flag.txt to the image
COPY gibberish.zip /app/
WORKDIR /app

# * Creates /challenge/artifacts.tar.gz which cmgr uses to offer artifact
#   downloads in problem.md.
# * Creates /challenge/metadata.json which defines the flag and potentially
#   other metadata.
RUN tar czvf /challenge/artifacts.tar.gz gibberish.zip && \
    echo "{\"flag\":\"joe_biden_is_our_comrade_6ffac749573f71f3\"}" > /challenge/metadata.json

# This is a dummy command that keeps the container running. cmgr will keep
# restarting the container if it exits.
CMD ["tail", "-f", "/dev/null"]
