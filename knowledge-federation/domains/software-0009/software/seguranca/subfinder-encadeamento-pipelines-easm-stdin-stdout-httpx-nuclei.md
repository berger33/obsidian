---
id: software.seguranca.tranche04.000348
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

# Subfinder: Encadeamento Unix (`stdin`/`stdout`) em Pipelines de Reconhecimento com `httpx`, `katana` e `nuclei`

## Em uma frase
Seguindo a filosofia Unix das ferramentas ProjectDiscovery, o `subfinder` aceita domínios via `stdin` e emite subdomínios limpos via `stdout` (`-silent`), encadeando-se diretamente com `httpx`, `katana` e `nuclei`.

## Por que importa
Permite construir pipelines automatizados de descoberta contínua que partem de uma lista de domínios raiz corporativos, descobrem subdomínios passivamente, verificam quais respondem via HTTP/TLS e auditam exposições críticas.

## Como funciona
O uso da flag `-silent` (e `-duc` para desativar checagens de atualização em pipelines de CI/CD) garante que apenas FQDNs válidos sejam impressos no `stdout`, evitando que banners ASCII ou logs informativos poluam a entrada da ferramenta seguinte no pipe.

## Exemplo
```bash
# Pipeline EASM completo: enumeração passiva -> probing HTTP/TLS -> detecção de tecnologias
cat root-domains.txt \
  | subfinder -silent -duc \
  | httpx -silent -duc -sc -title -td -json -o live-web-assets.jsonl
```

## Limites e trade-offs
Encadear `subfinder | httpx` diretamente em redes corporativas sem antes filtrar ativos fora de escopo (`-f`) enviará sondas HTTP ativas para todos os subdomínios encontrados nas fontes passivas.

## Como verificar
Verifique que `live-web-assets.jsonl` contém apenas linhas JSON válidas geradas pelo `httpx` sem mensagens de banner misturadas.

## Conexões
- [[subfinder-formatos-saida-jsonl-collect-sources-output-dir-audit]] — Veja também: Subfinder: Saída Estruturada JSONL (`-oJ`), Atribuição de Fontes (`-cs`) e Diretórios por Domínio (`-oD`).
- [[subfinder-uso-como-biblioteca-go-sdk-runner-enumerate]] — Veja também: Subfinder: Integração Programática em Go via SDK (`runner.NewRunner` e `EnumerateSingleDomainWithCtx`).
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
