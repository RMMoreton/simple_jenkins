node {
    stage('Prep') {
        sh ls
    }
    stage('Build') {
        sh "docker build -t simple_date ."
    }
    stage('Run') {
        sh "docker run --rm simple_date"
    }
}
