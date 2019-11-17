# api
Tienen una API en api.infojobs.net

Pero no dejan registrar nuevas apps.

Aunque dentro de la web hay un formulario de testeo, que devuelve,
resultados REALES, y esta web no tiene proteccion anti robots,
por lo tanto podemos crear un robot que haga peticiones de test a su API
a traves de esta web y recoja los resultados.

Aparte, se ve que hay apartados que requieren autorizacion por parte
del usuario, salta un iframe para aceptar, pero el navegador no lo carga,
PERO, si abrimos el contenido del iframe en otra pantlala y aceptamos,
hacemos la peticion de nuevo y funciona lol.

EJEMPLO
///
https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?scope=COVER_LETTER_WRITE&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=COVER_LETTER_WRITE
///

LOL FUNCIONA HHAHAH
