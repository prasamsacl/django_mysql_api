<h1>Call&amp;Eat Fin Ciclo </h1>

![Logo proyecto-Photoroom png-Photoroom](https://github.com/prasamsacl/Call-Eat/assets/113896447/e6cf4aab-91a4-4e95-99ed-6938f0d4dba0)

  <p align="left">

 <section id="insignias">
        <div class="badge-container">
            <a href="https://github.com/prettier/prettier">
                      <a href="#">
                <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green" alt="Status">
            </a>
                <img src="https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square" alt="code style: prettier">
            </a>
            <a href="https://github.com/tu-usuario/tu-repo/actions">
                <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build Status">
            </a>
            <a href="https://github.com/tu-usuario/tu-repo/blob/main/LICENSE">
                <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
            </a>
            <a href="https://github.com/tu-usuario/tu-repo">
                <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
            </a>
            <a href="https://github.com/tu-usuario/tu-repo">
                <img src="https://img.shields.io/badge/coverage-80%25-yellow" alt="Code Coverage">
            </a>
        </div>
    </section>

<nav>
        <h2>Índice</h2>
        <ol>
            <br>
          ✍️<a href="#descripcion">Descripción del Proyecto y ámbito de implementación</a>✍️
        </br>
            <br>  💻<a href="#estado">Temporalización del proyecto y fases de desarrollo</a>💻</br>
           <br>🛠️ <a href="#demostracion">Recursos de hardware y software</a>🛠️</br>
           <br>📁 <a href="#acceso">Arquitectura software y de sistemas</a>📁 </br>
             <br> 🔨 <a href="#tecnologias">Descripción de datos</a>🔨</br
        </ol>
    </nav>
  <ol>  
 <li><h4>Descripción del Proyecto y ámbito de implementación</h4></li>
 Call&Eat es un proyecto enfocado en mejorar la experiencia de entrega de alimentos a domicilio para los clientes del establecimiento físico Call&Eat. La plataforma consiste en un sitio web que permite a los clientes realizar pedidos de comida desde la comodidad de sus hogares, ofreciendo comodidad y variedad.

Para desarrollar esta plataforma, he decidido utilizar una combinación de tecnologías modernas que garantizan un rendimiento óptimo y una experiencia de usuario fluida y segura. En el lado del servidor, estoy utilizando Django REST Framework en conjunto con MySQL como base de datos para gestionar los datos y proporcionar una API REST. Django REST Framework me brinda un conjunto completo de herramientas para manejar operaciones CRUD de manera eficiente, mientras que MySQL me ofrece un almacenamiento seguro y escalable para los datos de mi aplicación.

En el frontend, estoy utilizando React.js junto con React Hooks y React Router para construir una interfaz de usuario interactiva y dinámica. React.js me permite crear componentes modulares y reutilizables, mientras que React Hooks simplifica la gestión del estado y el ciclo de vida de mis componentes. React Router, por otro lado, facilita la navegación dentro de la aplicación al permitirme definir rutas y enlaces entre diferentes componentes de manera declarativa.
Para el diseño y la maquetación del sitio web, estoy utilizando Bootstrap, que me proporciona un conjunto de herramientas y estilos predefinidos para crear una interfaz de usuario atractiva y responsive de manera rápida y sencilla.

En resumen, Call&Eat es una plataforma web diseñada para mejorar la experiencia de entrega de alimentos a domicilio, utilizando tecnologías modernas tanto en el backend como en el frontend para garantizar una experiencia de usuario óptima. Con futuras mejoras planeadas, estamos comprometidos a seguir satisfaciendo las necesidades y preferencias de nuestros usuarios en un mercado en constante evolución.


<li><h4>Temporalización del proyecto y fases de desarrollo</h4></li>
🏗️Proyecto en construcción 🏗️


<li><h4>Retos y Aprendizajes Significativos</h4></li>

Durante el desarrollo del proyecto, nos enfrentamos a varios desafíos y aprendimos muchas lecciones importantes:
Aprendizaje de nuevas tecnologías: La curva de aprendizaje para algunas tecnologías nuevas fue más empinada de lo esperado, especialmente al aprender a utilizar un nuevo framework o herramienta.
Problemas de integración: Integrar diferentes componentes del sistema o trabajar con sistemas existentes presentó desafíos inesperados que requirieron tiempo adicional para resolver.
Gestión del tiempo: Mantener el proyecto en marcha dentro del plazo establecido fue un desafío, especialmente al enfrentarnos a cambios en los requisitos o problemas técnicos inesperados.
Comunicación con el cliente: Asegurar una comunicación clara y efectiva con el cliente a lo largo del proyecto fue fundamental para comprender y abordar adecuadamente sus necesidades y expectativas.

  
<li><h4>Recursos de hardware y software</h4></li>
<h2>Hardware</h2>
HP Pavilion x360 convertible 14-dy1xxx, utilizo el siguiente hardware:
Procesador: Intel Core i5 de 11ª generación o superior
Memoria RAM: 8 GB (actualizable a 16 GB si es necesario para un mejor rendimiento)
Tarjeta Gráfica: Gráficos integrados Intel Iris Xe
Espacio en Disco Duro: SSD de 256 GB o 512 GB
Conectividad: Wi-Fi 6, Bluetooth 5.0, puertos USB tipo A y C, HDMI

<h2><h4>Software</h4></h2>
Sistema Operativo:
Windows 10 Home o Pro (actualizable a Windows 11)
Entornos de Desarrollo Integrado (IDE):
Visual Studio Code (versión 1.60 o superior)
Frameworks y Bibliotecas de Desarrollo:
Django (versión 3.2 o superior)
React (versión 17 o superior)
Django REST Framework para API REST
MySQL para la gestión de bases de datos
React Hooks y React Router para la gestión de estado y navegación en React
Bootstrap para el diseño y estilos
Sistemas de Control de Versiones:
Git (versión 2.30 o superior)
GitHub para gestión de repositorios
Navegador Web:
Google Chrome (versión 90 o superior)
Mozilla Firefox (versión 88 o superior)

<li><h4>Arquitectura software y de sistemas</h4></li>
  Actores humanos: Clientes de Call&Eat. 
Comunicación entre elementos: Los clientes interactúan con la aplicación a través de una interfaz de usuario web o móvil. Las solicitudes de los clientes se envían al servidor de la aplicación Call&Eat a través de Internet. El servidor procesa estas solicitudes, accede a la base de datos para recuperar la información necesaria, como los detalles de los platos y los menús, y genera respuestas apropiadas que se envían de vuelta al cliente. Se sigue una arquitectura cliente-servidor, donde el cliente puede ser un navegador web en una computadora de escritorio o un dispositivo móvil, y el servidor es la aplicación web alojada en un servidor remoto que gestiona todas las operaciones y lógica de negocio de Call&Eat.

<li><h4>Descripción de datos</h4></li>
Call&Eat es una plataforma que ofrece una experiencia completa de pedido de comida, comenzando con una página principal que presenta imágenes atractivas y una descripción del servicio. La sección de la carta muestra una variedad de platos organizados por categorías, mientras que la carta semanal ofrece menús fijos para cada día de la semana, incluyendo primer plato, segundo plato y postre, todo a un precio fijo. Los usuarios pueden explorar una galería de imágenes para ver los platos destacados o el ambiente del local. La sección de contacto proporciona información detallada del local, como dirección y número de teléfono. La cesta de la compra permite a los usuarios seleccionar platos y gestionar su pedido, mientras que el proceso de pago finaliza la transacción, generando un recibo del pedido con detalles de los platos seleccionados y el total a pagar.


<li><h4>PERSONAS DESARROLLADORAS DEL PROYECTO</h4></li>
Prasamsa Castelao López

<li><h4>LICENCIA</h4></li>
<section id="insignias">
        <div class="badge-container">
            <a href="https://github.com/prettier/prettier">
                      <a href="#">
                <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green" alt="Status">
            </a>
                <img src="https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square" alt="code style: prettier">
            </a>
            <a href="https://github.com/tu-usuario/tu-repo/actions">
                <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build Status">
            </a>
            <a href="https://github.com/tu-usuario/tu-repo/blob/main/LICENSE">
                <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
            </a>
            <a href="https://github.com/tu-usuario/tu-repo">
                <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
            </a>
            <a href="https://github.com/tu-usuario/tu-repo">
                <img src="https://img.shields.io/badge/coverage-80%25-yellow" alt="Code Coverage">
            </a>
        </div>
    </section>
</ol>

