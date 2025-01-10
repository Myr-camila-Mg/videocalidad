pipeline {
    agent any

    stages {
        stage('Preparación del entorno') {
            steps {
                script {
                    echo 'Instalando dependencias...'
                    bat 'python3 -m ensurepip --upgrade'
                    bat 'python3 -m pip install --upgrade pip'
                    bat 'pip install -r requirements.txt'
                    bat 'pip install selenium'
                }
            }
        }
        stage('Ejecución de tests unitarios') {
            steps {
                script {
                    echo 'Ejecutando tests unitarios...'
                    bat 'python3 -m unittest discover -s testselenium'
                }
            }
        }
    }
}



