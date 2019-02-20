# Car detection

This repository contains source code to detect objects from an image 
and is meant to be used to count cars and trucks.

## Requirements

The source code runs using Python 3.6 or higher.

Python packages required are in the `requirements.txt` file and may be installed using pip:

```bash
pip install -r requirements.txt
```

Running the main script on Ubuntu also requires the following packages:

```bash
sudo apt install pkg-config python-opencv
```

If not present, pre-trained model may be downloaded:

```bash
./download_config_files.sh
```

## Usage

There are three scripts in the source code.

### Pull latest image from S3 bucket

To pull the latest image from the S3 bucket:

```bash
python3 pull_last_file_from_bucket.py
```

### Detect cars

To run the main detection script:

```bash
python3 detect.py <optional : /image/location.png>
```

By default, the script will use the latest image in the `images/` folder.

It will generate an image with objects detected in the `result_images/` folder and a JSON report in the `result_reports/` (for instance `{car: 5, truck: 2}`).

### Push results to S3 bucket

To push the latest results to the S3 bucket:

```bash
python3 push_results_to_bucket.py
```
