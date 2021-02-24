pipeline {
    agent any
    environment {
        registry = "aranor104/ci_pipeline"
        registryCredential = 'docker_hub'
        dockerImage = ''
    }
    stages {
        stage('Pull from github') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git url: 'git://github.com/Approx104/CI_pipeline',
                     branch: 'main'
            }
        }
        stage('run rest app') {
            steps {
                script {
                    bat 'start /min python pythonProject/rest_app.py'
                }
            }
        }
        stage('run backend testing') {
            steps {
                script {
                    bat 'python pythonProject/backend_testing.py'
                }
            }
        }
        stage('run clean') {
            steps {
                script {
                    bat 'python pythonProject/clean_environment.py'
                }
            }
        }
        stage('build and push image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('set version') {
            steps {
                bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
            }
        }
        stage('docker compose') {
            steps {
                bat "docker-compose up -d"
            }
        }
    }
    post {
        always {
            bat "docker-compose down"
            bat "docker rmi $registry:$BUILD_NUMBER"
        }
    }
}