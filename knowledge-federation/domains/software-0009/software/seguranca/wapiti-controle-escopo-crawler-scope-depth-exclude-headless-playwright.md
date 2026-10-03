---
id: software.seguranca.tranche09.000863
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

# Wapiti: Controle de **Escopo (`--scope`)**, Profundidade (`-d`), Exclusão de Rotas Destrutivas (**`-x` Logout**) e Crawler **Headless (`--headless`)**

## Em uma frase
Ao apontar um scanner DAST automático para uma aplicação web autenticada, dois perigos operacionais precisam ser controlados antes de apertar Enter: **(1)** o crawler seguir um link para fora do alvo ou entrar em um loop infinito de calendário/paginação, e **(2)** o crawler clicar no botão **`/logout`**, **`/delete-account`** ou **`/reset-db`**, matando a própria sessão ou apagando dados do ambiente!

## Por que importa
O Wapiti controla a fronteira de navegação com **`--scope`** (`url` = testa apenas a URL exata informada; `page` = apenas aquela página e seus parâmetros; `folder` = tudo abaixo daquele subdiretório; `domain` = todo o subdomínio; `punk` = sem restrição) combinado com **`-d` / `--depth`** (profundidade máxima de links) e **`--max-links-per-page`** / **`--max-files-per-dir`**.

## Como funciona
Para proteger a sessão e o banco de dados, passe sempre **`-x` / `--exclude`** nas rotas de logout/exclusão e **`-s` / `--start`** para fornecer URLs sementes adicionais; e quando a aplicação for uma **SPA (React/Vue/Angular)** que renderiza links via JavaScript no DOM, ative o navegador **Playwright** integrado com **`--headless visible`** ou **`--headless hidden`**!

## Exemplo
```bash
# Executar o Wapiti restrito ao escopo da pasta (--scope folder), com crawler Headless (--headless hidden) e excluindo /logout
wapiti -u https://app.internal.corp/portal/ \
  --scope folder \
  --depth 5 \
  --headless hidden \
  --exclude "https://app.internal.corp/portal/logout*" \
  --skip "csrf_token" \
  -m "sql,xss,csp,http_headers,cookieflags" \
  -f html -o /cases/pentest/wapiti_report_html
```

## Limites e trade-offs
Observe a flag **`--skip <parametro>`**: usá-la em parâmetros de estado (como `--skip "csrf_token"` ou `--skip "session_id"`) impede que os módulos de ataque corrompam o token anti-CSRF exigido pelo formulário!

## Como verificar
Se for a primeira vez usando `--headless`, execute **`wapiti-install-headless-browser`** para baixar o motor de navegador gerenciado pelo Playwright.

## Conexões
- [[wapiti-modulos-injecao-sql-timesql-xss-permanentxss-xxe-exec-file]] — Veja também: Wapiti (`-m` / `--module`): Módulos de Injeção Ativa (`sql`, `timesql`, `ldap`, `xss`, `permanentxss`, `exec`, `file`, `xxe`, `crlf` e `ssrf`).
- [[wapiti-varredura-autenticada-getcookie-form-script-cookies-ntlm]] — Veja também: Wapiti: Varredura Autenticada com **`wapiti-getcookie`**, Extração do Navegador (`--cookie`), **`--form-script`** e Autenticação HTTP (`Basic`/`Digest`/`NTLM`).
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
