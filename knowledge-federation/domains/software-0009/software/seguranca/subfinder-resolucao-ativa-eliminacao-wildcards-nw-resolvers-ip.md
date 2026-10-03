---
id: software.seguranca.tranche04.000344
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

# Subfinder: Resolução DNS Ativa (`-nW` / `-active`), Eliminação de Wildcards e Extração de IPs (`-oI`)

## Em uma frase
Embora seja passivo por padrão, o `subfinder` possui um módulo interno de resolução DNS ativa e eliminação de *wildcards* (`-nW` / `-active`) configurável com listas de resolvedores confiáveis (`-r` / `-rL`) e concorrência (`-t`).

## Por que importa
Domínios configurados com registros DNS wildcard (`*.example.corp IN A 198.51.100.10`) fazem com que qualquer subdomínio histórico ou inexistente pareça ativo; o filtro de wildcard descarta respostas sintéticas falsas.

## Como funciona
Quando `-nW` (`-active`) é especificado, o `subfinder` resolve cada subdomínio encontrado pelas fontes passivas usando as goroutines configuradas em `-t` contra os servidores DNS de `-rL resolvers.txt`, testa se o domínio pai responde para nomes aleatórios (wildcard DNS) e, se `-oI` (`-ip`) for combinado com `-oJ`, inclui o endereço IP resolvido e a fonte de descoberta.

## Exemplo
```bash
# Filtrar apenas subdomínios atualmente ativos no DNS com IP resolvido e sem falsos positivos de wildcard
subfinder -d example.corp \
  -nW -oI -cs -oJ \
  -r 1.1.1.1,8.8.8.8,9.9.9.9 \
  -t 30 -o active-subdomains.jsonl
```

## Limites e trade-offs
Habilitar `-nW` transforma a execução de puramente passiva em resolução DNS ativa; se o servidor DNS autoritativo do alvo for monitorado, ele verá consultas para os subdomínios enumerados.

## Como verificar
Inspecione `jq -c '{host, ip, source}' active-subdomains.jsonl` e confirme que todos os registros emitidos possuem endereço IP válido resolvido.

## Conexões
- [[subfinder-selecao-fontes-recursive-all-exclude-sources-max-results]] — Veja também: Subfinder: Seleção Granular de Fontes (`-s`, `-es`, `-all`, `-recursive`) e Paginação (`-mr`).
- [[subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao]] — Veja também: Subfinder: Rate-Limiting Global (`-rl`) e por Provedor (`-rls`), Timeouts e Limite de Leitura (`-rsr`).
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.
- [[subfinder-filtragem-escopo-match-filter-exclude-ip]] — Referência cruzada direta com subfinder-filtragem-escopo-match-filter-exclude-ip.
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
