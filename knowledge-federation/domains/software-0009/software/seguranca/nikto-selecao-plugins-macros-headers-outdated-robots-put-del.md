---
id: software.seguranca.tranche09.000855
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

# Nikto **`-Plugins`**: Execução Direta de Plugins Específicos (`headers`, `outdated`, `robots`, `put_del_test`, `ssl`, `apache_expect_xss` e `siebel`)

## Em uma frase
Quando você quer executar apenas verificações pontuais e ultrarrápidas com o Nikto (por exemplo, checar apenas os cabeçalhos HTTP de segurança, o `robots.txt` e se os métodos HTTP `PUT`/`DELETE` estão abertos, realizando menos de 15 requisições no total!), a flag **`-Plugins "<lista>"`** permite selecionar exatamente quais plugins de `program/plugins/` serão executados!

## Por que importa
Por padrão, conforme mostra o `nikto.conf.default`, o Nikto executa a macro **`@@DEFAULT=@@ALL;-@@EXTRAS;tests(report:500)`** (que roda todos os plugins exceto `dictionary` e `siebel`).

## Como funciona
Mas se você passar **`-Plugins "headers;outdated;robots;put_del_test;httpoptions"`**, o Nikto **desativa a varredura de 7.000 arquivos do plugin `tests`** e executa em 2 segundos apenas a auditoria passiva/leve de cabeçalhos, versão do servidor, `robots.txt` e métodos HTTP!

## Exemplo
```bash
# Executar uma auditoria ultraleve (menos de 15 requisicoes!) checando apenas cabecalhos, versao, robots.txt e metodos HTTP
nikto -h https://app.internal.corp \
  -Plugins "headers;outdated;robots;httpoptions;put_del_test" \
  -ask no -nointeractive -nocheck \
  -o /cases/pentest/nikto_light_headers.json
```

## Limites e trade-offs
Esse perfil **`-Plugins "headers;outdated;robots;httpoptions"`** é perfeito para rodar em pipelines rápidos de CI/CD ou contra sistemas críticos em produção onde você não quer enviar milhares de requisições `404`!

## Como verificar
Liste os parâmetros aceitos por cada plugin executando `nikto -list-plugins`.

## Conexões
- [[nikto-tecnicas-evasao-ids-waf-libwhisker-evasion-deteccao]] — Veja também: Nikto **`-evasion`**: As 10 Técnicas de Codificação HTTP **LibWhisker** (`1`–`8`, `A`, `B`) para Teste de Regras de Normalização de **IDS / WAF**.
- [[nikto-varredura-autenticada-headers-cookies-mtls-proxies]] — Veja também: Nikto: Varredura Autenticada (**`-id` Basic/NTLM**, **`-Add-header`**, `STATIC-COOKIE`), Certificados de Cliente **mTLS (`-RSAcert`, `-key`)** e **`-useproxy`**.
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Referência cruzada direta com nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins.
- [[nikto-filtragem-categorias-testes-tuning-reverso-x-escopo]] — Referência cruzada direta com nikto-filtragem-categorias-testes-tuning-reverso-x-escopo.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
