FROM python:3.7-alpine

WORKDIR /app

RUN pip install --upgrade pip

RUN apk add --update \
  wget \
  udev \
  ttf-freefont \
  chromium \
  chromium-chromedriver

RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
    apk add --no-cache libxslt && \
    pip install lxml --no-cache-dir && \
    apk del .build-deps

RUN pip install selenium \
    && pip install bs4 \
    && pip install html5lib

CMD ["python", "/app/amazon.py"]