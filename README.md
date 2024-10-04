# LogisticaSA-CloudSolution

Este repositorio contiene la solución propuesta para el caso de uso "Logística Inteligente S.A.", una empresa ficticia dedicada a la gestión y optimización de rutas de entrega para empresas de transporte. La solución utiliza servicios de AWS como EC2, RDS, Lambda y Elasticache, junto con algoritmos de optimización desarrollados en Python y contenerizados con Docker.

## Descripción del Proyecto

La empresa busca mejorar la eficiencia de las rutas de entrega utilizando algoritmos de optimización. Se ha diseñado una arquitectura en la nube basada en AWS para procesar datos de rutas, almacenar información de clientes y ejecutar algoritmos de optimización bajo demanda.

### Arquitectura Propuesta

- **EC2**: Para procesamiento de datos de rutas.
- **RDS**: Almacenamiento de información de clientes y rutas.
- **Docker**: Contenerización de los modelos de optimización de rutas.
- **Lambda**: Ejecución a demanda de algoritmos de optimización.
- **Elasticache**: Aceleración de consultas geográficas.


MIT License

Copyright (c) 2024 Grupo 5

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
