# api
Tienen una API en api.infojobs.net

Pero no dejan registrar nuevas apps.

Aunque dentro de la web hay un formulario de testeo, que devuelve,
resultados REALES, y esta web no tiene proteccion anti robots,
por lo tanto podemos crear un robot que haga peticiones de test a su API
a traves de esta web y recoja los resultados.

El problema es que para validar acciones de tu cuenta a la API, si que pasa
por un subdominio protegido, __www.infojobs.net__, hay que testear a ver que pasa
si nos saltamos esa redireccion y la cambiamos con burp.