# GUION VIDEO

Hola, soy Victor y hoy te voy a enseñar como he creado un robot para automatizar busquedas de trabajo, ya que soy programador, y si eres programador y no automatizas las partes aburridas y repetitivas de la vida, __zoom cara__ ¿realmente eres programador?

__Este vídeo es un poco tecnico, aviso.__

La idea era simple, hacer peticiones con un lenguaje de programación para imitar las acciones que hariamos a mano, pero a lo bestia. Así que con Python y Requests podemos escribir el siguiente codigo para conseguir ofertas de trabajo de infojobs y... espera un momento esto no es infojobs.
__Codigo simple y respuesta__

Problema número uno, infojobs tiene contratdo un sistema antirobots diseñado para bloquear justamente lo que queremos hacer. Mas adelante exploicaré como funciona.

En este punto decidí busacar un poco más de información sobre infojobs, y mirando los registros DNS __dnsdump mostrar__ me dí cuenta de que tenían una API. Y al buscar sobre ella en Google __vid buscando en google__ ¡Una API para la pagina que quiero automatizar creada en 2012, GENIAL! __haciendo zoom en la pagina principal abajo a la derecha al 2012__

¡Bueno vamos a crear una app! __clickamos en create, inicio con pass, y mostrar el texto de que no se pueden crear apis, color blanco y negro__ Bien tienen una API y no se puede usar, lo cual es una putada, ya que esta muy bien documentada, tiene ejemplos, errores y una consola de test para probar tus peticiones... __ir diciendo al ir esneñando (entoncación y puntuación importantes)__ 

__Cuando digo y una consola para probar, enviar una petición y...__ Espera, esta petición, devuelve una respuesta valida de la API. Y esta oferta es de verdad.

__EMOJI__ Y si mi robot en vez de atacar a infojobs.net, hiciera lo siguiente __mostrar dibujitos__ Enviamos peticiones a developer.infojobs.net, las cuales van a un backend que interactua con la API, y literalmente usamos la API CERRADA, usando este panel de "test" como proxy __MAS EMOJI__ 

__Mostrar codigo en python de un get offers__
¡FUNCIONA!

El problema viene cuando queremos interactuar con nuestra cuenta, ya que tenemos que dar permiso a la aplicación para interactuar con la API por nosotros. La misma web nos da la url para hacerlo, pero el problema, es que está bajo el dominio de __infojobs.net__ el cual si recuerdas, esta protegido por un sistema antibots.

Así que llegados a este punto me dije a mi mismo, voy a intentar hacer ingenieria inversa para ver si puedo saltarme este sistema, ¿Que podría salir mal? __mientras hago la pregunta, mostrar https://www.distilnetworks.com/block-bot-detection/ MACHINE LEARNING, salir resaltandolo con el cursor__

Sinceramente, fue mucho mas fácil de lo que pensaba, supuestamente el javascript que se carga aqui __html__ crea una "huella digital", con datos como tu cpu, sistema operativo, tamaño de la pantalla y "proof of work" para demostrar que el js ha cargado y ha sido ejecutado en un navegador.

Vamos a ver esta huella digital __usamos burp sacamos la huella, la decodificamos, la pasamos a unmin js__, todos estos datos los podemos copiar y pegar en una peticion falsa para emular que nuestro navegador ha hecho algo con el javascript, excepto este parametro __zoom proof__, aunque si eres programador esta parte ya sabes cual es __subrayar timenow__, __al cabo de dos segundos poner respuesta en js en la pantalla__, y este trozo de 20 caracteres del final que parece un montón de mierda aleatoria... __sight__  Efectivamente es un montón de mierda aleatoria, no me hizo falta ni leerme el codigo fuente, __subrayar string largoabc__ al ver esto ya supe que estaba pasando.

Y al terminar nuestra huya digital falsa todo funcionó a la perfección, __mostrar burp una petición con una huella que ponga el navegador DE MENTIRA LOL__, el sitema antibots te devuelve unas cookies, y con ellas haces una petición para conseguir navegando, y LISTO!

Tras unos cuantos días trasteando con codigo ageno la siguiente herramienta surgió:
__mostrar pantalla terminal__

Codigo fuente en github.com/ciurana2016

Y eso es todo, si mi bot te ha contactado y tienes una oferta de trabajo de algo divertido enviame un email a admin"victorciurana.com

__exit() , 1 segundo de tv rota con sonido irritante y fin video__


