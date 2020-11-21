FROM python:3.7-alpine

WORKDIR /app

RUN apk add --update \
  wget \
  udev \
  ttf-freefont \
  chromium \
  chromium-chromedriver \
  && pip install selenium

CMD ["python", "/app/transfermarkt.py"]