FROM jfloff/alpine-python:latest-slim
EXPOSE 7777
EXPOSE 7778
EXPOSE 7779
RUN /entrypoint.sh \
  -p twisted \
&& echo
WORKDIR /app
CMD python helium.py
