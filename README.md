# Cloud Data API with Terraform

This project demonstrates a simple data pipeline using FastAPI and Terraform. 
It simulates a master data workflow by receiving data through a REST API, and includes a Terraform configuration to show Infrastructure-as-Code practices.

---

## Features

- FastAPI REST API with GET and POST endpoints
- Simulated master table behavior using local storage
- Terraform configuration to simulate cloud infrastructure provisioning
- Demonstrates:
  - Infrastructure-as-Code
  - API data ingestion
  - Data consolidation workflow
  - Version-controlled infrastructure

---

## Project Structure

cloud-data-api/
│
├── api/ # FastAPI backend code
├── terraform/ # Terraform configuration files
└── README.md # Project documentation

yaml
---

## Tech Stack

- Python, FastAPI, Pydantic
- Terraform (local_file provider demo)
- GitHub Codespaces
