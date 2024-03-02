FROM node:18

WORKDIR /app

RUN apk update && apk upgrade

COPY ./package*.json /app/

RUN npm ci && npm cache clean --force

COPY . .

RUN chmod +x entrypoint.production.sh

RUN npm run build

