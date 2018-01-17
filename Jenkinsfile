pipeline {
    agent {
        dockerfile true
    }

    stages {
        stage('Run') {
            steps {
                sh 'python app.py -t "${datetime}"'
            }
        }
    }
}
