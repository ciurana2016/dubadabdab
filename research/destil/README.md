# Flujo de funcionamiento

Asi funciona la proteccion:
1. Todas las peticiones inicialmente descargan un .html de "destil"
2. Este .html descarga un .js que crea la huella digital
3. El .js hace un **POST** a dominio.com/random.js?PID=CODIGO
    - El PID aparece a saco en el .js ,se genera de lado servidor? puede ser
    ya que tengo vatios archivos con PID distintos.
    - Aparte que me doi cuenta ahora hay que sacar un HEADER ajax noseque, muy claro en el codigo easy gg
    - La huella digital esta en el parametro "p"  tipo json
    Ejemplo de huella digital generada en __ejemplo_huella.json__ (unminified y decoded)
    - La respuesta del **POST** anterior nos asigna 6 cookies (ejemplo) (max-age 30 dias creo):
        ```
        D_IID=10F7DB29-5AE5-3080-A046-F885DBE3F1CF;
        D_UID=67460C79-7568-3D7F-8169-5E6261F49D0C;
        D_ZID=B11C119B-C366-3201-8149-F329F88B7256;
        D_ZUID=E7C64477-3738-3830-983F-07F5C0ED6B69;
        D_HID=1C8384CB-E703-36D3-88FD-8CCB42696628;
        D_SID=81.203.18.92:1bhFy8QUBzdaOXbSLBcwUiKoTCV211lT0SxNiBemX70;
        ``` 
    - Esta respuesta vuelve con un header X-UID ```E7C64477-3738-3830-983F-07F5C0ED6B69``` , el cual es importante
    para la siguiente peticion

4.  Se hace ina peticion *GET* con las cookies anteriores y una que no se de donde sale la cual es:
        ```
        AWSALB=2pp9gUl0j3Nqa2nnJ3Oc08eHtdSTGyEvLAC5OlncQUo5AaDwNuCJNdHDjIPB0kxiAM/1J5SEncbDXgX5bIh3Is2THqv9RW29LzlhQ1gxwJJ01Dp1BrMzarE0rwLt
        ```
    - La peticion:
        ```
            GET /distil_identify_cookie.html?httpReferrer=%2F&uid=E7C64477-3738-3830-983F-07F5C0ED6B69 HTTP/1.1
            Host: www.infojobs.net
            User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
            Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
            Accept-Encoding: gzip, deflate
            DNT: 1
            Connection: close
            Referer: https://www.infojobs.net/
            Cookie: AWSALB=2pp9gUl0j3Nqa2nnJ3Oc08eHtdSTGyEvLAC5OlncQUo5AaDwNuCJNdHDjIPB0kxiAM/1J5SEncbDXgX5bIh3Is2THqv9RW29LzlhQ1gxwJJ01Dp1BrMzarE0rwLt; D_IID=10F7DB29-5AE5-3080-A046-F885DBE3F1CF; D_UID=67460C79-7568-3D7F-8169-5E6261F49D0C; D_ZID=B11C119B-C366-3201-8149-F329F88B7256; D_ZUID=E7C64477-3738-3830-983F-07F5C0ED6B69; D_HID=1C8384CB-E703-36D3-88FD-8CCB42696628; D_SID=81.203.18.92:1bhFy8QUBzdaOXbSLBcwUiKoTCV211lT0SxNiBemX70
            Upgrade-Insecure-Requests: 1
        ```
    - La respuesta es la siguiente:
        ```
            HTTP/1.1 302 Moved Temporarily
            Content-Type: text/html
            Content-Length: 154
            Connection: close
            Date: Wed, 20 Nov 2019 18:07:00 GMT
            Location: /
            Server: nginx
            X-OCL: o00
            X-PCL: p00
            X-Cache: Miss from cloudfront
            Via: 1.1 ba02bee1844aafe0e5007ff2776c8fc8.cloudfront.net (CloudFront)
            X-Amz-Cf-Pop: MAD50
            X-Amz-Cf-Id: 0KuHdcKK0mSWwG9Hl337gFcxph8OIJUj6u2jdq1xPHKhAYEXNrUgJQ==
            
            <html>
            <head><title>302 Found</title></head>
            <body bgcolor="white">
            <center><h1>302 Found</h1></center>
            <hr><center>nginx</center>
            </body>
            </html>
        ```
5. Al ser un 302 nos lleva a __Location__ que en este caso es la paginna principal, con las cookies obtenidas en los pasos anteriores, la peticion es la siguiente:

        ```
            GET / HTTP/1.1
            Host: www.infojobs.net
            User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
            Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
            Accept-Encoding: gzip, deflate
            Referer: https://www.infojobs.net/
            DNT: 1
            Connection: close
            Cookie: AWSALB=2pp9gUl0j3Nqa2nnJ3Oc08eHtdSTGyEvLAC5OlncQUo5AaDwNuCJNdHDjIPB0kxiAM/1J5SEncbDXgX5bIh3Is2THqv9RW29LzlhQ1gxwJJ01Dp1BrMzarE0rwLt; D_IID=10F7DB29-5AE5-3080-A046-F885DBE3F1CF; D_UID=67460C79-7568-3D7F-8169-5E6261F49D0C; D_ZID=B11C119B-C366-3201-8149-F329F88B7256; D_ZUID=E7C64477-3738-3830-983F-07F5C0ED6B69; D_HID=1C8384CB-E703-36D3-88FD-8CCB42696628; D_SID=81.203.18.92:1bhFy8QUBzdaOXbSLBcwUiKoTCV211lT0SxNiBemX70
            Upgrade-Insecure-Requests: 1
        ```
        
6. Conclusion>
    * Se hace POST huella digital, lo cual devuelve unas cookies y un header.
    * Se hace un GET pasando el header por url y las cookies. (supongo que testea algo en el back)
    * El get devuelve un 302 el cual con las cookies ya puede hacer peticiones.

