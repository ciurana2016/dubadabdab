## Antes de nada lista de cookies y funcionalidad
https://www.infojobs.net/cookies-policy-i.xhtml 

Enlace del Iframe:
### https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL
    
El formulario en el enlace anterior ataca a (con user y pass):
### https://accounts.infojobs.net/security/accounts/login/run
__General__
    Request URL: https://accounts.infojobs.net/security/accounts/login/run
    Referrer Policy: no-referrer-when-downgrade

__Request headers__
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Origin' : 'https://www.infojobs.net',
    'Referer' : 'https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL',
    'Sec-Fetch-User' : '?1',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',

__Form data__
    client_id: empleo_ij
    login_url_type: WEB
    login_type: 3
    email: admin@victorciurana.com
    password: PASS

Se cancela automaticamente y vuelve (302) a hacer un POST:
### https://accounts.infojobs.net/security/accounts/login/run 
__General__
    Request URL: https://accounts.infojobs.net/security/accounts/login/run
    Request Method: POST
    Status Code: 302 
    Remote Address: 34.241.90.231:443
    Referrer Policy: no-referrer-when-downgrade

__Response headers__
    content-encoding: gzip
    content-language: es
    content-length: 20
    content-type: text/html; charset=windows-1252
    date: Mon, 18 Nov 2019 19:43:09 GMT
    location: https://accounts.infojobs.net/oauth/user/authorize?client_id=empleo_ij&redirect_uri=https://www.infojobs.net/security/accounts/login-redirect/run&response_type=code&login_type=3
    server: Apache
    set-cookie: AWSALB=a7iyk6rQ0oGue14creO1egBsH1oWfgNc+V+Q9H2/OPAr3+Z5WY16aQcq7bzJBS/VxL2N77ZInCSMRuLWBYrRguH0lPPKlv+dB2U7w3zGkagfOkdI7zdBn1OgIK9p; Expires=Mon, 25 Nov 2019 19:43:08 GMT; Path=/
    set-cookie: JSESSIONID=ktxCwypU8IRJQr+Cw-H5Rdck; Path=/; Secure
    set-cookie: IJCUE=DBGfsYAvtvUyLHMF4d366F%252FRcYadklCfaSqBfGNxMOUpzSFHtn7eKJ2vmyBsvS2Y9ThSh6bv; Domain=accounts.infojobs.net; Path=/; HttpOnly
    set-cookie: IJCUS=DKyFUpptEGs3mxJe64J5419WwWBUVrGyXCZM9uNIiYMNLuGSjqHCk3LIQBzNOxeQ0S3p0nnSDdHB%250AaNsaytfhalkroCLZKjEhSdxARx8X%252BabOt%252BSEXa69c6%252BB6oAHmD16qbXyPvrnfnI%253D; Domain=accounts.infojobs.net; Path=/; Secure; HttpOnly
    set-cookie: IJCUG=DIfK%252FqxW0VWdb3uNG73EBL6h1b6mdq51UDuSTP33nkfUfy%252Fnda0Z0XssGGNC6cNRYDot6Lm84nHK%250ADnrb5aKIxMFJnYEGCc1%252F3J0%253D; Domain=.infojobs.net; Path=/; HttpOnly
    set-cookie: IJAuthenticationSuccess=true; Domain=.infojobs.net; Path=/; Secure
    status: 302
    strict-transport-security: max-age=63072000; includeSubdomains;
    vary: Accept-Encoding,User-Agent

__Request headers__
    :authority: accounts.infojobs.net
    :method: POST
    :path: /security/accounts/login/run
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    accept-encoding: gzip, deflate, br
    accept-language: es-ES,es;q=0.9,en;q=0.8
    cache-control: max-age=0
    content-length: 104
    content-type: application/x-www-form-urlencoded
    cookie: JSESSIONID=cPvCnJilSWiVCyckyLHWPvRh; IJTESTUID=64331fa7-d2da-44c0-963e-824690f88518; IJUSERUID=05708230-19af-4e2d-bd06-072eb2a26dbd; ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c; test-cookie=to%20be%20or%20not%20to%20be; ajs_user_id=null; ajs_group_id=null; utag_main=v_id:016e800960f6001b4dc828cb4e5d0307800cc07000bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574107928630$ses_id:1574106128630%3Bexp-session$vapi_domain:infojobs.net; AMCVS_05FF6243578784B37F000101%40AdobeOrg=1; s_cc=true; _pulse2data=211a477e-747c-4e1a-a601-04397280acf3%2Cv%2C%2C1574107029556%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMThUMTk6NDI6MDlaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..7tQ_Nncoxx5_qewI5KH73g.oB5v4-XdTeuIv4vtr60ps5Sp2qj83jEMsZR8kAsORn5uV_pwkfZsMO-RP9O7B2qrdFzY2KX_6iFJGbHirAMwWCBsq5AwSYUJ0gWS762FEiGMGDh1AuHVJLmjCiIPhHYBLf9xtNIswYH7clyaUJ0KAyPdt4HSygqjjWpKVN8LuFaM-2kqkaH9uFVcvTmODw7XdxAvyZuUdDdpS-JtJfMJig.-cNiBQXIva_E7XVxILv9jw%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..xSr_EzSygIhSK0DGpwv5V35MMc25W8p-IHLf-opY1B4; AMCV_05FF6243578784B37F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18219%7CMCMID%7C32684227982076427600498174367758074122%7CMCAAMLH-1574710928%7C6%7CMCAAMB-1574710928%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1574113329s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18226%7CvVersion%7C4.3.0; s_sq=schibstedspainjobsinfojobsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dother%2526link%253DIniciar%252520sesi%2525C3%2525B3n%2526region%253Dapi-login-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dother%2526pidt%253D1%2526oid%253DIniciar%252520sesi%2525C3%2525B3n%2526oidt%253D3%2526ot%253DSUBMIT
    origin: https://www.infojobs.net
    referer: https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL
    sec-fetch-mode: navigate
    sec-fetch-site: same-site
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36

