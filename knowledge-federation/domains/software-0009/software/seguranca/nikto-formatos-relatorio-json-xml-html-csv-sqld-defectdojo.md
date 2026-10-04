---
id: software.seguranca.tranche09.000859
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

# Nikto: Exportação Multi-Formato (**`-Format json,xml,htm,csv,sqld`**), Ingestão Direta em Banco SQL (**`sqld`**) e **OWASP DefectDojo**

## Em uma frase
Conforme documentado no `README.md` oficial e no `nikto.conf.default`, a flag **`-Format`** do Nikto aceita **múltiplos formatos separados por vírgula na mesma execução** (ex.: `-Format json,htm,xml,csv`), gerando todos os relatórios ao final de um único scan!

## Por que importa
Além dos arquivos em disco (`json`, `xml`, `htm`, `csv`, `txt`, `sql`), o Nikto possui o formato **`sqld` (*SQL Direct*)**, que insere os resultados diretamente em um banco de dados **MySQL ou PostgreSQL** central configurado em `nikto.conf` (`DB_TYPE`, `DB_HOST`, `DB_NAME`) usando as variáveis de ambiente `NIKTO_DB_USER` e `NIKTO_DB_PASS`!

## Como funciona
Para plataformas de gestão de vulnerabilidades como o **OWASP DefectDojo**, os formatos **`xml`** e **`json`** do Nikto são suportados nativamente pelo importador `"Nikto Scan"` (mapeando os identificadores `OSVDB` / `Nikto ID`, URI, método HTTP e descrição).

## Exemplo
```bash
# Executar o Nikto exportando o relatorio em XML/JSON para ingestao automatizada no OWASP DefectDojo
nikto -h https://app.internal.corp \
  -Plugins "headers;outdated;robots;httpoptions" \
  -ask no -nointeractive -nocheck \
  -o /cases/pentest/nikto_defectdojo.xml -Format xml
```

## Limites e trade-offs
Se existirem IDs específicos do `db_tests` que a política da sua empresa já aceitou como falso positivo / informativo global, você pode listá-los na diretiva **`SKIPIDS=`** dentro do `nikto.conf` (ou via `-Option "SKIPIDS=000123 000456"`) para que nunca mais poluam os relatórios.

## Como verificar
Valide o arquivo XML ou JSON gerado antes de enviá-lo para a API `/api/v2/import-scan/` do DefectDojo.

## Conexões
- [[nikto-varredura-multi-host-multi-porta-nmap-gnmap-maxtime-pause]] — Veja também: Nikto em Lote: Ingestão Direta de Saída **Nmap (`-h scan.gnmap`)**, Múltiplas Portas (`-port 80,443,8080`) e Limites **`-maxtime` / `-Pause`**.
- [[nikto-deteccao-defensiva-assinaturas-waf-user-agent-rate-limiting]] — Veja também: Engenharia de Detecção (Blue Team): Identificação de Varreduras **Nikto** no **Coraza WAF / OWASP CRS**, **Suricata** e **Fail2ban**.
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Referência cruzada direta com nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins.
- [[nikto-selecao-plugins-macros-headers-outdated-robots-put-del]] — Referência cruzada direta com nikto-selecao-plugins-macros-headers-outdated-robots-put-del.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
