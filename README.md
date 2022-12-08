### Object Detection example on a selection on SportRadar Challenge

This is an example of folder structure of a complete run on [DeepSportRadar Instance Segmentation Challenge](https://github.com/DeepSportRadar/instance-segmentation-challenge)!
Predictions are computed on the union of val and test sets using a detectron2 mask_rcnn_R_50_FPN_3x model finetuned on the train set. Metadata are created with the name of the folders in which images are contained.

#### How to run the selection

In order to run the selection (on valtest set) you have first to upload data to your cloud buckets by using the following AWS CLI commands:

```
aws s3 cp input_bucket s3://yourInputBucket/sportradar_input/ --recursive
aws s3 cp lightly_bucket s3://yourInputBucket/sportradar_lightly/ --recursive
```

Then simply run the worker with your API token and your worker id:

```
bash worker.sh
```

And finally run your Python scheduling script with:

```
python job_scheduler.py
```
