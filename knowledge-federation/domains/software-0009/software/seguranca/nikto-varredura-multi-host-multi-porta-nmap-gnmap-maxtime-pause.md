---
id: software.seguranca.tranche09.000858
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

# Nikto em Lote: Ingestão Direta de Saída **Nmap (`-h scan.gnmap`)**, Múltiplas Portas (`-port 80,443,8080`) e Limites **`-maxtime` / `-Pause`**

## Em uma frase
A flag **`-h` (`-host`)** do Nikto aceita não apenas uma URL ou IP único, mas também um **arquivo texto de hosts/IPs** ou diretamente um **arquivo de saída Grepable do Nmap (`-oG scan.gnmap`)**!

## Por que importa
Quando você passa **`nikto -h /cases/easm/nmap_scan.gnmap`**, o Nikto lê automaticamente o arquivo `.gnmap`, identifica todos os hosts e todas as portas abertas marcadas como `http`, `https`, `ssl/http` ou `http-alt` pelo Nmap e audita cada serviço web na porta e protocolo corretos!

## Como funciona
Para garantir que um único host lento ou tarpit não trave a varredura do lote inteiro pela madrugada, combine sempre **`-maxtime 15m`** (tempo máximo por host, ex.: `15m`, `900s` ou `1h`), **`-timeout 10`** e **`-Pause 0.2`** (atraso em segundos entre cada teste).

## Exemplo
```bash
# Alimentar o Nikto diretamente com um arquivo Grepable do Nmap (.gnmap) limitando o tempo maximo por host a 10 minutos
nikto -h /cases/easm/stage2_nmap_detailed.gnmap \
  -maxtime 10m \
  -timeout 8 \
  -Pause 0.1 \
  -Cgidirs none -Tuning x6 \
  -ask no -nointeractive -nocheck \
  -o /cases/easm/nikto_batch_report.json -Format json
```

## Limites e trade-offs
Adicione **`-Display P`** ou **`-Display V`** se quiser acompanhar o progresso no `stdout`, e **`-Display S`** (*Scrub output*) quando precisar sanitizar endereços IP e hostnames dos logs para compartilhar em relatórios públicos ou treinamentos.

## Como verificar
Verifique no JSON gerado a separação estruturada por host e porta.

## Conexões
- [[nikto-tratamento-soft-404-no404-db-404-strings-falso-positivo]] — Veja também: Nikto: Calibração contra Páginas **"Soft 404"** (`db_404_strings`, `-no404`) e Prefixo de Diretório **`-root`**.
- [[nikto-formatos-relatorio-json-xml-html-csv-sqld-defectdojo]] — Veja também: Nikto: Exportação Multi-Formato (**`-Format json,xml,htm,csv,sqld`**), Ingestão Direta em Banco SQL (**`sqld`**) e **OWASP DefectDojo**.
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Referência cruzada direta com nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins.
- [[naabu-integracao-nativa-nmap-cli-service-fingerprinting-nse]] — Referência cruzada direta com naabu-integracao-nativa-nmap-cli-service-fingerprinting-nse.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
