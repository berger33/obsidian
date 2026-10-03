---
id: software.seguranca.tranche09.000862
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

# Wapiti (`-m` / `--module`): Módulos de Injeção Ativa (`sql`, `timesql`, `ldap`, `xss`, `permanentxss`, `exec`, `file`, `xxe`, `crlf` e `ssrf`)

## Em uma frase
Conforme documentado na seção `Module names` do `README.rst` oficial, o Wapiti organiza seus ataques em **34 módulos independentes** que podem ser selecionados individualmente ou por grupos na flag **`-m` / `--module`** (ex.: `-m "sql,xss,exec,file,ssrf"` ou o preset `-m common`).

## Por que importa
Um diferencial importante do Wapiti no teste de **Cross-Site Scripting (XSS)** é a separação entre os módulos **`xss` (Reflected XSS)** e **`permanentxss` (Stored / Persistent XSS)**: após injetar identificadores únicos em todos os formulários da aplicação durante o módulo `xss`, o módulo `permanentxss` **re-varre toda a aplicação do zero** procurando se algum payload gravado no banco de dados reapareceu sem sanitização em outra página (como no painel de administração ou lista de comentários)!

## Como funciona
Da mesma forma, o Wapiti separa **`sql`** (SQL/XPath Injection rápida baseada em erros e lógica booleana) de **`timesql`** (Blind SQL Injection baseada em atraso de tempo `SLEEP`/`WAITFOR`, que é mais lenta e deve ser rodada seletivamente).

## Exemplo
```bash
# Executar o Wapiti ativando especificamente os modulos de Injeção (SQLi, XSS refletido/armazenado, RCE, LFI e XXE)
wapiti -u https://app.internal.corp/ \
  -m "sql,xss,permanentxss,exec,file,xxe,crlf" \
  --max-scan-time 1800 \
  -f json -o /cases/pentest/wapiti_injections.json
```

## Limites e trade-offs
Na sintaxe do `-m` do Wapiti, você também pode usar o prefixo **`-`** para **desativar** um módulo específico de um preset: por exemplo, **`-m "all,-blindsql,-timesql,-brute_login_form"`** executa todos os módulos exceto os mais lentos/intrusivos!

## Como verificar
Verifique no relatório JSON gerado a requisição HTTP completa (`http_request`) e o comando `curl_command` reproduzível para cada vulnerabilidade confirmada.

## Conexões
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Veja também: **Wapiti 3 (`wapiti-scanner/wapiti`)**: Arquitetura do Scanner **DAST Black-Box** Assíncrono em Python (`httpx`, `aiosqlite`, `Playwright` e `mitmproxy`).
- [[wapiti-controle-escopo-crawler-scope-depth-exclude-headless-playwright]] — Veja também: Wapiti: Controle de **Escopo (`--scope`)**, Profundidade (`-d`), Exclusão de Rotas Destrutivas (**`-x` Logout**) e Crawler **Headless (`--headless`)**.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
