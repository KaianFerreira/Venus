## Como executar
O unico requisito necessario é o docker. :heart_eyes:

Após instalar o docker rodar os seguintes comandos com privilegios de administrador (no linux sudo no windows eu não sei):  
docker build https://gitlab.com/KaianFSantos/venus.git#master:backend

docker run -d -p 8080:8080 backend

## Endpoints da API
Para verficar os endpoints importar no postman "endpoints_postman.txt"

## Dicas uteis docker
Quando rodamos os comandos acima criamos uma imagem (Algo parecido como uma imagem de emulador), é possivel listar remover e etc.
Tambem é criado um container algo parecido com um emulador de sistema operacional porem muito mais leve.

O espaço ocupado pelo projeto é de 200MB o preço a se pagar pela praticidade do docker :stuck_out_tongue_closed_eyes:

comandos:
 imagens-> https://docs.docker.com/engine/reference/commandline/image/

 containers -> https://docs.docker.com/engine/reference/commandline/docker/