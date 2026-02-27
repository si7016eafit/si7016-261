# Ollama

## ollama es una plataforma para uso de modelos abiertos LLM.

## entrar al sitio https://ollama.com y leer que tipo de servicios puedo implementar con esta plataforma.

## permite implementar un servicio similar a chatgpt con una variedad de modelos.

## esta versión está dockerizada, se requiere que instale docker en la máquina, con buena CPU, Memoria y una GPU mínimo Nvidia T4.

## para ejecutar el servicio:

### hardware requerido:

    Máquina EC2 en Amazon, g4dn.xlarge, con Sistema Operativo Ubuntu 24.04

    Ya los alumnos tienen las credenciales para acceso al servicio.

    Cuando requieran trabajar en la máquina, entran a la consola de amazon, suben la máquina virtual y cuando ya hayan terminado de trabajar, bajan la máquina virtual.

    Conectarse a la máquina de forma remota:

    ssh -i si7016student.pem ubuntu@13.56.167.51

## ejecutar ollama:

    1. en el directorio propio de cada estudiante, clone el repositorio:
    
    ejemplo:

    (pytorch) ubuntu@ip-172-31-31-28:~/emontoya/si7016-261/lecture05$ cd ollama/
    (pytorch) ubuntu@ip-172-31-31-28:~/emontoya/si7016-261/lecture05/ollama$ docker compose up -d

    2. cree un tunnel desde su máquina local, para conectarse a ollama por el puerto 30000

    ssh -i si7016student.pem ubuntu@13.56.167.51 -L 3000:localhost:3000

    3. abra un navegador en su máquina, y entre a:

    localhost:3000

    4. despues que cree una cuenta de administrador, agregue un modelo.

    Settings del usuario (parte superior derecha - icono naranjado)
    Admin Panel
    Settings
    Models
    Manage
    Pull a model from Ollama.com.     (click en la lista de modelos para que los explore)
    <digite algun nombre típico de modelo: mistral, gpt-oss, qwen2.5, deepseek-r1, etc

    adicione, al menos 3 modelos.

    5. entre a la interfaz de consulta tipo chatgpt, y realice varias consultas.... comparé entre los diferentes modelos. Tome tiempos de respuesta.

    6. de acuerdo a las características leidas en https://ollama.com, ¿Qué tipo de aplicaciones se pueden realizar en el marco de la materia SI7016?





