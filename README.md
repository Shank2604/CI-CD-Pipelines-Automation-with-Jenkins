📌 Project Overview

This project demonstrates a real-world DevOps CI/CD pipeline designed for production-like environments.
It automates build, test, deployment, monitoring, backup, and rollback of a Python application using Jenkins, Docker, Linux, and AWS services.

The goal of this project is to eliminate manual deployment errors, improve reliability, and follow DevOps best practices used in industry.

🧠 Key Concepts Demonstrated

Continuous Integration & Continuous Deployment (CI/CD)

Linux automation & scripting

Cloud deployment using AWS EC2

Secure credential management

Automated health checks

🏗️ Architecture Overview

Developer
   │
   ▼
GitHub (Source Code)
   │
   ▼
Jenkins CI/CD Pipeline
   │
   ├── Build & Test
   ├── Docker Image Build
   ├── Backup Current Version (S3)
   ├── Deploy to EC2
   ├── Health Check
   └── Rollback on Failure

⚙️ CI/CD Pipeline Workflow

Developer pushes code to GitHub

Jenkins pipeline is triggered automatically

Current stable version is backed up to AWS S3

New container is deployed to AWS EC2

Health check is performed

If health check fails → automatic rollback occurs

☁️ AWS Services Used

EC2 – Application hosting

S3 – Backup storage

IAM – Secure authentication and authorization

👤 Author

Shashank Srivastav
Aspiring DevOps Engineer