__Form data__
    client_id: empleo_ij
    login_url_type: WEB
    login_type: 3
    email: admin@victorciurana.com
    password: PASS

Salta a "Oauth", ya que supongo que el login lo hizo bien anteriormente
### https://accounts.infojobs.net/oauth/user/authorize?client_id=empleo_ij&redirect_uri=https://www.infojobs.net/security/accounts/login-redirect/run&response_type=code&login_type=3
__General__
    Request URL: https://accounts.infojobs.net/oauth/user/authorize?client_id=empleo_ij&redirect_uri=https://www.infojobs.net/security/accounts/login-redirect/run&response_type=code&login_type=3
    Request Method: GET
    Status Code: 302 
    Remote Address: 34.241.90.231:443
    Referrer Policy: no-referrer-when-downgrade

__Response headers__
    content-encoding: gzip
    content-language: es
    content-length: 20
    content-type: text/html; charset=windows-1252
    date: Mon, 18 Nov 2019 19:43:09 GMT
    location: https://www.infojobs.net/security/accounts/login-redirect/run?code=9b25ba5f-ad4d-476f-b1d9-2eea35865b07&login_type=3
    server: Apache
    set-cookie: AWSALB=raxr2UIVetKW7Dxsi6RQiPwf4EI+qtQ8CsIZCmm5nETIgEJzuKxYZI4w8qRDVRu+PXJTCsQW/5DJ6eJEyC9ZGMvhvAl0/HQZ9JsvyUQ//pXZe7d+Bq4LZZEtgIb9; Expires=Mon, 25 Nov 2019 19:43:09 GMT; Path=/
    status: 302
    strict-transport-security: max-age=63072000; includeSubdomains;
    vary: Accept-Encoding,User-Agent

__Request headers__
    :authority: accounts.infojobs.net
    :method: GET
    :path: /oauth/user/authorize?client_id=empleo_ij&redirect_uri=https://www.infojobs.net/security/accounts/login-redirect/run&response_type=code&login_type=3
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    accept-encoding: gzip, deflate, br
    accept-language: es-ES,es;q=0.9,en;q=0.8
    cache-control: max-age=0
    cookie: JSESSIONID=cPvCnJilSWiVCyckyLHWPvRh; IJTESTUID=64331fa7-d2da-44c0-963e-824690f88518; IJUSERUID=05708230-19af-4e2d-bd06-072eb2a26dbd; ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c; test-cookie=to%20be%20or%20not%20to%20be; ajs_user_id=null; ajs_group_id=null; utag_main=v_id:016e800960f6001b4dc828cb4e5d0307800cc07000bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574107928630$ses_id:1574106128630%3Bexp-session$vapi_domain:infojobs.net; AMCVS_05FF6243578784B37F000101%40AdobeOrg=1; s_cc=true; _pulse2data=211a477e-747c-4e1a-a601-04397280acf3%2Cv%2C%2C1574107029556%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMThUMTk6NDI6MDlaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..7tQ_Nncoxx5_qewI5KH73g.oB5v4-XdTeuIv4vtr60ps5Sp2qj83jEMsZR8kAsORn5uV_pwkfZsMO-RP9O7B2qrdFzY2KX_6iFJGbHirAMwWCBsq5AwSYUJ0gWS762FEiGMGDh1AuHVJLmjCiIPhHYBLf9xtNIswYH7clyaUJ0KAyPdt4HSygqjjWpKVN8LuFaM-2kqkaH9uFVcvTmODw7XdxAvyZuUdDdpS-JtJfMJig.-cNiBQXIva_E7XVxILv9jw%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..xSr_EzSygIhSK0DGpwv5V35MMc25W8p-IHLf-opY1B4; AMCV_05FF6243578784B37F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18219%7CMCMID%7C32684227982076427600498174367758074122%7CMCAAMLH-1574710928%7C6%7CMCAAMB-1574710928%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1574113329s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18226%7CvVersion%7C4.3.0; s_sq=schibstedspainjobsinfojobsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dother%2526link%253DIniciar%252520sesi%2525C3%2525B3n%2526region%253Dapi-login-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dother%2526pidt%253D1%2526oid%253DIniciar%252520sesi%2525C3%2525B3n%2526oidt%253D3%2526ot%253DSUBMIT; AWSALB=a7iyk6rQ0oGue14creO1egBsH1oWfgNc+V+Q9H2/OPAr3+Z5WY16aQcq7bzJBS/VxL2N77ZInCSMRuLWBYrRguH0lPPKlv+dB2U7w3zGkagfOkdI7zdBn1OgIK9p; JSESSIONID=ktxCwypU8IRJQr+Cw-H5Rdck; IJCUE=DBGfsYAvtvUyLHMF4d366F%252FRcYadklCfaSqBfGNxMOUpzSFHtn7eKJ2vmyBsvS2Y9ThSh6bv; IJCUS=DKyFUpptEGs3mxJe64J5419WwWBUVrGyXCZM9uNIiYMNLuGSjqHCk3LIQBzNOxeQ0S3p0nnSDdHB%250AaNsaytfhalkroCLZKjEhSdxARx8X%252BabOt%252BSEXa69c6%252BB6oAHmD16qbXyPvrnfnI%253D; IJCUG=DIfK%252FqxW0VWdb3uNG73EBL6h1b6mdq51UDuSTP33nkfUfy%252Fnda0Z0XssGGNC6cNRYDot6Lm84nHK%250ADnrb5aKIxMFJnYEGCc1%252F3J0%253D; IJAuthenticationSuccess=true
    referer: https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL
    sec-fetch-mode: navigate
    sec-fetch-site: same-site
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36

