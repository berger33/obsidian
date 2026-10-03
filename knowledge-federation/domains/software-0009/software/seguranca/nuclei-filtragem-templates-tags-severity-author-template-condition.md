---
id: software.seguranca.tranche01.000053
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

# Nuclei Seleção e Filtragem de Templates: `-tags`, `-etags`, `-severity` (`critical,high`), `-tc` (Template Condition) e `-as` (Automatic Scan)

## Em uma frase
Com mais de 6.500 templates na biblioteca oficial `nuclei-templates`, o Nuclei oferece filtros granulares na linha de comando: **`-s` / `-severity`** (`info,low,medium,high,critical`), **`-tags`** (incluir tags como `cve,exposure,misconfig`), **`-etags`** (excluir tags intrusivas como `dos,fuzz,intrusive`), **`-tc`** (expressões lógicas sobre metadados) e **`-as` / `-automatic-scan`** (seleção automática baseada em fingerprint tecnológico Wappalyzer).

## Por que importa
Disparar todos os 6.500+ templates (incluindo WordPress, Joomla, Cisco e F5) contra um microserviço em Go desperdiça milhares de requisições; o modo **`-as`** identifica primeiro a stack tecnológica do alvo e executa apenas os templates correspondentes.

## Como funciona
Além disso, a flag **`-nh` / `-new-templates`** executa exclusivamente os templates adicionados na última atualização do `nuclei-templates`, ideal para varreduras rápidas diárias quando novas CVEs saem.

## Exemplo
```bash
# Escaneando apenas vulnerabilidades críticas e altas de CVEs e exposições, excluindo testes intrusivos:
nuclei -l urls.txt -severity critical,high -tags cve,exposure -etags dos,intrusive

# Seleção automática de templates por detecção de tecnologia (Wappalyzer):
nuclei -u https://staging.example.com -as
```

## Limites e trade-offs
Em ambientes de produção, inclua sempre `-etags dos,fuzz,intrusive` para garantir que nenhum template de negação de serviço ou fuzzing pesado seja executado.

## Como verificar
Liste os templates que seriam selecionados pelos seus filtros sem enviar tráfego de rede adicionando a flag **`-tl`** (*template list*).

## Conexões
- [[nuclei-anatomia-template-yaml-info-http-matchers-extractors]] — Veja também: Nuclei Anatomia de um Template YAML: metadados `info` (`severity`, `classification`, `tags`), `matchers` e `extractors`.
- [[nuclei-multi-protocolo-dns-ssl-tcp-websocket-whois-network-scans]] — Veja também: Nuclei Além do HTTP: templates multi-protocolo para auditoria de `DNS`, `SSL/TLS`, `TCP`, `WHOIS` e serviços de rede.

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
