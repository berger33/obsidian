---
id: software.seguranca.tranche09.000864
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

# Wapiti: Varredura Autenticada com **`wapiti-getcookie`**, Extração do Navegador (`--cookie`), **`--form-script`** e Autenticação HTTP (`Basic`/`Digest`/`NTLM`)

## Em uma frase
Se o scanner DAST não estiver autenticado, ele testará apenas a tela de login pública e deixará 95% das funcionalidades internas da aplicação sem auditoria.

## Por que importa
Conforme detalhado no `README.rst` e `pyproject.toml`, o Wapiti oferece quatro mecanismos de autenticação: **(1)** importar cookies diretamente do seu navegador Chrome/Firefox local ou capturar uma sessão interativa com o utilitário **`wapiti-getcookie -u <url_login> -c cookies.json`** (passando depois **`-c cookies.json`** ao `wapiti`); **(2)** preencher formulários de login automaticamente (`--auth-user`, `--auth-password`, `--auth-method post`); **(3)** autenticação de protocolo HTTP **`Basic`, `Digest` e `NTLM`** (via biblioteca `httpx-ntlm`); e **(4)** carregar um script Python customizado via **`--form-script`** para fluxos complexos de SSO/MFA/Tokens dinâmicos!

## Como funciona
Além disso, a flag **`-H` / `--header "Authorization: Bearer <TOKEN>"`** injeta tokens JWT ou chaves de API diretamente em todas as requisições.

## Exemplo
```bash
# Capturar cookies de sessao autenticada com wapiti-getcookie e executar o Wapiti mantendo a sessao ativa (excluindo /logout)
wapiti-getcookie -u https://app.internal.corp/login -c /cases/pentest/wapiti_session.json

wapiti -u https://app.internal.corp/dashboard \
  -c /cases/pentest/wapiti_session.json \
  --exclude "https://app.internal.corp/logout*" \
  --scope domain \
  -m "sql,xss,file,exec,ssrf" \
  -f json -o /cases/pentest/wapiti_auth_scan.json
```

## Limites e trade-offs
Sempre que usar `-c wapiti_session.json`, lembre-se de passar **`--exclude "*logout*" --exclude "*signout*"`** para que o crawler do Wapiti não encerre a sessão que o `wapiti-getcookie` acabou de abrir!

## Como verificar
Inspecione o arquivo `/cases/pentest/wapiti_session.json` para verificar os cookies e seus atributos `Secure`/`HttpOnly` capturados.

## Conexões
- [[wapiti-controle-escopo-crawler-scope-depth-exclude-headless-playwright]] — Veja também: Wapiti: Controle de **Escopo (`--scope`)**, Profundidade (`-d`), Exclusão de Rotas Destrutivas (**`-x` Logout**) e Crawler **Headless (`--headless`)**.
- [[wapiti-varredura-apis-rest-openapi-swagger-json-payloads]] — Veja também: Wapiti para **APIs REST (`--swagger`)**: Auditoria Direta de Contratos **OpenAPI / Swagger** e Injeção de Payloads dentro de **Corpos JSON**.
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