__Query String Parameters__
    client_id: empleo_ij
    redirect_uri: https://www.infojobs.net/security/accounts/login-redirect/run
    response_type: code
    login_type: 3

Salta otra vez nose porque, al acabar el oauth ? nuse
### https://www.infojobs.net/security/accounts/login-redirect/run?code=9b25ba5f-ad4d-476f-b1d9-2eea35865b07&login_type=3
__General__
    Request URL: https://www.infojobs.net/security/accounts/login-redirect/run?code=9b25ba5f-ad4d-476f-b1d9-2eea35865b07&login_type=3
    Request Method: GET
    Status Code: 302 
    Remote Address: 52.85.47.133:443
    Referrer Policy: no-referrer-when-downgrade

__Response headers__
    content-language: es,es-es
    content-length: 0
    content-security-policy: frame-ancestors 'self' *.optimizely.com *.optimizelyedit.com *.adobe.com;
    content-type: text/html; charset=windows-1252
    date: Mon, 18 Nov 2019 19:43:09 GMT
    location: https://www.infojobs.net/security/accounts/login-redirect/reproduce-request.xhtml?login_type=3&dgv=4722324540640591273
    p3p: CP="CAO PSA OUR"
    server: nginx
    set-cookie: AWSALB=EFQyRQlpYeoCIQoReQbPXFRZZRHK4PSA6K1X3+XKcG8/2zNcRzN7n7LnjBzcLv2SDMFz7BY+ex++HN5ClSj2d7awqxxvSZivBiX9dNps+omNaR3IHi5152w3eCTX; Expires=Mon, 25 Nov 2019 19:43:09 GMT; Path=/
    set-cookie: IJS=DCKsG4di9xdvdCC9AcTPyUgrJEAEiC2bbJoB178GmAuSIfatHIktMvlR3rTm9E3Su9VaKOL9HY%2BUSoi78Dwz11USQxb71uorTd4PbQhe1pIfIGtBcg%3D%3D; Domain=www.infojobs.net; Path=/; Secure; HttpOnly
    set-cookie: IJE=DF4NXfhFOcFQm0N%2By3O7Df5vQ03gmU6qPQw7JmI33JAJKsp5E5ZWTCrulp9TSi6M5wwGtYzdzXR6AzoN; Domain=.infojobs.net; Path=/; Secure; HttpOnly
    set-cookie: IJH=DH%2BrWyywNMWqN63qGyJw0%2BNyoE%2FTydy24zSSklYzbNOhbVRJ1%2BuUA0zQ3A1CScSBX2bt17lvHWFsIbS%2FxMx6kA%3D%3D; Domain=.infojobs.net; Expires=Mon, 18-May-2020 18:43:09 GMT; Path=/; Secure; HttpOnly
    set-cookie: IJUSERNL=Victor%C2%ACCA%C2%AC38908077-2d61-4fa8-88fb-2409cc4da3ce%C2%ACseg%3D23%C2%ACprv%3D26; Domain=.infojobs.net; Expires=Sat, 06-Dec-2087 22:57:16 GMT; Path=/
    set-cookie: nfsld9d6558b2036b0758d9bfefe08f0c45d=1; Domain=.infojobs.net; Path=/
    set-cookie: IJTESTUID=64331fa7-d2da-44c0-963e-824690f88518; Domain=.infojobs.net; Expires=Thu, 19-Dec-2019 19:43:09 GMT; Path=/
    set-cookie: IJUSERUID=05708230-19af-4e2d-bd06-072eb2a26dbd; Domain=.infojobs.net; Expires=Mon, 18-Nov-2019 20:28:09 GMT; Path=/
    status: 302
    strict-transport-security: max-age=63072000; includeSubdomains;
    vary: Accept-Encoding,User-Agent
    via: 1.1 5cd3e44770ed622e884d102aff05f63e.cloudfront.net (CloudFront)
    x-amz-cf-id: kozf2CFVMNhKqPcA2kM_MJmXoO5I0_Ymd4kI5RSdpMgf3u5vIdu1RQ==
    x-amz-cf-pop: MAD50
    x-cache: Miss from cloudfront
    x-ocl: o00
    x-pcl: p00

