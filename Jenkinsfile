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
        stage('run rest app') {
            steps {
                script {
                    bat 'start /min python rest_app.py'
                }
            }
        }
        stage('run web app') {
            steps {
                script {
                    bat 'start /min python web_app.py'
                }
            }
        }
        stage('run backend testing') {
            steps {
                script {
                    bat 'python backend_testing.py'
                }
            }
        }
        stage('run frontend testing') {
            steps {
                script {
                    bat 'python frontend_testing.py'
                }
            }
        }
        stage('run combined testing') {
            steps {
                script {
                    bat 'python combined_testing.py'
                }
            }
        }
        stage('run clean') {
            steps {
                script {
                    bat 'python clean_environment.py'
                }
            }
        }
    }
}