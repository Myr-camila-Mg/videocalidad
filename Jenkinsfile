pipeline {
    agent any  // Ejecuta el pipeline en cualquier nodo disponible

    environment {
        // Definir la ruta al ejecutable de Python
        PYTHON_PATH = 'C:/Users/sunmi/AppData/Local/Programs/Python/Python313/python.exe'
    }

    stages {
        stage('Preparación del entorno') {
            steps {
                script {
                    echo 'Instalando dependencias...'
                    // Crear un entorno virtual con el ejecutable de Python especificado
                    bat "\"${env.PYTHON_PATH}\" -m venv venv"  // Crea un entorno virtual
                    bat "\"${env.PYTHON_PATH}\" -m pip install --upgrade pip"  // Actualiza pip
                    bat "\"${env.PYTHON_PATH}\" -m pip install -r requirements.txt"  // Instala dependencias
                    bat "\"${env.PYTHON_PATH}\" -m pip install selenium"  // Instalar Selenium
                }
            }
        }

        stage('Ejecución de tests unitarios') {
            steps {
                script {
                    echo 'Ejecutando tests unitarios...'
                    // Ejecuta los tests con unittest
                    bat "\"${env.PYTHON_PATH}\" -m unittest discover -s testselenium"
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
                 body: 'Hubo un error al ejecutar los tests. Revisa Jenkins para más detalles por favor.'
        }
    }
}




