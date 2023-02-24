FROM node:16.18

ENV PORT=3000

#outside -> inside container(src->dest)
COPY . /frontend-react-js

WORKDIR /frontend-react-js

RUN npm install

EXPOSE ${PORT}

CMD ["npm", "start"]