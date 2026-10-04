---
id: software.seguranca.tranche04.000346
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
fontes: ["https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md", "https://docs.projectdiscovery.io/opensource/subfinder/overview", "https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Subfinder: Controle de Escopo com Match (`-m`), Filter (`-f`) e Exclusão de IPs (`-ei`)

## Em uma frase
As opções `-m` (`-match`), `-f` (`-filter`) e `-ei` (`-exclude-ip`) do `subfinder` restringem os subdomínios emitidos na saída de acordo com regras de escopo contratual de testes de intrusão ou programas de Bug Bounty.

## Por que importa
Evita que subdomínios explicitamente fora de escopo (ex.: `*.prod-pci.example.corp` ou ambientes de parceiros terceirizados) sejam repassados automaticamente para ferramentas ativas de *probing* e *crawling* no restante do pipeline.

## Como funciona
As flags `-m` e `-f` aceitam strings separadas por vírgula ou o caminho de um arquivo contendo padrões de subdomínios a incluir ou excluir. Já a flag `-ei` (`-exclude-ip`) remove endereços IP literais que algumas fontes passivas retornam misturados a nomes de domínio.

## Exemplo
```bash
# Incluir apenas subdomínios de homologação/API e excluir escopos proibidos pelo ROE (Rules of Engagement)
subfinder -d example.corp \
  -f out-of-scope-hosts.txt \
  -ei -silent \
  -o in-scope-subdomains.txt
```

## Limites e trade-offs
Aplicar o filtro de escopo apenas no `subfinder` não substitui a configuração de escopo nas ferramentas seguintes (`httpx`, `katana`, `nuclei`), pois redirecionamentos HTTP 302 podem levar o scanner ativo de volta para um host fora de escopo.

## Como verificar
Confirme com `grep -Ff out-of-scope-hosts.txt in-scope-subdomains.txt` que nenhum ativo listado no arquivo de exclusão está presente no artefato final.

## Conexões
- [[subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao]] — Veja também: Subfinder: Rate-Limiting Global (`-rl`) e por Provedor (`-rls`), Timeouts e Limite de Leitura (`-rsr`).
- [[subfinder-formatos-saida-jsonl-collect-sources-output-dir-audit]] — Veja também: Subfinder: Saída Estruturada JSONL (`-oJ`), Atribuição de Fontes (`-cs`) e Diretórios por Domínio (`-oD`).
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.
- [[subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei]] — Referência cruzada direta com subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei.
- [[katana-controle-escopo-field-scope-crawl-scope-out-of-scope]] — Referência cruzada direta com katana-controle-escopo-field-scope-crawl-scope-out-of-scope.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
