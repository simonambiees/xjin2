# References base image by SHA to avoid drift. This is Ubuntu 24.04. You will
# probably want to update the hash when working on a new challenge.
FROM ubuntu@sha256:e3f92abc0967a6c19d0dfa2d55838833e947b9d74edbcb0113e48535ad4be12a AS challenge


# Challenge metadata and artifacts go here. Only root has access
RUN mkdir /challenge && \
    chmod 700 /challenge

# * Copy flag.txt to the image
COPY Trump_Tower.jpg /app/
WORKDIR /app

# FROM base AS challenge
ARG FLAG

RUN touch flag.txt the_building_photo.jpg trump_scandals.pdf
RUN echo "Did you know Trump has a tower in NYC with his name on it? Talk about corruption! I best he keeps secrets in the building!" > trump_scandals.pdf
RUN echo $FLAG | sed "s/.*{/picoCTF{dont_take_me_for_granted_/1" > flag.txt
RUN tar czvf the_truth.tar.gz flag.txt
RUN cat Trump_Tower.jpg the_truth.tar.gz > the_building_photo.jpg
RUN tar czvf latest_scandal.tar.gz the_building_photo.jpg trump_scandals.pdf

# * Creates /challenge/artifacts.tar.gz which cmgr uses to offer artifact
#   downloads in problem.md.
# * Creates /challenge/metadata.json which defines the flag and potentially
#   other metadata.
RUN tar czvf /challenge/artifacts.tar.gz latest_scandal.tar.gz && \
    echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json


# This is a dummy command that keeps the container running. cmgr will keep
# restarting the container if it exits.
CMD ["tail", "-f", "/dev/null"]
