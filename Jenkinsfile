pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/devops-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Deploy') {
            steps {
                sh 'bash scripts/deploy.sh'
            }
        }

        stage('Health Check') {
            steps {
                sh 'python3 scripts/health_check.py'
            }
        }
    }
}
