## Como executar
O unico requisito necessario é o docker. :heart_eyes:

Após instalar o docker rodar os seguintes comandos com privilegios de administrador (no linux sudo no windows eu não sei):  

```
docker build -t backend https://gitlab.com/KaianFSantos/venus.git#master:backend
```
```
docker run -d -p 8080:8080 backend
```

## Dicas uteis docker :whale:
Quando rodamos os comandos acima criamos uma imagem (Algo parecido como uma imagem de emulador), é possivel listar remover e etc.
Tambem é criado um container algo parecido com um emulador de sistema operacional porem muito mais leve.

O espaço ocupado pelo projeto é de 200MB o preço a se pagar pela praticidade do docker :stuck_out_tongue_closed_eyes:

comandos:

 imagens-> https://docs.docker.com/engine/reference/commandline/image/

 containers -> https://docs.docker.com/engine/reference/commandline/docker/
 
## Tambem pode ser utilizado sem docker :unamused:

O requisito é possuir o Python 3 na sua maquina e executar o seguinte comando nessa pasta

```
pip install -r requirements.txt
```


## Endpoints da API
Para verficar os endpoints importar no postman "endpoints_postman.txt"

