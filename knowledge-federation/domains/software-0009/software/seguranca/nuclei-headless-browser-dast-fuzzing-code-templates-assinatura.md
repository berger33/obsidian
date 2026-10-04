---
id: software.seguranca.tranche01.000059
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

# Nuclei Modo Headless (`-headless`), Fuzzing DAST (`-dast`) e Assinatura Criptográfica de Templates `code:`

## Em uma frase
Para casos avançados que exigem execução de JavaScript no navegador ou lógica customizada, o Nuclei suporta **templates `headless:`** (habilitados via flag **`-headless`**, que navegam no DOM e detectam *DOM-based XSS*), **templates de Fuzzing (`-dast` / `-fuzz`)** (que injetam payloads em query params, headers e bodies) e **templates `code:`** (que exigem **assinatura criptográfica obrigatória** por segurança).

## Por que importa
Como um template `code:` pode executar comandos locais (Python, Bash, Sh, Go) na máquina onde o Nuclei está rodando, executar um template `code:` baixado da internet sem verificar sua assinatura permitiria execução remota de código no próprio runner de segurança!

## Como funciona
Por esse motivo, o Nuclei **bloqueia por padrão** a execução de qualquer template `code:` que não esteja criptograficamente assinado pela chave confiável do usuário (`nuclei -sign`) E sem a flag explícita `-code` na linha de comando.

## Exemplo
```bash
# Assinando um template customizado local e executando varredura headless para DOM XSS:
nuclei -u https://staging.example.com -headless -tags xss
```

## Limites e trade-offs
Nunca execute templates de terceiros não revisados com a flag `-code` habilitada em máquinas com acesso a credenciais de produção.

## Como verificar
Verifique os templates headless disponíveis com `nuclei -tl -type headless`.

## Conexões
- [[nuclei-controle-taxa-concorrencia-rate-limit-bulk-size-request-clustering]] — Veja também: Nuclei Performance, *Request Clustering* e Rate Limiting (`-rl`, `-c`, `-bs`): proteção do alvo e otimização de tráfego.
- [[nuclei-relatorios-exportacao-sarif-jsonl-markdown-integracao-jira-github]] — Veja também: Nuclei Exportação e Integração CI/CD (`-sarif-export`, `-jsonl`, `-markdown-export` e `-rc` Report Config para Jira/GitHub/Splunk).

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
