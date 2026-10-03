---
id: software.seguranca.tranche09.000860
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

# Engenharia de Detecção (Blue Team): Identificação de Varreduras **Nikto** no **Coraza WAF / OWASP CRS**, **Suricata** e **Fail2ban**

## Em uma frase
Do ponto de vista de **Operações de Segurança (SOC / Blue Team)**, o Nikto é uma das ferramentas mais ruidosas da internet: uma execução padrão envia mais de 7.000 requisições sequenciais em poucos minutos, inclui por padrão `(Nikto/2.x)` no cabeçalho `User-Agent` (a menos que alterado com `-useragent`) e sonda centenas de caminhos inexistentes que geram uma enxurrada de códigos `404` e `403` nos logs do Nginx/Apache.

## Por que importa
No **OWASP Core Rule Set (CRS v4)** rodando sobre o **Coraza WAF**, a regra **`913100`** (*Found User-Agent associated with security scanner*) detecta imediatamente o User-Agent padrão do Nikto.

## Como funciona
E mesmo que o atacante customize o User-Agent (`-useragent "Mozilla/5.0..."`) e use `-evasion`, a combinação de: **(1)** acesso a arquivos canário/honeytokens clássicos testados pelo Nikto (`/cgi-bin/`, `/phpmyadmin/`, `/server-status`, `/.env`) e **(2)** uma jail do **Fail2ban** ou cenário do **CrowdSec** monitorando a taxa de erros `404`/`400` por IP bloqueia a origem nos primeiros 5 segundos de varredura!

## Exemplo
```nginx
# Trecho Nginx + Fail2ban: registrar status e User-Agent para bloquear varreduras massivas de 404 (Nikto/Gobuster)
# Em /etc/fail2ban/filter.d/nginx-scanner-404.conf:
# failregex = ^<HOST> - .* "(GET|POST|HEAD) .+ HTTP/.*" (404|403|400) .*$
```

## Limites e trade-offs
Para testar a eficácia do seu SIEM, WAF e Fail2ban em homologação, execute o Nikto primeiro com o User-Agent padrão (validando o bloqueio L7 imediato pela regra `913100` do CRS) e depois com `-useragent` customizado (validando o bloqueio comportamental por taxa de `404` no Fail2ban/CrowdSec!).

## Como verificar
Verifique no `eve.json` do Suricata e no log de auditoria do Coraza WAF os alertas gerados durante a simulação.

## Conexões
- [[nikto-formatos-relatorio-json-xml-html-csv-sqld-defectdojo]] — Veja também: Nikto: Exportação Multi-Formato (**`-Format json,xml,htm,csv,sqld`**), Ingestão Direta em Banco SQL (**`sqld`**) e **OWASP DefectDojo**.
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Referência cruzada direta com nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
