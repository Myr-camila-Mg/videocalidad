pipeline {
    agent any

    stages {
        stage('Preparación del entorno') {
            steps {
                echo 'Instalando dependencias...'
                sh 'pip install --upgrade pip'
                sh 'pip install selenium'
            }
        }
        stage('Ejecución de tests unitarios') {
            steps {
                echo 'Ejecutando tests unitarios...'
                sh 'python -m unittest discover -s testselenium'
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminado.'
        }
        success {
            echo 'Pipeline completado con éxito.'
        }
        failure {
            echo 'Pipeline fallido. Verifica los logs para más detalles.'
        }
    }
}

        failure {
            echo 'Pipeline fallido. Verifica los logs para más detalles.'
        }
    }
}
