pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', artifactNumToKeepStr: '5', daysToKeepStr: '5'))
    }
    environment {
        registry = "aranor104/ci_pipeline"
        registryCredential = 'docker_hub'
        dockerImage = ''
    }
    stages {
        stage('Pull from github') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * * ')])])
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
        stage('test dockerized app') {
            steps {
                script {
                    bat 'python pythonProject/docker_backend_testing.py'
                }
            }
        }
        stage('chart install') {
            steps {
                bat 'helm install my-release ./mychart -set image.repository="aranor104/ci_pipeline":${BUILD_NUMBER}'
            }
        }
        stage('start tunnel') {
            steps {
                bat "minikube service rest-app-service –url > k8s_url.txt"
            }
        }
        stage('test deployed app') {
            steps {
                script {
                    bat 'python pythonProject/k8s_backend_testing.py'
                }
            }
        }
    }
    post {
        always {
            bat "docker-compose down"
            bat "docker rmi $registry:$BUILD_NUMBER"
            bat "helm delete my-release"
        }
    }
}