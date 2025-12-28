pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/jamserali/SeleniumPytest-bdd.git', branch: 'develop'
            }
        }

        stage('Setup Python venv') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\python -m pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Run PyTest BDD') {
            steps {
                bat '''
                venv\\Scripts\\pytest -n auto --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                allure generate allure-results -o allure-report --clean
                '''
            }
        }
    }

     post {
        always {
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]
        }
    }
}
