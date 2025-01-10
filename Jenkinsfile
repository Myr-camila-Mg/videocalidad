pipeline {
    agent any

    stages {
        stage('Preparación del entorno') {
            steps {
                script {
                    echo 'Instalando dependencias...'
                    bat 'python -m ensurepip --upgrade'
                    bat 'python -m pip install --upgrade pip'
                    bat 'pip install -r requirements.txt'
                    bat 'pip install selenium'
                }
            }
        }
        stage('Ejecución de tests unitarios') {
            steps {
                script {
                    echo 'Ejecutando tests unitarios...'
                    bat 'python -m unittest discover -s testselenium'
                }
            }
        }
    }
    post {
        success {
            // Notificación si los tests son exitosos
            echo 'Tests ejecutados exitosamente'
        }
        failure {
            // Notificación si los tests fallan
            mail to: 'mcmurillo@unillanos.edu.co',
                 subject: 'Error en la ejecución de tests',
                 body: 'Hubo un error al ejecutar los tests. Revisa Jenkins para más detalles.'
        }
    }
}




