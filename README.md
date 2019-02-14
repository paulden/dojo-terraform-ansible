# Dojo Terraform / Ansible

This repository holds some code to demonstrate how Terraform and Ansible may be used, to create and
configure instances on a cloud provider (AWS here) using code.

## Goal

We want to run a Python script from a distant server. The code is available on a bucket on AWS S3.
We need to create the server and configure it to run the script.

### How we are going to do it

We are going to use AWS to create and configure instances automatically to run our script. This way, we can create
(or destroy) instances on demand and ensure all operations may be reproduced identically.
 
Let's split the work to be done into different steps:
- 1 - Deploy an instance on AWS using **Terraform**
- 2 - Configure the instance to be able to run the Python script using **Ansible**
- 3.0 - Run the script from an Ansible playbook
- 3.1 - Create a cronjob to run the script every 10 minutes (optional)

## Python script

The Python script is also available in the `data_code` folder and contains a `README.md`.
It uses some pip packages to extract object from an image (using YOLOv3 algorithm). 
