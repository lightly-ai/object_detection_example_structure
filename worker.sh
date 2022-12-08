#! /usr/bin/bash
docker run --shm-size="1024m" --gpus all --rm -it     -v OUTPUT_DIR:/home/output_dir lightly/worker:latest token=your_awesome_token worker.worker_id=your_worker_id 