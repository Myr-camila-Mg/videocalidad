pipeline {
    agent any 
    environment {
        PYTHON_PATH = 'C:/Users/sunmi/AppData/Local/Programs/Python/Python313/python.exe'
    }

    stages {
        stage('Preparación del entorno') {
            steps {
                script {
                    echo 'Instalando dependencias...'
                    bat "\"${env.PYTHON_PATH}\" -m venv venv"  // Crea un entorno virtual
                    bat "\"${env.PYTHON_PATH}\" -m pip install --upgrade pip"  // Actualiza pip
                    bat "\"${env.PYTHON_PATH}\" -m pip install selenium"  // Instalar Selenium
                }
            }
        }

        stage('Ejecución de tests unitarios') {
            steps {
                script {
                    echo 'Ejecutando tests unitarios...'
                    bat "\"${env.PYTHON_PATH}\" -m unittest discover -s testselenium -p \"tes_*.py\""
                }
            }
        }
    }

    post {
        success {
            echo 'Tests ejecutados exitosamente'
        }
        failure {
            emailext to: 'daniel.munoz.melendez@unillanos.edu.co',
                     subject: 'Error en la ejecución de tests',
                     body: 'Hola, hay un error.'
        }
    }

}



