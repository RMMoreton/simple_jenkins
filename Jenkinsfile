node {
    stage('Clone') {
        git url: 'https://github.com/RMMoreton/simple_jenkins/'
    }
    stage('Build') {
        sh "docker build -t simple_date ."
    }
    stage('Run') {
        sh "docker run --rm simple_date"
    }
}
