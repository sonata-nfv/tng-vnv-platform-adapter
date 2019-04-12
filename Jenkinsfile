pipeline {
  agent any
  stages {
    stage('Container Build') {
      parallel {
        stage('Container Build') {
          steps {
            echo 'Building...'
          }
        }
        stage('tng-vnv-platform-mngr') {
          steps {
            sh 'docker build -t registry.sonata-nfv.eu:5000/tng-vnv-platform-adapter .'
          }
        }
      }
    }
    stage('Containers Publication') {
      parallel {
        stage('Containers Publication') {
          steps {
            echo 'Publication of containers in local registry....'
          }
        }
        stage('docker push') {
          steps {
            sh 'docker push registry.sonata-nfv.eu:5000/tng-vnv-platform-adapter'
          }
        }
      }
    }
    stage('Deployment in Pre-Integration') {
      parallel {
        stage('Deployment in Pre-Integration') {
          steps {
            echo 'Deploying in integration...'
          }
        }
        stage('Deploying') {
          steps {
            sh 'rm -rf tng-devops || true'
            sh 'git clone https://github.com/sonata-nfv/tng-devops.git'
            dir(path: 'tng-devops') {
              sh 'ansible-playbook roles/vnv.yml -i environments -e "target=pre-int-vnv-bcn.5gtango.eu component=tng-vnv-platform-adapter"'
            }
          }
        }
      }
    }
    stage('Smoke Tests') {
      steps {
        echo 'TODO: Performing Smoke Tests....'
      }
    }
    stage('Promoting containers to integration env') {
      when {
         branch 'master'
      }
      parallel {
        stage('Publishing containers to int') {
          steps {
            echo 'Promoting containers to integration'
          }
        }
        stage('tng-vnv-platform-adapter') {
          steps {
            sh 'docker tag registry.sonata-nfv.eu:5000/tng-vnv-platform-adapter:latest registry.sonata-nfv.eu:5000/tng-vnv-platform-adapter:int'
            sh 'docker push registry.sonata-nfv.eu:5000/tng-vnv-platform-adapter:int'
            sh 'rm -rf tng-devops || true'
            sh 'git clone https://github.com/sonata-nfv/tng-devops.git'
            dir(path: 'tng-devops') {
              sh 'ansible-playbook roles/vnv.yml -i environments -e "target=pre-int-vnv-bcn.5gtango.eu component=tng-vnv-platform-adapter"'
            }
          }
        }
      }
    }
  }
  post {
    success {
      emailext(subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", body: """<p>SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                        <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""", recipientProviders: [[$class: 'DevelopersRecipientProvider']]) 
    }
    failure {
      emailext(subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                        <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""", recipientProviders: [[$class: 'DevelopersRecipientProvider']])
    }
  }
}