---
id: software.seguranca.tranche01.000051
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

# ProjectDiscovery Nuclei: arquitetura do scanner de vulnerabilidades de alta performance baseado em templates YAML

## Em uma frase
O **Nuclei** (`projectdiscovery/nuclei`, escrito em Go e licenciado sob MIT) é um scanner de vulnerabilidades moderno e de alta performance que utiliza **templates declarativos em YAML** para simular passos reais de verificação e exploração controlada em múltiplos protocolos (**HTTP**, **DNS**, **TCP**, **SSL/TLS**, **Websocket**, **WHOIS**, **Headless**, **JavaScript** e **Code**), visando **zero falsos positivos**.

## Por que importa
Scanners tradicionais de vulnerabilidades frequentemente alertam uma CVE crítica baseando-se apenas no banner de versão do servidor HTTP (`Server: nginx/...`), mesmo quando o pacote já recebeu *backport* de correção pela distribuição Linux.

## Como funciona
No Nuclei, cada template YAML define exatamente a requisição/interação a ser enviada e os **matchers** precisos (status code, corpo da resposta, headers, expressões DSL ou interação *Out-of-Band* via Interactsh) que comprovam de forma inequívoca que a vulnerabilidade está presente e explorável no alvo.

## Exemplo
```bash
# Atualizando a biblioteca comunitária de templates e escaneando um alvo único:
nuclei -update-templates
nuclei -u https://staging.example.com
```

## Limites e trade-offs
Conforme o aviso importante no README oficial do Nuclei, a ferramenta foi projetada primordialmente para uso como **CLI standalone**; expor o binário `nuclei` diretamente como um serviço público compartilhado sem isolamento adicional pode trazer riscos de segurança.

## Como verificar
Execute `nuclei -version` e `nuclei -validate` para verificar a instalação do binário e a integridade dos templates.

## Conexões
- [[nuclei-anatomia-template-yaml-info-http-matchers-extractors]] — Veja também: Nuclei Anatomia de um Template YAML: metadados `info` (`severity`, `classification`, `tags`), `matchers` e `extractors`.

## Fontes
- [ProjectDiscovery Nuclei GitHub — README.md (YAML Template Engine, Multi-Protocol Support, Filtering Flags, Rate Limiting & CI/CD Reporting)](https://raw.githubusercontent.com/projectdiscovery/nuclei/main/README.md) — README oficial do projectdiscovery/nuclei documentando instalação, flags de filtragem de templates, controle de concorrência, OAST Interactsh e formatos de saída; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Nuclei Overview (Template Anatomy, Matchers/Extractors, Request Clustering, Workflows & Authenticated Scans)](https://docs.projectdiscovery.io/opensource/nuclei/overview) — Visão geral oficial da documentação do Nuclei explicando a anatomia dos templates YAML, agrupamento de requisições, fluxos multi-step e varreduras autenticadas; consultado em 2026-10-03.
- [ProjectDiscovery Nuclei — Official GitHub Repository](https://github.com/projectdiscovery/nuclei) — Repositório oficial MIT do ProjectDiscovery Nuclei; consultado em 2026-10-03.
