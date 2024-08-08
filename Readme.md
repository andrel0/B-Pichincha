# DevOps Exercise

## Descripción

Este proyecto implementa un microservicio en python con un endpoint REST `/DevOps` que responde a solicitudes POST con un mensaje personalizado. El microservicio está
asegurado con una API Key y está contenerizado para su despliegue en cualquier entorno. En caso que el metodo no sea el correcto la respuesta devolverá error.

## Requisitos para el proyecto

- Docker / Docker Desktop ( registry local )
- Minikube
- Azure DevOps - Azure Pipelines

## Instalación y Configuracion de ambientes ( Local y Nube )

1. wsl --install

2. Descargar, instalar  y configurar Registry local y Docker Desktop:

Invoke-WebRequest -Uri "https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe" -OutFile "DockerDesktopInstaller.exe"
Start-Process -Wait -FilePath ".\DockerDesktopInstaller.exe"

docker run -d -p 5000:5000 --name registry registry:2


3. Descargar e instalar Minikube:

Invoke-WebRequest -Uri "https://storage.googleapis.com/minikube/releases/latest/minikube-installer.exe" -OutFile "minikube-installer.exe"
Start-Process -Wait -FilePath ".\minikube-installer.exe"

Iniciar Minikube:
minikube start --driver=docker


4. Descargar e instalar el agente de Azure DevOps: 

Ve a tu organización en Azure DevOps.

Navegar hacia Project settings > Agent pools.
Selecciona Default (o crear un nuevo pool para asignar VM o equipo local).

Click en New agent y seguir las instrucciones para descargar el agente.

Configurar el agente ( Powershell)

.\config.cmd --unattended --url https://dev.azure.com/BancoPichincha --auth pat --token tu_token --pool default --agent tu_agente --runAsService


5. Adaptar el pipeline para usar el agente local y desplegar en Minikube

6. Configurar las Variables de Entorno en Azure DevOps:
dockerRegistryServiceConnection: Conexión al registro de Docker donde se almacenará la imagen.
MINIKUBE_IP: Dirección IP de tu Minikube.
MINIKUBE_PASSWORD: Contraseña para acceder a Minikube.

7. Ejecutar el Pipeline
Verificar que el pipeline se ejecute correctamente, compilando la imagen Docker, subiéndola al registro y desplegándola en Minikube.

8. Verificar el Despliegue
Acceder a Minikube y verificar que los pods, replicaset y servicios estén corriendo correctamente:
kubectl rs
kubectl get pods
kubectl get services

Clonar el repositorio:
git clone <URL_DEL_REPOSITORIO>


# Repositorio personal J. C. Carresi en github : 
https://github.com/andrel0/B-Pichincha