# glances es una plataforma que permite monitorear el hw de una máquina

## para ejecutarlo:

    cd glances
    docker compose up -d

# este servicio servicio se accede por el puerto 61208, para lo cual requiere levantar un tunel asi:

    ssh -i si7016student.pem ubuntu@13.56.167.51 -L 61208:localhost:61208

## abra un navegador en su máquina, y entre a:

    localhost:61208

## explore los recursos de hw de la máquina a monitear.