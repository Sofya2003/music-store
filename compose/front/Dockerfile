FROM node:16-alpine

ARG PROJ_DIR=/front_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./musical-instrument-store ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN npm install -g npm

COPY ./musical-instrument-store/package.json ${PROJ_DIR}
COPY ./musical-instrument-store/package-lock.json ${PROJ_DIR}

RUN npm install

CMD ["npm", "run", "serve"]