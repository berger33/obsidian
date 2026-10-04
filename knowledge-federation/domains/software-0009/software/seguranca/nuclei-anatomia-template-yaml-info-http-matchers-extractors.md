---
id: software.seguranca.tranche01.000052
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
fontes: ["https://docs.projectdiscovery.io/opensource/nuclei/overview", "https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md", "https://github.com/projectdiscovery/nuclei"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nuclei Anatomia de um Template YAML: metadados `info` (`severity`, `classification`, `tags`), `matchers` e `extractors`

## Em uma frase
Todo template do Nuclei é um arquivo YAML estruturado em um bloco obrigatório de metadados **`info:`** (contendo `name`, `author`, `severity`, `description`, `reference`, `classification` com `cve-id`/`cvss-metrics`/`cwe-id` e `tags`) seguido de um ou mais blocos de protocolo (como **`http:`**, `dns:`, `tcp:`, `ssl:`) com **`matchers`** e **`extractors`**.

## Por que importa
Padronizar a detecção de uma nova CVE ou falha de configuração interna em um arquivo YAML de 30 linhas permite que qualquer engenheiro de segurança transforme um *Proof of Concept (PoC)* manual em um teste de regressão automatizado em minutos.

## Como funciona
Dentro do bloco `http:`, você especifica `method` e `path` (usando variáveis como `{{BaseURL}}`), `matchers-condition: and` (exigindo que **todos** os matchers de status, header e palavra/regex no body sejam verdadeiros simultaneamente para evitar falsos positivos) e `extractors` (para capturar versões, tokens ou IDs da resposta).

## Exemplo
```yaml
id: exposed-prometheus-metrics-check

info:
  name: Exposed Prometheus Metrics Endpoint
  author: sec-team
  severity: low
  tags: config,prometheus,exposure

http:
  - method: GET
    path:
      - "{{BaseURL}}/metrics"
    matchers-condition: and
    matchers:
      - type: status
        status:
          - 200
      - type: word
        words:
          - "# HELP go_gc_duration_seconds"
          - "# TYPE"
        condition: and
```

## Limites e trade-offs
Use sempre **`matchers-condition: and`** combinando uma checagem de código HTTP (`status: [200]`) com strings exclusivas da resposta (`type: word` ou `type: dsl`) para que páginas genéricas de *catch-all* (que retornam HTTP 200 para qualquer URL) não gerem falsos positivos.

## Como verificar
Valide a sintaxe do seu template customizado executando `nuclei -t ./meu-template.yaml -validate`.

## Conexões
- [[nuclei-arquitetura-scanner-vulnerabilidades-templates-yaml-zero-false-positives]] — Veja também: ProjectDiscovery Nuclei: arquitetura do scanner de vulnerabilidades de alta performance baseado em templates YAML.
- [[nuclei-filtragem-templates-tags-severity-author-template-condition]] — Veja também: Nuclei Seleção e Filtragem de Templates: `-tags`, `-etags`, `-severity` (`critical,high`), `-tc` (Template Condition) e `-as` (Automatic Scan).

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
