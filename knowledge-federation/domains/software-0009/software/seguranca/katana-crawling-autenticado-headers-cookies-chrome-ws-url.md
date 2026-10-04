---
id: software.seguranca.tranche04.000368
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md", "https://docs.projectdiscovery.io/opensource/katana/overview", "https://github.com/projectdiscovery/katana/releases"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Katana: Crawling Autenticado com Headers/Cookies (`-H`), Sessão de Navegador (`-cdd`) e Chrome DevTools (`-cwu`)

## Em uma frase
Para mapear a superfície interna de uma aplicação após o login, o `katana` suporta injeção de cabeçalhos `Authorization`/`Cookie` (`-H`), reutilização de diretório de perfil do Chrome (`-cdd` / `-chrome-data-dir` com `-noi`) ou conexão direta a um navegador já autenticado via WebSocket DevTools (`-cwu` / `-chrome-ws-url`).

## Por que importa
Mais de 80% dos endpoints críticos de uma aplicação SaaS ou corporativa ficam atrás da tela de login (SSO/MFA/Passkeys) e retornam `401 Unauthorized` ou `302 Redirect` para crawlers não autenticados.

## Como funciona
Em fluxos com MFA ou OAuth2 complexo, o analista abre uma instância do Chrome com `--remote-debugging-port=9222`, realiza o login manualmente uma única vez e passa a URL WebSocket (`ws://127.0.0.1:9222/devtools/browser/...`) para `katana -hl -cwu <ws-url>` combinada com `-cos "logout|signout"` para preservar a sessão ativa durante todo o spidering.

## Exemplo
```bash
# Crawling autenticado via token Bearer e cookie de sessão preservando a sessão contra logout
katana -u https://api.staging.corp/v1/me \
  -H "Authorization: Bearer ${STAGING_JWT}" \
  -H "Cookie: session_id=${STAGING_SESSION}" \
  -fs fqdn -cos "logout|revoke|signout" \
  -d 3 -jc -jsonl -o authenticated-crawl.jsonl
```

## Limites e trade-offs
Quando usar `-cdd` (diretório de perfil do Chrome) para manter cookies de login no modo Headless, é obrigatório adicionar `-noi` (`-no-incognito`), pois por padrão o modo Headless do `katana` abre abas em modo anônimo que ignoram os cookies persistidos no perfil.

## Como verificar
Confirme em `authenticated-crawl.jsonl` que as rotas autenticadas retornam `status_code: 200` em vez de redirecionamentos para `/login`.

## Conexões
- [[katana-knowledge-base-classificacao-endpoints-segredos-kb]] — Veja também: Katana: Knowledge Base (`-kb`), Classificação de Endpoints REST/GraphQL (`-kb-endpoints`) e Detecção de Segredos (`-kb-secrets`).
- [[katana-rate-limiting-concorrencia-parallelism-delay-timeout-resume]] — Veja também: Katana: Controle de Concorrência (`-c`, `-p`), Rate-Limiting (`-rl`, `-rlm`, `-rd`), TLS Impersonation (`-tlsi`) e `-resume`.
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.
- [[katana-controle-escopo-field-scope-crawl-scope-out-of-scope]] — Referência cruzada direta com katana-controle-escopo-field-scope-crawl-scope-out-of-scope.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
