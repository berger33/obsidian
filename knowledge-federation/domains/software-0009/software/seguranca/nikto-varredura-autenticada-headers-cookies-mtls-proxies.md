---
id: software.seguranca.tranche09.000856
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/sullo/nikto/master/README.md", "https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default", "https://github.com/sullo/nikto/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nikto: Varredura Autenticada (**`-id` Basic/NTLM**, **`-Add-header`**, `STATIC-COOKIE`), Certificados de Cliente **mTLS (`-RSAcert`, `-key`)** e **`-useproxy`**

## Em uma frase
Para auditar aplicações corporativas que exigem autenticação por cabeçalho (`Authorization: Bearer <JWT>`), cookies de sessão, Basic/Digest/NTLM Auth ou **Certificados de Cliente mTLS**, o Nikto oferece suporte nativo na linha de comando e no `nikto.conf`.

## Por que importa
Nas versões modernas do Nikto, a flag **`-Add-header "Nome: Valor"`** (que pode ser repetida múltiplas vezes!) injeta cabeçalhos arbitrários como tokens Bearer ou chaves de API; a flag **`-id usuario:senha`** (ou `usuario:senha:dominio` para NTLM) configura autenticação HTTP; e a opção **`-Option "STATIC-COOKIE=session=xyz;"`** envia cookies fixos em todas as requisições.

## Como funciona
Para endpoints protegidos por **mTLS**, basta passar o certificado e a chave privada em PEM via **`-RSAcert /caminho/client.crt -key /caminho/client.key`**!

## Exemplo
```bash
# Executar o Nikto autenticado com Token JWT (-Add-header), Certificado mTLS (-RSAcert/-key) e passando pelo proxy local
nikto -h https://mtls-api.internal.corp \
  -Add-header "Authorization: Bearer eyJhbGciOiJFUzI1NiIs..." \
  -Add-header "X-Audit-Ticket: SEC-2026" \
  -RSAcert /cases/pentest/client.crt \
  -key /cases/pentest/client.key \
  -useproxy http://127.0.0.1:8080 \
  -Cgidirs none -Tuning 23b -ask no -nointeractive -nocheck
```

## Limites e trade-offs
Quando a aplicação não deve manter cookies novos enviados pelo servidor durante os testes (para evitar que um teste altere o estado da sessão), adicione a flag **`-nocookies`**.

## Como verificar
Inspecione no `mitmproxy` (`127.0.0.1:8080`) que os cabeçalhos adicionados com `-Add-header` estão presentes nas requisições do Nikto.

## Conexões
- [[nikto-selecao-plugins-macros-headers-outdated-robots-put-del]] — Veja também: Nikto **`-Plugins`**: Execução Direta de Plugins Específicos (`headers`, `outdated`, `robots`, `put_del_test`, `ssl`, `apache_expect_xss` e `siebel`).
- [[nikto-tratamento-soft-404-no404-db-404-strings-falso-positivo]] — Veja também: Nikto: Calibração contra Páginas **"Soft 404"** (`db_404_strings`, `-no404`) e Prefixo de Diretório **`-root`**.
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Referência cruzada direta com nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins.
- [[gobuster-autenticacao-mtls-certificados-p12-pem-cookies-headers-proxies]] — Referência cruzada direta com gobuster-autenticacao-mtls-certificados-p12-pem-cookies-headers-proxies.
- [[mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile]] — Referência cruzada direta com mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