__Request headers__
    :authority: www.infojobs.net
    :method: GET
    :path: /security/accounts/login-redirect/run?code=9b25ba5f-ad4d-476f-b1d9-2eea35865b07&login_type=3
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    accept-encoding: gzip, deflate, br
    accept-language: es-ES,es;q=0.9,en;q=0.8
    cache-control: max-age=0
    cookie: D_IID=EC05AE4C-05E7-365A-9074-298B52FE1C88; D_UID=36ECFA4C-2EC7-3262-A349-94BF4D9DB43A; D_ZID=B39930DB-57AC-3284-A5FB-D8276DC96B30; D_ZUID=76C92D11-4E34-39A6-9816-1668E84CD73B; D_HID=4228BBE2-740B-34A3-9306-0DA0BE35DCDE; D_SID=81.203.18.92:1bhFy8QUBzdaOXbSLBcwUiKoTCV211lT0SxNiBemX70; JSESSIONID=cPvCnJilSWiVCyckyLHWPvRh; IJTESTUID=64331fa7-d2da-44c0-963e-824690f88518; IJUSERUID=05708230-19af-4e2d-bd06-072eb2a26dbd; AWSALB=a/rKeQJtAvzwxrFj2h+ODxlArjIkXxP6pRJperengOvqpeAQA945/we39VfdTSSGvgjCIzke2ptrl33jGvOU8yxO+wsaReG12HUDK0rf4O4HYFhKGdOjXXERin9e; ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c; test-cookie=to%20be%20or%20not%20to%20be; ajs_user_id=null; ajs_group_id=null; IJADBLOCKER=false; utag_main=v_id:016e800960f6001b4dc828cb4e5d0307800cc07000bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574107928630$ses_id:1574106128630%3Bexp-session$vapi_domain:infojobs.net; AMCVS_05FF6243578784B37F000101%40AdobeOrg=1; s_cc=true; _pulse2data=211a477e-747c-4e1a-a601-04397280acf3%2Cv%2C%2C1574107029556%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMThUMTk6NDI6MDlaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..7tQ_Nncoxx5_qewI5KH73g.oB5v4-XdTeuIv4vtr60ps5Sp2qj83jEMsZR8kAsORn5uV_pwkfZsMO-RP9O7B2qrdFzY2KX_6iFJGbHirAMwWCBsq5AwSYUJ0gWS762FEiGMGDh1AuHVJLmjCiIPhHYBLf9xtNIswYH7clyaUJ0KAyPdt4HSygqjjWpKVN8LuFaM-2kqkaH9uFVcvTmODw7XdxAvyZuUdDdpS-JtJfMJig.-cNiBQXIva_E7XVxILv9jw%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..xSr_EzSygIhSK0DGpwv5V35MMc25W8p-IHLf-opY1B4; AMCV_05FF6243578784B37F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18219%7CMCMID%7C32684227982076427600498174367758074122%7CMCAAMLH-1574710928%7C6%7CMCAAMB-1574710928%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1574113329s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18226%7CvVersion%7C4.3.0; s_sq=schibstedspainjobsinfojobsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dother%2526link%253DIniciar%252520sesi%2525C3%2525B3n%2526region%253Dapi-login-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dother%2526pidt%253D1%2526oid%253DIniciar%252520sesi%2525C3%2525B3n%2526oidt%253D3%2526ot%253DSUBMIT; IJCUG=DIfK%252FqxW0VWdb3uNG73EBL6h1b6mdq51UDuSTP33nkfUfy%252Fnda0Z0XssGGNC6cNRYDot6Lm84nHK%250ADnrb5aKIxMFJnYEGCc1%252F3J0%253D; IJAuthenticationSuccess=true
    referer: https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL
    sec-fetch-mode: navigate
    sec-fetch-site: same-site
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36

__Query String Parameters__
    code: 9b25ba5f-ad4d-476f-b1d9-2eea35865b07
    login_type: 3

Sigue pasando cosigos y mierdas entre IPs diferentes
### https://www.infojobs.net/security/accounts/login-redirect/reproduce-request.xhtml?login_type=3&dgv=4722324540640591273
__General__
    Request URL: https://www.infojobs.net/security/accounts/login-redirect/reproduce-request.xhtml?login_type=3&dgv=4722324540640591273
    Request Method: GET
    Status Code: 302 
    Remote Address: 52.85.47.133:443
    Referrer Policy: no-referrer-when-downgrade

__Response headers__
    content-language: es
    content-length: 0
    content-security-policy: frame-ancestors 'self' *.optimizely.com *.optimizelyedit.com *.adobe.com;
    content-type: application/xhtml+xml
    date: Mon, 18 Nov 2019 19:43:09 GMT
    location: https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?scope=CANDIDATE_PROFILE_WITH_EMAIL&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=CANDIDATE_PROFILE_WITH_EMAIL&dgv=19161524573339042201
    p3p: CP="CAO PSA OUR"
    server: nginx
    set-cookie: AWSALB=cTn/94mY8YQLaYA8bud42jY74Gy67dQf1rdZ3AP0i5XiUJhv/xEXUOUhQe2pprqOhVQgF4IaQ9jeg1l8CzGGzTaURNAj1jawjizuyguxXqDmzNXXxHoogNyDz+Go; Expires=Mon, 25 Nov 2019 19:43:09 GMT; Path=/
    set-cookie: IJAuthenticationSuccess=true; Domain=.infojobs.net; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/
    set-cookie: ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c; Domain=.infojobs.net; Expires=Wed, 18-Nov-2020 01:43:09 GMT; Path=/
    set-cookie: ajs_user_id=%22sdrn%3Ainfojobs.net%3Auser%3A32128330420%22; Domain=.infojobs.net; Expires=Wed, 18-Nov-2020 01:43:09 GMT; Path=/
    set-cookie: ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c; Domain=.infojobs.net; Expires=Wed, 18-Nov-2020 01:43:09 GMT; Path=/
    status: 302
    strict-transport-security: max-age=63072000; includeSubdomains;
    vary: Accept-Encoding,User-Agent
    via: 1.1 5cd3e44770ed622e884d102aff05f63e.cloudfront.net (CloudFront)
    x-amz-cf-id: nOegISEQiIl5VVWnD17KVmhIM5Tw9CM41zAWZqH_T4qNq1RfbRYJCg==
    x-amz-cf-pop: MAD50
    x-cache: Miss from cloudfront
    x-ocl: o00
    x-pcl: p00

