#! /usr/bin/bash
docker run --shm-size="1024m" --gpus all --rm -it -e LIGHTLY_TOKEN={MY_LIGHTLY_TOKEN} \ 
    lightly/worker:latest token=your_awesome_token worker.worker_id={MY_WORKER_ID}