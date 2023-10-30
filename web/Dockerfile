FROM node:18-alpine

WORKDIR /react-vite-app

EXPOSE 3000

COPY package.json yarn.lock ./

RUN yarn install

COPY . ./

CMD ["npm", "start"]