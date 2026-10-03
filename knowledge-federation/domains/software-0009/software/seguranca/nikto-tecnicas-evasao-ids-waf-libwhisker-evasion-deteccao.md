---
id: software.seguranca.tranche09.000854
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

# Nikto **`-evasion`**: As 10 Técnicas de Codificação HTTP **LibWhisker** (`1`–`8`, `A`, `B`) para Teste de Regras de Normalização de **IDS / WAF**

## Em uma frase
Para ajudar engenheiros de segurança (Blue Team / AppSec) a testar se o seu **WAF (Coraza / ModSecurity)** ou **IDS (Suricata / Snort)** normaliza corretamente requisições HTTP ofuscadas antes de aplicar assinaturas, o Nikto integra as 10 técnicas clássicas de evasão da biblioteca **LibWhisker** através da flag **`-evasion <codigos>`**!

## Por que importa
Conforme listado no `README.md` oficial: **`1`** (Codificação URI aleatória `%xx`), **`2`** (Auto-referência de diretório `/./admin/./config`), **`3`** (Terminação prematura de URL), **`4`** (Prefixar string aleatória longa), **`5`** (Parâmetro falso), **`6`** (Usar caractere `TAB` como separador da requisição HTTP em vez de espaço), **`7`** (Alterar maiúsculas/minúsculas da URL para servidores Windows/IIS), **`8`** (Usar barra invertida `\` do Windows), **`A`** (Usar retorno de carro `0x0d` como separador) e **`B`** (Usar byte `0x0b` como separador)!

## Como funciona
Você pode combinar múltiplas técnicas na mesma execução (ex.: **`-evasion 127`** aplica simultaneamente codificação URI + `/./` + variação de caixa!).

## Exemplo
```bash
# Testar se o WAF/IDS na frente do servidor normaliza corretamente caminhos com /./ (2) e codificacao URI %xx (1)
nikto -h https://waf-test.internal.corp \
  -evasion 12 \
  -Tuning 23 \
  -Cgidirs none \
  -ask no -nointeractive -nocheck
```

## Limites e trade-offs
Em servidores HTTP modernos (Nginx, Envoy, Go `net/http`) que seguem estritamente o **RFC 9110 / RFC 9112**, as técnicas de protocolo sujas **`6` (`TAB`), `A` (`0x0d`) e `B` (`0x0b`)** são rejeitadas imediatamente com `HTTP 400 Bad Request`; portanto, use apenas `1`, `2` e `7` ao testar normalização de caminho em servidores modernos.

## Como verificar
Verifique nos logs do Suricata e do Coraza WAF que as requisições com `-evasion 12` foram decodificadas (`url_decode`, `normalizePath`) e detectadas normalmente.

## Conexões
- [[nikto-modos-mutacao-mutate-diretorios-usuarios-apache-cgiwrap]] — Veja também: Nikto **`-mutate` e `-Cgidirs`**: Descoberta Cruzada de Diretórios/Arquivos (`-mutate 1`), Enumeração Apache `/~user` (`-mutate 3`) e Diretórios CGI.
- [[nikto-selecao-plugins-macros-headers-outdated-robots-put-del]] — Veja também: Nikto **`-Plugins`**: Execução Direta de Plugins Específicos (`headers`, `outdated`, `robots`, `put_del_test`, `ssl`, `apache_expect_xss` e `siebel`).
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Referência cruzada direta com nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
