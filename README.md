### Object Detection example on a selection on SportRadar Challenge

This is an example of folder structure in the Lightly format for data selection using data from the [DeepSportRadar Instance Segmentation Challenge](https://github.com/DeepSportRadar/instance-segmentation-challenge)!
Predictions are computed on the union of val and test sets using a detectron2 mask_rcnn_R_50_FPN_3x model finetuned on the train set. Metadata are created with the name of the folders in which images are contained. KS-FR-ROANNE folder is removed using our [relevant filenames feature](https://docs.lightly.ai/docs/relevant-filenames).
In this example you will find an implementation using [AWS S3](https://docs.lightly.ai/docs/aws-s3). Lightly also supports working with [Azure](https://docs.lightly.ai/docs/azure) and with [Google Cloud Storage](https://docs.lightly.ai/docs/google-cloud-storage). You need to adjust some code accordingly to the docs in order to use these other providers, but the folder structure remains the same.

#### How to run the selection

This is how the folder structure looks like:

```
.
├── input_bucket/
│   ├── KS-FR-BLOIS/
│   │   ├── 24330/
│   │   │   ├── camcourt1_1513714448590_0.png
│   │   │   └── ...
│   │   └── ...
│   └── ...
└── lightly_bucket/
    └── .lightly/
        ├── metadata/
        │   ├── schema.json
        │   ├── KS-FR-BLOIS/
        │   │   ├── 24330/
        │   │   │   ├── camcourt1_1513714448590_0.png
        │   │   │   └── ...
        │   │   └── ...
        │   └── ...
        ├── predictions/
        │   ├── tasks.json
        │   └── object_detection_sportradar/
        │       ├── schema.json
        │       ├── KS-FR-BLOIS/
        │       │   ├── 24330/
        │       │   │   ├── camcourt1_1513714448590_0.png
        │       │   │   └── ...
        │       │   └── ...
        │       └── ...
        └── relevant_filenames.txt
```

In order to run the selection (on valtest set) you have first to upload data to your cloud buckets by using the following AWS CLI commands:

```
aws s3 cp input_bucket s3://yourInputBucket/sportradar_input/ --recursive
aws s3 cp lightly_bucket s3://yourInputBucket/sportradar_lightly/ --recursive
```

Then simply run the worker with your API token and your worker id:

```
bash start_lightly_worker.sh
```

And finally run your Python scheduling script with:

```
python run_lightly.py
```
