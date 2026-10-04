---
id: software.seguranca.tranche04.000363
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

# Katana: Controle Estrito de Escopo (`-fs`, `-cs`, `-cos`, `-do` e `-e`) para Prevenção de Fuga de Crawl

## Em uma frase
O `katana` previne que o spider siga links para fora do alvo autorizado utilizando escopo por campo DNS (`-fs`), expressões regulares de inclusão (`-cs` / `-crawl-scope`), regex de exclusão (`-cos` / `-crawl-out-scope`), bloqueio de saída (`-do`) e exclusão de hosts/IPs (`-e`).

## Por que importa
Sem controle de escopo, um único link para redes sociais, parceiros comerciais ou botões de *"Logout"* (`-cos "logout|signout"`) faz o crawler abandonar a sessão autenticada ou varrer domínios de terceiros não autorizados.

## Como funciona
A flag `-fs` (`-field-scope`) aceita `rdn` (padrão: mesmo domínio raiz registrável, ex.: `*.example.corp`), `fqdn` (estritamente o mesmo subdomínio inicial, ex.: apenas `app.example.corp`) ou `dn` (palavra-chave do domínio). Complementarmente, `-cos` recebe regexes de caminhos proibidos (como `/logout`, `/delete`, `/reset`) que jamais devem ser visitados pelo crawler.

## Exemplo
```bash
# Restringir o crawl estritamente ao mesmo FQDN e bloquear rotas de logout ou exclusão
katana -u https://app.staging.corp/dashboard \
  -fs fqdn \
  -cos "logout|signout|account/delete" \
  -e cdn,private-ips \
  -d 4 -o scoped-crawl.txt
```

## Limites e trade-offs
Usar o padrão `-fs rdn` ao testar um único subdomínio de homologação (`staging.example.corp`) permite que o crawler siga links que apontam para `www.example.corp` (produção); use sempre `-fs fqdn` quando apenas um subdomínio específico estiver autorizado.

## Como verificar
Execute `cut -d/ -f3 scoped-crawl.txt | sort -u` e confirme que 100% das URLs visitadas pertencem exclusivamente ao FQDN `app.staging.corp`.

## Conexões
- [[katana-analise-javascript-jc-jsluice-known-files-endpoints]] — Veja também: Katana: Parsing Estático de Arquivos JavaScript (`-jc` e `-jsl`) e Descoberta de `known-files` (`-kf`).
- [[katana-preenchimento-formularios-aff-form-config-estrategias-visita]] — Veja também: Katana: Preenchimento Automático de Formulários (`-aff`, `-fc`), Extração (`-fx`) e Estratégias de Visita (`-s`).
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.
- [[katana-crawling-autenticado-headers-cookies-chrome-ws-url]] — Referência cruzada direta com katana-crawling-autenticado-headers-cookies-chrome-ws-url.
- [[subfinder-filtragem-escopo-match-filter-exclude-ip]] — Referência cruzada direta com subfinder-filtragem-escopo-match-filter-exclude-ip.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
