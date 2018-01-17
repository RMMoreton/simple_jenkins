pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/RMMoreton/simple_jenkins/'
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t simple_date ."
            }
        }
        stage('Run') {
            steps {
                sh "docker run --rm simple_date python app.py -t '${datetime}'"
            }
        }
        stage('Clean') {
            steps {
                sh "docker rmi simple_date"
            }
        }
    }
}
