# Tarea 3 Sistemas Distribuidos

Para levantar el contenedor:

```
docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
```