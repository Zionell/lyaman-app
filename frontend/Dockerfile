FROM node:18

ENV SERVER_API_URL=$SERVER_API_URL
ENV IMAGE_PROXY=$IMAGE_PROXY

WORKDIR /app

COPY ./package*.json /app/

RUN npm ci

COPY . .

EXPOSE 3000

RUN chmod +x entrypoint.production.sh

RUN npm run build

