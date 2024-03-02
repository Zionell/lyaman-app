FROM node:18

WORKDIR /app

EXPOSE 3000

#RUN apk update && apk upgrade

COPY ./package*.json /app/

RUN npm ci && npm cache clean --force

COPY . .

RUN chmod +x entrypoint.production.sh

RUN npm run build

