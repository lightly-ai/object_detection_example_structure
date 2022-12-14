from lightly.api import ApiWorkflowClient
from lightly.openapi_generated.swagger_client.models.dataset_type import DatasetType
from lightly.openapi_generated.swagger_client.models.datasource_purpose import DatasourcePurpose

# Create the Lightly client to connect to the API.
client = ApiWorkflowClient(token="MY_LIGHTLY_TOKEN")

# Create a new dataset on the Lightly Platform.
client.create_dataset(
    'dataset-name',
    DatasetType.IMAGES
)

# Configure the Input datasource.
client.set_s3_config(
    resource_path="s3://yourInputBucket/sportradar_input/",
    region="eu-central-1",
    access_key="S3-ACCESS-KEY",
    secret_access_key="S3-SECRET-ACCESS-KEY",
    purpose=DatasourcePurpose.INPUT
)

# Configure the Lightly datasource.
client.set_s3_config(
    resource_path="s3://yourLightlyBucket/sportradar_lightly/",
    region="eu-central-1",
    access_key="S3-ACCESS-KEY",
    secret_access_key="S3-SECRET-ACCESS-KEY",
    purpose=DatasourcePurpose.LIGHTLY
)

client.schedule_compute_worker_run(
    worker_config={
        'enable_training': True,
        "relevant_filenames_file": ".lightly/relevant_filenames.txt",
    },
    selection_config={
        "n_samples": 10,
        "strategies": [
            {
                "input": {
                    "type": "METADATA",
                    "key": "court"
                },
                "strategy": {
                    "type": "BALANCE",
                    "target": {
                        "KS-FR-MONACO" : 0.2
                    }  
                },
            },
            {
                "input": {
                    "type": "EMBEDDINGS",
                    "task": "object_detection_sportradar",
                },
                "strategy": {
                    "type": "DIVERSITY",
                }
            },
            {
                "input": {
                    "type": "EMBEDDINGS",
                },
                "strategy": {
                    "type": "DIVERSITY",
                }
            },
            {
            "input": {
                "type": "SCORES",
                "task": "object_detection_sportradar", 
                "score": "uncertainty_entropy" 
            },
            "strategy": {
                "type": "WEIGHTS"
            }
        }
        ]
    },
)
