FROM node:16.16-alpine

WORKDIR /app

EXPOSE 3000

RUN apk update && apk upgrade

COPY ./package*.json /app/

RUN npm install && npm cache clean --force

COPY . .

RUN chmod +x entrypoint.production.sh

RUN npm run build

