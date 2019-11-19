# Cookies que se tienen cuando se da permiso a la api de test

Usando burp para sacar las cookies de la peticion final que queremos,
mirar a ver cuales son necesarias


__ORIGINAL__

POST /test-console/execute.xhtml HTTP/1.1
Host: developer.infojobs.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 184
Origin: https://developer.infojobs.net
DNT: 1
Connection: close
Referer: https://developer.infojobs.net/test-console/console.xhtml?dgv=6526915629214341759
Cookie: JSESSIONID=Dkw5P69SQkVmiZ6nofSvwOzZ; xtvrn=$500892$; JSESSIONID=lTLA8VC7QImH-nno2SXzaqer; IJTESTUID=7e90fab4-421a-448c-aef1-a82a22e710ff; ajs_anonymous_id=2facc123-67ce-4f97-9892-5dc6dd02e041; IJUSERUID=8eee80b2-88d5-40f1-9433-fa615b2c3612; AWSELB=6F772D7F025CE724146F13F5B98B9A20F07F7A8E0C9D7256D1219719E9B539A617EA68DBED01CE8948C896AF7D4494949DBAB3487512C772A0F98AC9834E315B69561AC2CD; utag_main=v_id:016e81aa8ede00016189b2bc4b4d0105200cc00f00bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$_st:1574135268894$ses_id:1574133468894%3Bexp-session$vapi_domain:infojobs.net; AMCV_05FF6243578784B37F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18220%7CMCMID%7C90407483161492042306817621505135204529%7CMCAID%7CNONE%7CMCOPTOUT-1574140669s%7CNONE%7CvVersion%7C4.3.0; ajs_user_id=%22sdrn%3Ainfojobs.net%3Auser%3A32128330420%22; ajs_group_id=null; AMCVS_05FF6243578784B37F000101%40AdobeOrg=0; s_cc=true; _pulse2data=561a559d-80a0-44ec-bce9-9fd346012d4d%2Cv%2C%2C1574134370251%2CeyJpc3N1ZWRBdCI6IjIwMTktMTEtMTlUMDM6MTc6NTBaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..WUfn88pCy4-E-a-oAIQP1A.FvA7DwxdRPXT0ahPariUbprc2NSeFkQCe2Xf0NJgeldo0i0VdpStI4vNvHCQm0E4z4B1CTVUAIt6kJwQLY9EiTh9JcfzG0SYQR8mPrK02q1ZzqM75X4ZltJz88bn4gn3LMR2caHH132-pd7I8mLw8vJb4R98hxNga4rNdZwRjkl1kTKzHmAfVA7plbtsjQqk_rpu4vQoAVHq7FHHjY_YDA.W1QiXr-gH22y9QkOlRD6Bg%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..2LcR8h4V8Hx9t_qxl7NXRdIqCOEC7ZrvPI4fG1Sa4nw; s_sq=schibstedspainjobsinfojobsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dother%2526link%253DIniciar%252520sesi%2525C3%2525B3n%2526region%253Dapi-login-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dother%2526pidt%253D1%2526oid%253DIniciar%252520sesi%2525C3%2525B3n%2526oidt%253D3%2526ot%253DSUBMIT; IJCUG=DOWyD%252FZwhwDkLbL%252B1YDViw5QRsKfqQ4yfPXvfVfN8t3It6ocxuVTvt0DCwIKbNic59gfoP2mdx0G%250AyXzf59B%252BwvVCiZ4%252BlB43NbI%253D; IJE=DBN62vQBCdYEq2p45xUjcyTMk1dWr7K%2B1aP3FULGmMN8KY1O9MBNk%2B4WvvP1Dx2EUbK%2BqKfMgzUJI0C8; IJH=DCpzKjU2Gs0RVBxI4AgusyOTyr4HoXAu1TRcqjIDLE7mQegcKvtZ365U%2F9UMPzhLfbwY1fqsOkOI6bIpM33CWA%3D%3D; IJUSERNL=Victor%C2%ACCA%C2%AC38908077-2d61-4fa8-88fb-2409cc4da3ce%C2%ACseg%3D23%C2%ACprv%3D26; nfsld9d6558b2036b0758d9bfefe08f0c45d=
Upgrade-Insecure-Requests: 1

urifield=https%3A%2F%2Fapi.infojobs.net%2Fapi%2F2%2Fcandidate&versionfield=2&methodfield=GET&hmethodfield=GET&operationEntityField=-candidate&attachment_type=Local&bodyContentType=json

__EDITADO__ Quitamos cookies innecesarias y sigue devolviendo la respuesta que queremos
POST /test-console/execute.xhtml HTTP/1.1
Host: developer.infojobs.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 184
Origin: https://developer.infojobs.net
DNT: 1
Connection: close
Referer: https://developer.infojobs.net/test-console/console.xhtml?dgv=6526915629214341759
Cookie: JSESSIONID=Dkw5P69SQkVmiZ6nofSvwOzZ; IJTESTUID=7e90fab4-421a-448c-aef1-a82a22e710ff; AWSELB=6F772D7F025CE724146F13F5B98B9A20F07F7A8E0C9D7256D1219719E9B539A617EA68DBED01CE8948C896AF7D4494949DBAB3487512C772A0F98AC9834E315B69561AC2CD
Upgrade-Insecure-Requests: 1

urifield=https%3A%2F%2Fapi.infojobs.net%2Fapi%2F2%2Fcandidate&versionfield=2&methodfield=GET&hmethodfield=GET&operationEntityField=-candidate&attachment_type=Local&bodyContentType=json

