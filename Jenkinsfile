pipeline {
    agent {
        dockerfile true
    }

    stages {
        stage('Run') {
            steps {
                sh 'virtualenv venv'
                sh '. venv/bin/activate'
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'python app.py -t "${datetime}"'
            }
        }
    }
}
