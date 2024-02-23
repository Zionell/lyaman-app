FROM node:18

WORKDIR /app

#RUN apt-get update && apt-get upgrade

COPY ./package*.json ./

RUN npm ci && npm cache clean --force

COPY . .

RUN npm run build

EXPOSE 1337

CMD ["npm", "run", "start"]