__Request headers__
    :authority: www.infojobs.net
    :method: GET
    :path: /security/accounts/login-redirect/reproduce-request.xhtml?login_type=3&dgv=4722324540640591273
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    accept-encoding: gzip, deflate, br
    accept-language: es-ES,es;q=0.9,en;q=0.8
    cache-control: max-age=0
    cookie: D_IID=EC05AE4C-05E7-365A-9074-298B52FE1C88; D_UID=36ECFA4C-2EC7-3262-A349-94BF4D9DB43A; D_ZID=B39930DB-57AC-3284-A5FB-D8276DC96B30; D_ZUID=76C92D11-4E34-39A6-9816-1668E84CD73B; D_HID=4228BBE2-740B-34A3-9306-0DA0BE35DCDE; D_SID=81.203.18.92:1bhFy8QUBzdaOXbSLBcwUiKoTCV211lT0SxNiBemX70; JSESSIONID=cPvCnJilSWiVCyckyLHWPvRh; IJTESTUID=64331fa7-d2da-44c0-963e-824690f88518; IJUSERUID=05708230-19af-4e2d-bd06-072eb2a26dbd; ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c; test-cookie=to%20be%20or%20not%20to%20be; ajs_user_id=null; ajs_group_id=null; IJADBLOCKER=false; utag_main=v_id:016e800960f6001b4dc828cb4e5d0307800cc07000bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574107928630$ses_id:1574106128630%3Bexp-session$vapi_domain:infojobs.net; AMCVS_05FF6243578784B37F000101%40AdobeOrg=1; s_cc=true; _pulse2data=211a477e-747c-4e1a-a601-04397280acf3%2Cv%2C%2C1574107029556%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMThUMTk6NDI6MDlaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..7tQ_Nncoxx5_qewI5KH73g.oB5v4-XdTeuIv4vtr60ps5Sp2qj83jEMsZR8kAsORn5uV_pwkfZsMO-RP9O7B2qrdFzY2KX_6iFJGbHirAMwWCBsq5AwSYUJ0gWS762FEiGMGDh1AuHVJLmjCiIPhHYBLf9xtNIswYH7clyaUJ0KAyPdt4HSygqjjWpKVN8LuFaM-2kqkaH9uFVcvTmODw7XdxAvyZuUdDdpS-JtJfMJig.-cNiBQXIva_E7XVxILv9jw%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..xSr_EzSygIhSK0DGpwv5V35MMc25W8p-IHLf-opY1B4; AMCV_05FF6243578784B37F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18219%7CMCMID%7C32684227982076427600498174367758074122%7CMCAAMLH-1574710928%7C6%7CMCAAMB-1574710928%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1574113329s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18226%7CvVersion%7C4.3.0; s_sq=schibstedspainjobsinfojobsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dother%2526link%253DIniciar%252520sesi%2525C3%2525B3n%2526region%253Dapi-login-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dother%2526pidt%253D1%2526oid%253DIniciar%252520sesi%2525C3%2525B3n%2526oidt%253D3%2526ot%253DSUBMIT; IJCUG=DIfK%252FqxW0VWdb3uNG73EBL6h1b6mdq51UDuSTP33nkfUfy%252Fnda0Z0XssGGNC6cNRYDot6Lm84nHK%250ADnrb5aKIxMFJnYEGCc1%252F3J0%253D; IJAuthenticationSuccess=true; AWSALB=EFQyRQlpYeoCIQoReQbPXFRZZRHK4PSA6K1X3+XKcG8/2zNcRzN7n7LnjBzcLv2SDMFz7BY+ex++HN5ClSj2d7awqxxvSZivBiX9dNps+omNaR3IHi5152w3eCTX; IJS=DCKsG4di9xdvdCC9AcTPyUgrJEAEiC2bbJoB178GmAuSIfatHIktMvlR3rTm9E3Su9VaKOL9HY%2BUSoi78Dwz11USQxb71uorTd4PbQhe1pIfIGtBcg%3D%3D; IJE=DF4NXfhFOcFQm0N%2By3O7Df5vQ03gmU6qPQw7JmI33JAJKsp5E5ZWTCrulp9TSi6M5wwGtYzdzXR6AzoN; IJH=DH%2BrWyywNMWqN63qGyJw0%2BNyoE%2FTydy24zSSklYzbNOhbVRJ1%2BuUA0zQ3A1CScSBX2bt17lvHWFsIbS%2FxMx6kA%3D%3D; IJUSERNL=Victor%C2%ACCA%C2%AC38908077-2d61-4fa8-88fb-2409cc4da3ce%C2%ACseg%3D23%C2%ACprv%3D26; nfsld9d6558b2036b0758d9bfefe08f0c45d=1
    referer: https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL
    sec-fetch-mode: navigate
    sec-fetch-site: same-site
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36

__Query String Parameters__
    login_type: 3
    dgv: 4722324540640591273

Otro salto ...
### https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?scope=CANDIDATE_PROFILE_WITH_EMAIL&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=CANDIDATE_PROFILE_WITH_EMAIL&dgv=19161524573339042201
__General__
    Request URL: https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?scope=CANDIDATE_PROFILE_WITH_EMAIL&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=CANDIDATE_PROFILE_WITH_EMAIL&dgv=19161524573339042201
    Request Method: GET
    Status Code: 302 
    Remote Address: 52.85.47.133:443
    Referrer Policy: no-referrer-when-downgrade

__Response headers__
    cache-control: no-cache, private
    content-language: es
    content-length: 0
    content-security-policy: frame-ancestors 'self' *.optimizely.com *.optimizelyedit.com *.adobe.com;
    content-type: application/xhtml+xml
    date: Mon, 18 Nov 2019 19:43:09 GMT
    location: https://developer.infojobs.net/test-console/continue-request.xhtml?code=06e88b03-949a-40e1-83ba-92586a5b5583&state=CANDIDATE_PROFILE_WITH_EMAIL&scopes=CANDIDATE_PROFILE_WITH_EMAIL&auth_type=api&dgv=14839528301444153507
    p3p: CP="CAO PSA OUR"
    server: nginx
    set-cookie: AWSALB=7FKkpM+oNJsE6LaD/7gO9Z5zDXh+NNHCjDWPLH8YajRcx9cg+mlULKprIgdRrNc/hNA0i6iSdr5ZK/0MG5F8r4olXnKf+x76D6x3l9yuL9zXYWQcMieWvbzmhRGz; Expires=Mon, 25 Nov 2019 19:43:09 GMT; Path=/
    set-cookie: IJE=DEf%2BsqOP62B4YbZoxeJW1ejcYMBdn3v%2B%2FsQR1kSH3hl5Bf4hc2jp5yKJt4cocXbMkopWq68gFp0tHE6Z; Domain=.infojobs.net; Path=/; Secure; HttpOnly
    status: 302
    strict-transport-security: max-age=63072000; includeSubdomains;
    vary: Accept-Encoding,User-Agent
    via: 1.1 5cd3e44770ed622e884d102aff05f63e.cloudfront.net (CloudFront)
    x-amz-cf-id: HdXtErCGWqIPYDIv2zsghTI4Kb9PfEAqxGk5ob5IPDKD-KUUHlMV3A==
    x-amz-cf-pop: MAD50
    x-cache: Miss from cloudfront
    x-ocl: o00
    x-pcl: p00

