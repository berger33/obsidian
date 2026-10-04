---
id: software.seguranca.tranche09.000869
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
fontes: ["https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst", "https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml", "https://wapiti-scanner.github.io/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Wapiti: Ajuste de Concorrência Assíncrona (**`--tasks`**), Timeouts (`-t`, `--max-scan-time`, `--max-attack-time`) e Sessões SQLite (`--store-session`)

## Em uma frase
Construído sobre o cliente HTTP assíncrono `httpx` e `asyncio`, o Wapiti controla quantas requisições HTTP simultâneas são disparadas através da flag **`--tasks <N>`** (padrão `32` tasks concorrentes).

## Por que importa
Em servidores de homologação pequenos ou aplicações legadas que abrem uma conexão de banco de dados não-poolada por requisição, 32 tasks concorrentes podem causar *timeouts* falsos (`HTTP 500` / `504 Gateway Timeout`, que o Wapiti reporta na categoria **Anomalies**); nesses ambientes, reduza para **`--tasks 8`** e ajuste **`-t` / `--timeout 15.0`**!

## Como funciona
Para controlar rigorosamente a janela de execução em pipelines de CI/CD, o Wapiti fornece **`--max-scan-time <segundos>`** (tempo máximo total da execução) e **`--max-attack-time <segundos>`** (tempo máximo permitido por módulo de ataque), além de **`--store-session <diretorio>`** e **`--flush-session`** (para limpar o cache SQLite e forçar uma varredura 100% nova).

## Exemplo
```bash
# Executar o Wapiti limpando sessoes anteriores (--flush-session), com 10 tasks concorrentes e teto de 15 minutos
wapiti -u https://app.internal.corp/ \
  --flush-session \
  --tasks 10 \
  --timeout 12 \
  --max-scan-time 900 \
  --max-attack-time 180 \
  -m "common" \
  -f json -o /cases/pentest/wapiti_timed_scan.json
```

## Limites e trade-offs
Atenção ao comportamento de cache do Wapiti: se você rodar o mesmo comando `wapiti -u https://alvo/` duas vezes seguidas **sem** passar `--flush-session`, na segunda vez o Wapiti lerá o banco SQLite existente em `~/.wapiti/scans/` e pulará os ataques que já foram concluídos! Passe sempre **`--flush-session`** após corrigir uma vulnerabilidade para validar que a correção realmente funcionou!

## Como verificar
Verifique na seção `anomalies` do relatório JSON se ocorreram erros `500 Internal Server Error` ou timeouts de recurso durante os testes.

## Conexões
- [[wapiti-deteccao-out-of-band-ssrf-xxe-log4shell-endpoint-customizado]] — Veja também: Wapiti **Out-of-Band (OAST / `--external-endpoint`)**: Detecção de **Blind SSRF**, **Blind XXE** e **Log4Shell** com Endpoint Externo Próprio.
- [[wapiti-relatorios-html-json-xml-md-integracao-proxy-mitmproxy]] — Veja também: Wapiti: Geração de Relatórios (**`-f html,json,xml,md,csv,txt`**), Encaminhamento via Proxy (**`-p` `mitmproxy` / ZAP**) e Pipelines DevSecOps.
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.
- [[feroxbuster-gerenciamento-estado-state-file-resume-from-time-limit]] — Referência cruzada direta com feroxbuster-gerenciamento-estado-state-file-resume-from-time-limit.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
