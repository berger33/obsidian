---
id: software.seguranca.tranche01.000058
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md", "https://docs.projectdiscovery.io/opensource/nuclei/overview", "https://github.com/projectdiscovery/nuclei"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nuclei Performance, *Request Clustering* e Rate Limiting (`-rl`, `-c`, `-bs`): proteção do alvo e otimização de tráfego

## Em uma frase
O motor do Nuclei inclui **Request Clustering** (agrupamento inteligente de múltiplos templates que fazem exatamente a mesma requisição `GET {{BaseURL}}/config.json`, enviando apenas 1 pacote HTTP e avaliando as respostas contra dezenas de templates em memória) e flags precisas de controle de carga: **`-rl` / `-rate-limit`** (requisições por segundo, padrão `150`), **`-c` / `-concurrency`** (templates em paralelo, padrão `25`) e **`-bs` / `-bulk-size`** (hosts em paralelo por template, padrão `25`).

## Por que importa
Sem controle de taxa (`-rl`), um scanner rápido escrito em Go pode disparar centenas de requisições por segundo contra um ambiente de homologação pequeno, derrubando o banco de dados ou acionando bloqueio imediato no WAF.

## Como funciona
Ajustar `-rl 30 -c 10 -bs 5` mantém a carga suave e previsível sobre um único serviço em staging, enquanto a flag **`-resume`** permite retomar uma varredura interrompida exatamente do ponto onde parou a partir do arquivo de checkpoint.

## Exemplo
```bash
# Executando varredura com limite estrito de 30 requisições/s, timeout de 10s e exclusão de hosts sensíveis:
nuclei -l targets.txt \
  -eh prod-payment.example.com \
  -rl 30 \
  -c 10 \
  -bs 5 \
  -timeout 10
```

## Limites e trade-offs
Use sempre a flag **`-eh` / `-exclude-hosts`** (aceitando IPs, CIDRs ou hostnames) para garantir que endereços sensíveis ou fora do escopo autorizado jamais sejam escaneados mesmo se constarem acidentalmente na lista de entrada.

## Como verificar
Execute com `-stats` para visualizar em tempo real no terminal a taxa de requisições por segundo (`RPS`), progresso percentual e matches.

## Conexões
- [[nuclei-authenticated-scans-secrets-file-headers-variables-ci-cd]] — Veja também: Nuclei Varreduras Autenticadas (`-H`, `-var` e arquivo de `secrets` com `pre-condition`): autenticação dinâmica em APIs e aplicações.
- [[nuclei-headless-browser-dast-fuzzing-code-templates-assinatura]] — Veja também: Nuclei Modo Headless (`-headless`), Fuzzing DAST (`-dast`) e Assinatura Criptográfica de Templates `code:`.

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
