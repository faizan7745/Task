pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('your-image-name')
                }
            }
        }

        stage('Push to ECR') {
            steps {
                script {
                    withAWS(region: 'your-aws-region', credentials: 'aws-credentials-id') {
                        docker.withRegistry('https://your-account-id.dkr.ecr.your-region.amazonaws.com', 'ecr:us-east-1') {
                            docker.image('your-image-name').push('latest')
                        }
                    }
                }
            }
        }

        stage('Deploy with Terraform') {
            steps {
                sh 'terraform init'
                sh 'terraform apply -auto-approve'
            }
        }
    }
}