__Request headers__
    :authority: www.infojobs.net
    :method: GET
    :path: /api/oauth/user-authorize/index.xhtml?scope=CANDIDATE_PROFILE_WITH_EMAIL&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=CANDIDATE_PROFILE_WITH_EMAIL&dgv=19161524573339042201
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    accept-encoding: gzip, deflate, br
    accept-language: es-ES,es;q=0.9,en;q=0.8
    cache-control: max-age=0
    cookie: D_IID=EC05AE4C-05E7-365A-9074-298B52FE1C88; D_UID=36ECFA4C-2EC7-3262-A349-94BF4D9DB43A; D_ZID=B39930DB-57AC-3284-A5FB-D8276DC96B30; D_ZUID=76C92D11-4E34-39A6-9816-1668E84CD73B; D_HID=4228BBE2-740B-34A3-9306-0DA0BE35DCDE; D_SID=81.203.18.92:1bhFy8QUBzdaOXbSLBcwUiKoTCV211lT0SxNiBemX70; JSESSIONID=cPvCnJilSWiVCyckyLHWPvRh; IJTESTUID=64331fa7-d2da-44c0-963e-824690f88518; IJUSERUID=05708230-19af-4e2d-bd06-072eb2a26dbd; ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c; test-cookie=to%20be%20or%20not%20to%20be; ajs_group_id=null; IJADBLOCKER=false; utag_main=v_id:016e800960f6001b4dc828cb4e5d0307800cc07000bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574107928630$ses_id:1574106128630%3Bexp-session$vapi_domain:infojobs.net; AMCVS_05FF6243578784B37F000101%40AdobeOrg=1; s_cc=true; _pulse2data=211a477e-747c-4e1a-a601-04397280acf3%2Cv%2C%2C1574107029556%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMThUMTk6NDI6MDlaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..7tQ_Nncoxx5_qewI5KH73g.oB5v4-XdTeuIv4vtr60ps5Sp2qj83jEMsZR8kAsORn5uV_pwkfZsMO-RP9O7B2qrdFzY2KX_6iFJGbHirAMwWCBsq5AwSYUJ0gWS762FEiGMGDh1AuHVJLmjCiIPhHYBLf9xtNIswYH7clyaUJ0KAyPdt4HSygqjjWpKVN8LuFaM-2kqkaH9uFVcvTmODw7XdxAvyZuUdDdpS-JtJfMJig.-cNiBQXIva_E7XVxILv9jw%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..xSr_EzSygIhSK0DGpwv5V35MMc25W8p-IHLf-opY1B4; AMCV_05FF6243578784B37F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18219%7CMCMID%7C32684227982076427600498174367758074122%7CMCAAMLH-1574710928%7C6%7CMCAAMB-1574710928%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1574113329s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18226%7CvVersion%7C4.3.0; s_sq=schibstedspainjobsinfojobsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dother%2526link%253DIniciar%252520sesi%2525C3%2525B3n%2526region%253Dapi-login-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dother%2526pidt%253D1%2526oid%253DIniciar%252520sesi%2525C3%2525B3n%2526oidt%253D3%2526ot%253DSUBMIT; IJCUG=DIfK%252FqxW0VWdb3uNG73EBL6h1b6mdq51UDuSTP33nkfUfy%252Fnda0Z0XssGGNC6cNRYDot6Lm84nHK%250ADnrb5aKIxMFJnYEGCc1%252F3J0%253D; IJS=DCKsG4di9xdvdCC9AcTPyUgrJEAEiC2bbJoB178GmAuSIfatHIktMvlR3rTm9E3Su9VaKOL9HY%2BUSoi78Dwz11USQxb71uorTd4PbQhe1pIfIGtBcg%3D%3D; IJE=DF4NXfhFOcFQm0N%2By3O7Df5vQ03gmU6qPQw7JmI33JAJKsp5E5ZWTCrulp9TSi6M5wwGtYzdzXR6AzoN; IJH=DH%2BrWyywNMWqN63qGyJw0%2BNyoE%2FTydy24zSSklYzbNOhbVRJ1%2BuUA0zQ3A1CScSBX2bt17lvHWFsIbS%2FxMx6kA%3D%3D; IJUSERNL=Victor%C2%ACCA%C2%AC38908077-2d61-4fa8-88fb-2409cc4da3ce%C2%ACseg%3D23%C2%ACprv%3D26; nfsld9d6558b2036b0758d9bfefe08f0c45d=1; AWSALB=cTn/94mY8YQLaYA8bud42jY74Gy67dQf1rdZ3AP0i5XiUJhv/xEXUOUhQe2pprqOhVQgF4IaQ9jeg1l8CzGGzTaURNAj1jawjizuyguxXqDmzNXXxHoogNyDz+Go; ajs_user_id=%22sdrn%3Ainfojobs.net%3Auser%3A32128330420%22
    referer: https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL
    sec-fetch-mode: navigate
    sec-fetch-site: same-site
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36

