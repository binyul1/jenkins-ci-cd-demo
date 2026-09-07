pipeline {
    agent { label 'built-in'}
 
    environment {
        IMAGE_NAME = "binyul1/jenkins-ci-cd-demo"
        VERSION = "v${env.BUILD_NUMBER}"
        }
    
    stages{
        stage('Checkout') {
            steps {
                git (
                    url: 'https://github.com/binyul1/jenkins-ci-cd-demo.git',
                    branch: 'main',
                    credentialsId: 'd0f593bf-63bd-4a22-892d-297751f334c7'  
                )
            }
        }
 
        stage('Install and Test') {
            steps {
                sh '''
                    #!/bin/bash
                    python3 -m venv venv
                    venv/bin/pip install -r backend/requirements.txt
                    PYTHONPATH=. venv/bin/pytest backend/tests/test_app.py --junitxml=results.xml
                '''
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$VERSION .'
                sh 'docker tag $IMAGE_NAME:$VERSION $IMAGE_NAME:latest'
            }
        }
 
        stage('Push to dockerhub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'caf9edc2-374b-4e9d-9f83-d7d59f3a05bb', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $IMAGE_NAME:$VERSION'
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }
 
 
    }
}