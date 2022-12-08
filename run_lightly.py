from lightly.api import ApiWorkflowClient
from lightly.openapi_generated.swagger_client.models.dataset_type import DatasetType
from lightly.openapi_generated.swagger_client.models.datasource_purpose import DatasourcePurpose

# Create the Lightly client to connect to the API.
client = ApiWorkflowClient(token='your_awesome_token')

# Create a new dataset on the Lightly Platform.
client.create_dataset(
    'your_dataset_name',
    DatasetType.IMAGES
)

# Input bucket
client.set_s3_config(
    resource_path='s3://YourInputBucket/sportradar_input/',
    region='eu-central-1',
    access_key='your_access_key',
    secret_access_key='your_secret_access_key',
    purpose=DatasourcePurpose.INPUT
)

# Lightly bucket
client.set_s3_config(
    resource_path='s3://YourLightlyBucket/sportradar_lightly/',
    region='eu-central-1',
    access_key='your_access_key',
    secret_access_key='your_secret_access_key',
    purpose=DatasourcePurpose.LIGHTLY
)

client.schedule_compute_worker_run(
    worker_config={
        'enable_corruptness_check': True,
        'remove_exact_duplicates': True,
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
    lightly_config={
        'loader': {
            'batch_size': 16,
            'shuffle': True,
            'num_workers': -1,
            'drop_last': True
        },
        'model': {
            'name': 'resnet-18',
            'out_dim': 128,
            'num_ftrs': 32,
            'width': 1
        },
        'trainer': {
            'gpus': 1,
            'max_epochs': 20,
            'precision': 32
        },
        'criterion': {
            'temperature': 0.5
        },
        'optimizer': {
            'lr': 1,
            'weight_decay': 0.00001
        },
        'collate': {
            'input_size': 64,
            'cj_prob': 0.8,
            'cj_bright': 0.7,
            'cj_contrast': 0.7,
            'cj_sat': 0.7,
            'cj_hue': 0.2,
            'min_scale': 0.15,
            'random_gray_scale': 0.2,
            'gaussian_blur': 0.5,
            'kernel_size': 0.1,
            'vf_prob': 0,
            'hf_prob': 0.5,
            'rr_prob': 0
        }
    }
)