__Query String Parameters__
    scope: CANDIDATE_PROFILE_WITH_EMAIL
    client_id: devsite-test-console-net
    redirect_uri: https://developer.infojobs.net/test-console/continue-request.xhtml
    response_type: code
    state: CANDIDATE_PROFILE_WITH_EMAIL
    dgv: 19161524573339042201

Y salto final donde se queda pillado un "pensando" ya que falla un javascript en la pagina final.
### https://developer.infojobs.net/test-console/continue-request.xhtml?code=06e88b03-949a-40e1-83ba-92586a5b5583&state=CANDIDATE_PROFILE_WITH_EMAIL&scopes=CANDIDATE_PROFILE_WITH_EMAIL&auth_type=api&dgv=14839528301444153507

__General__
    Request URL: https://developer.infojobs.net/test-console/continue-request.xhtml?code=06e88b03-949a-40e1-83ba-92586a5b5583&state=CANDIDATE_PROFILE_WITH_EMAIL&scopes=CANDIDATE_PROFILE_WITH_EMAIL&auth_type=api&dgv=14839528301444153507
    Request Method: GET
    Status Code: 200 OK
    Remote Address: 52.215.117.97:443
    Referrer Policy: no-referrer-when-downgrade

__Response headers__
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Language: es,en-en
    Content-Length: 2080
    Content-Type: text/html;charset=windows-1252
    Date: Mon, 18 Nov 2019 19:43:09 GMT
    Pragma: no-cache
    Server: Apache
    Strict-Transport-Security: max-age=63072000; includeSubdomains;
    Vary: Accept-Encoding,User-Agent
    X-Powered-By: JSP/2.2

__Request headers__
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    Accept-Encoding: gzip, deflate, br
    Accept-Language: es-ES,es;q=0.9,en;q=0.8
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: JSESSIONID=SjpkCbjO1JfP0J+ao+5RYNqg; AWSELB=6F772D7F025CE724146F13F5B98B9A20F07F7A8E0C9D7256D1219719E9B539A617EA68DBED01CE8948C896AF7D4494949DBAB3487512C772A0F98AC9834E315B69561AC2CD; xtvrn=$500892$; JSESSIONID=cPvCnJilSWiVCyckyLHWPvRh; IJTESTUID=64331fa7-d2da-44c0-963e-824690f88518; IJUSERUID=05708230-19af-4e2d-bd06-072eb2a26dbd; ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c; test-cookie=to%20be%20or%20not%20to%20be; ajs_group_id=null; utag_main=v_id:016e800960f6001b4dc828cb4e5d0307800cc07000bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574107928630$ses_id:1574106128630%3Bexp-session$vapi_domain:infojobs.net; AMCVS_05FF6243578784B37F000101%40AdobeOrg=1; s_cc=true; _pulse2data=211a477e-747c-4e1a-a601-04397280acf3%2Cv%2C%2C1574107029556%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMThUMTk6NDI6MDlaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..7tQ_Nncoxx5_qewI5KH73g.oB5v4-XdTeuIv4vtr60ps5Sp2qj83jEMsZR8kAsORn5uV_pwkfZsMO-RP9O7B2qrdFzY2KX_6iFJGbHirAMwWCBsq5AwSYUJ0gWS762FEiGMGDh1AuHVJLmjCiIPhHYBLf9xtNIswYH7clyaUJ0KAyPdt4HSygqjjWpKVN8LuFaM-2kqkaH9uFVcvTmODw7XdxAvyZuUdDdpS-JtJfMJig.-cNiBQXIva_E7XVxILv9jw%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..xSr_EzSygIhSK0DGpwv5V35MMc25W8p-IHLf-opY1B4; AMCV_05FF6243578784B37F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18219%7CMCMID%7C32684227982076427600498174367758074122%7CMCAAMLH-1574710928%7C6%7CMCAAMB-1574710928%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1574113329s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18226%7CvVersion%7C4.3.0; s_sq=schibstedspainjobsinfojobsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dother%2526link%253DIniciar%252520sesi%2525C3%2525B3n%2526region%253Dapi-login-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dother%2526pidt%253D1%2526oid%253DIniciar%252520sesi%2525C3%2525B3n%2526oidt%253D3%2526ot%253DSUBMIT; IJCUG=DIfK%252FqxW0VWdb3uNG73EBL6h1b6mdq51UDuSTP33nkfUfy%252Fnda0Z0XssGGNC6cNRYDot6Lm84nHK%250ADnrb5aKIxMFJnYEGCc1%252F3J0%253D; IJH=DH%2BrWyywNMWqN63qGyJw0%2BNyoE%2FTydy24zSSklYzbNOhbVRJ1%2BuUA0zQ3A1CScSBX2bt17lvHWFsIbS%2FxMx6kA%3D%3D; IJUSERNL=Victor%C2%ACCA%C2%AC38908077-2d61-4fa8-88fb-2409cc4da3ce%C2%ACseg%3D23%C2%ACprv%3D26; nfsld9d6558b2036b0758d9bfefe08f0c45d=1; ajs_user_id=%22sdrn%3Ainfojobs.net%3Auser%3A32128330420%22; IJE=DEf%2BsqOP62B4YbZoxeJW1ejcYMBdn3v%2B%2FsQR1kSH3hl5Bf4hc2jp5yKJt4cocXbMkopWq68gFp0tHE6Z
    Host: developer.infojobs.net
    Referer: https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: same-site
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36

__Query String Params__
    code: 06e88b03-949a-40e1-83ba-92586a5b5583
    state: CANDIDATE_PROFILE_WITH_EMAIL
    scopes: CANDIDATE_PROFILE_WITH_EMAIL
    auth_type: api
    dgv: 14839528301444153507

