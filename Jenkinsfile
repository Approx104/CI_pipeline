pipeline {
    agent any
    stages {
        stage('Pull from github') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git url: 'git://github.com/Approx104/Python-frontend-and-backend-stack',
                     branch: 'main'
            }
        }
        stage('run db connector') {
            steps {
                script {
                    bat 'python pythonProject/db_connector.py'
                }
            }
        }
        stage('run rest app') {
            steps {
                script {
                    bat 'start /min python pythonProject/rest_app.py'
                }
            }
        }
        stage('run web app') {
            steps {
                script {
                    bat 'start /min python pythonProject/web_app.py'
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
        stage('run frontend testing') {
            steps {
                script {
                    bat 'python pythonProject/frontend_testing.py'
                }
            }
        }
        stage('run combined testing') {
            steps {
                script {
                    bat 'python pythonProject/combined_testing.py'
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
    }
}