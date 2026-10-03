---
id: software.seguranca.tranche01.000060
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

# Nuclei Exportação e Integração CI/CD (`-sarif-export`, `-jsonl`, `-markdown-export` e `-rc` Report Config para Jira/GitHub/Splunk)

## Em uma frase
Para integrar os resultados das varreduras em pipelines de CI/CD e fluxos de gestão de vulnerabilidades, o Nuclei exporta nativamente em **SARIF** (`-se` / `-sarif-export`), **JSON Lines** (`-j` / `-jsonl`), **Markdown** (`-me` / `-markdown-export`, gerando um arquivo `.md` com request/response completo por achado) e integra-se diretamente com **Jira**, **GitHub Issues**, **GitLab Issues**, **Splunk** e **Elasticsearch** via **`-rc` / `-report-config`**.

## Por que importa
Quando um teste de regressão de segurança no Nuclei detecta uma falha, o desenvolvedor precisa ver a requisição HTTP exata (`curl` reproduzível) e o trecho da resposta que disparou o matcher diretamente na issue ou na aba de Code Scanning.

## Como funciona
Configurando um arquivo `issue-tracker-config.yaml` passado em `-rc` (com deduplicação e filtro de severidade), o Nuclei abre tickets automaticamente com a reprodução completa apenas para vulnerabilidades novas.

## Exemplo
```bash
# Executando Nuclei no CI gerando simultaneamente saída SARIF e diretório de relatórios Markdown:
nuclei -u https://staging.example.com \
  -tags misconfig,exposure \
  -sarif-export nuclei-results.sarif \
  -markdown-export ./nuclei-reports-md/
```

## Limites e trade-offs
Nos relatórios gerados por `-jsonl` ou `-me`, o Nuclei já inclui o comando `curl-command` pronto para copiar e reproduzir a vulnerabilidade manualmente.

## Como verificar
Valide o arquivo SARIF gerado com `jq '.runs[0].results | length' nuclei-results.sarif`.

## Conexões
- [[nuclei-headless-browser-dast-fuzzing-code-templates-assinatura]] — Veja também: Nuclei Modo Headless (`-headless`), Fuzzing DAST (`-dast`) e Assinatura Criptográfica de Templates `code:`.

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
