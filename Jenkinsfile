pipeline {
    agent any

    stages {
        stage('Preparación del entorno') {
            steps {
                script {
                    echo 'Instalando dependencias...'
                    sh 'pip install --upgrade pip'
                    sh 'pip install selenium'
                }
            }
        }
        stage('Ejecución de tests unitarios') {
            steps {
                script {
                    echo 'Ejecutando tests unitarios...'
                    sh 'python -m unittest discover -s testselenium'
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'Pipeline terminado.'
            }
        }
        success {
            script {
                echo 'Pipeline completado con éxito.'
            }
        }
        failure {
            script {
                echo 'Pipeline fallido. Verifica los logs para más detalles.'
            }
        }
    }
}


