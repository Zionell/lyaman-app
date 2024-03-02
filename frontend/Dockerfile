FROM node:18

WORKDIR /app

COPY ./package*.json /app/

RUN npm ci && npm cache clean --force

COPY . .

EXPOSE 3000

RUN chmod +x entrypoint.production.sh

RUN npm run build