Y el fallo final en la linea 72:
window.parent.executeAfterAuth();
Aunque no pasa nada porque podemos cerrar la ventana, volver a la consola de test, refrescar y funciona todo con las siguientes cookies

### https://developer.infojobs.net/test-console/execute.xhtml
__General__
    Request URL: https://developer.infojobs.net/test-console/execute.xhtml
    Request Method: POST
    Status Code: 200 OK
    Remote Address: 52.51.85.119:443
    Referrer Policy: no-referrer-when-downgrade

__Response headers__
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Language: es,en-en
    Content-Length: 9559
    Content-Type: text/html;charset=windows-1252
    Date: Mon, 18 Nov 2019 20:09:13 GMT
    Pragma: no-cache
    Server: Apache
    Strict-Transport-Security: max-age=63072000; includeSubdomains;
    Vary: Accept-Encoding,User-Agent
    X-Powered-By: JSP/2.2

__Request headers__
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    Accept-Encoding: gzip, deflate, br
    Accept-Language: es-ES,es;q=0.9,en;q=0.8
    Cache-Control: max-age=0
    Connection: keep-alive
    Content-Length: 219
    Content-Type: application/x-www-form-urlencoded
    Cookie:
        JSESSIONID=SjpkCbjO1JfP0J+ao+5RYNqg;
        AWSELB=6F772D7F025CE724146F13F5B98B9A20F07F7A8E0C9D7256D1219719E9B539A617EA68DBED01CE8948C896AF7D4494949DBAB3487512C772A0F98AC9834E315B69561AC2CD;
        xtvrn=$500892$;
        JSESSIONID=cPvCnJilSWiVCyckyLHWPvRh;
        IJTESTUID=64331fa7-d2da-44c0-963e-824690f88518;
        IJUSERUID=05708230-19af-4e2d-bd06-072eb2a26dbd;
        ajs_anonymous_id=4ad93af4-385f-46cf-8888-813a5fe5239c;
        ajs_group_id=null;
        utag_main=v_id:016e800960f6001b4dc828cb4e5d0307800cc07000bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574107928630$ses_id:1574106128630%3Bexp-session$vapi_domain:infojobs.net;
        AMCVS_05FF6243578784B37F000101%40AdobeOrg=1;
        s_cc=true;
        _pulse2data=211a477e-747c-4e1a-a601-04397280acf3%2Cv%2C%2C1574107029556%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMThUMTk6NDI6MDlaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..7tQ_Nncoxx5_qewI5KH73g.oB5v4-XdTeuIv4vtr60ps5Sp2qj83jEMsZR8kAsORn5uV_pwkfZsMO-RP9O7B2qrdFzY2KX_6iFJGbHirAMwWCBsq5AwSYUJ0gWS762FEiGMGDh1AuHVJLmjCiIPhHYBLf9xtNIswYH7clyaUJ0KAyPdt4HSygqjjWpKVN8LuFaM-2kqkaH9uFVcvTmODw7XdxAvyZuUdDdpS-JtJfMJig.-cNiBQXIva_E7XVxILv9jw%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..xSr_EzSygIhSK0DGpwv5V35MMc25W8p-IHLf-opY1B4;
        AMCV_05FF6243578784B37F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18219%7CMCMID%7C32684227982076427600498174367758074122%7CMCAAMLH-1574710928%7C6%7CMCAAMB-1574710928%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1574113329s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18226%7CvVersion%7C4.3.0;
        s_sq=schibstedspainjobsinfojobsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dother%2526link%253DIniciar%252520sesi%2525C3%2525B3n%2526region%253Dapi-login-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dother%2526pidt%253D1%2526oid%253DIniciar%252520sesi%2525C3%2525B3n%2526oidt%253D3%2526ot%253DSUBMIT;
        IJCUG=DIfK%252FqxW0VWdb3uNG73EBL6h1b6mdq51UDuSTP33nkfUfy%252Fnda0Z0XssGGNC6cNRYDot6Lm84nHK%250ADnrb5aKIxMFJnYEGCc1%252F3J0%253D; IJH=DH%2BrWyywNMWqN63qGyJw0%2BNyoE%2FTydy24zSSklYzbNOhbVRJ1%2BuUA0zQ3A1CScSBX2bt17lvHWFsIbS%2FxMx6kA%3D%3D; IJUSERNL=Victor%C2%ACCA%C2%AC38908077-2d61-4fa8-88fb-2409cc4da3ce%C2%ACseg%3D23%C2%ACprv%3D26;
        nfsld9d6558b2036b0758d9bfefe08f0c45d=1;
        ajs_user_id=%22sdrn%3Ainfojobs.net%3Auser%3A32128330420%22;
        IJE=DEf%2BsqOP62B4YbZoxeJW1ejcYMBdn3v%2B%2FsQR1kSH3hl5Bf4hc2jp5yKJt4cocXbMkopWq68gFp0tHE6Z
    Host: developer.infojobs.net
    Origin: https://developer.infojobs.net
    Referer: https://developer.infojobs.net/test-console/console.xhtml?dgv=5898536144957949562
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: same-origin
    Sec-Fetch-User: ?1
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36

__Form data__
    urifield: https://api.infojobs.net/api/2/candidate
    versionfield: 2
    methodfield: GET
    hmethodfield: GET
    operationEntityField: -candidate
    attachment_type: Local
    paramsAttached: 1
    headersAttached: 1
    bodyContentType: json

La respuesta es producida por el lado del servidor con la API y nos lo devuelve en el HTML dentro de <pre id="formattedBody">

__My key de usuario es 38908077-2d61-4fa8-88fb-2409cc4da3ce dentro de la API__
















