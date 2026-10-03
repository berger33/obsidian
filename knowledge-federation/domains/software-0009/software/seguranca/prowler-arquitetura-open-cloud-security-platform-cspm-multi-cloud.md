---
id: software.seguranca.tranche02.000171
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md", "https://docs.prowler.com/introduction", "https://github.com/prowler-cloud/prowler"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Prowler: arquitetura da plataforma open-source de segurança e conformidade multi-cloud (`AWS`, `Azure`, `GCP`, `Kubernetes`, `M365`, `GitHub`)

## Em uma frase
Conforme documentado no README e na página oficial *What is Prowler?* (`docs.prowler.com/introduction`), o **Prowler** (`prowler-cloud/prowler`, licenciado sob Apache 2.0) é a plataforma open-source de **Cloud Security Posture Management (CSPM)** mais utilizada do mundo, automatizando avaliações de segurança, resposta a incidentes, hardening e conformidade contínua em **AWS**, **Azure**, **Google Cloud**, **Kubernetes**, **Alibaba Cloud**, **Oracle Cloud (OCI)**, **Cloudflare**, **OpenStack**, **GitHub**, **M365**, **Google Workspace**, **Okta**, **IaC** e **Container Images**.

## Por que importa
Com dezenas de contas AWS, subscrições Azure, projetos GCP, clusters Kubernetes e organizações GitHub, auditar configurações de IAM, criptografia, rede pública e logs manualmente é impossível e sujeito a deriva diária.

## Como funciona
O ecossistema open-source do Prowler compreende o **Prowler CLI** (`prowler <provider>`), o **Prowler Local Dashboard** (`prowler dashboard`) e o **Prowler Local Server / App** (aplicação web e API self-hosted com workers e banco de grafos de caminhos de ataque), apoiados pelo catálogo público **[Prowler Hub](https://hub.prowler.com/)**.

## Exemplo
```bash
# Executando uma auditoria completa de segurança com o Prowler CLI na conta AWS atual:
prowler aws

# Iniciando o dashboard visual interativo local para explorar os resultados gerados:
prowler dashboard
```

## Limites e trade-offs
Antes de iniciar varreduras em nuvem, utilize sempre credenciais somente-leitura de auditoria (na AWS, as políticas gerenciadas `SecurityAudit` e `ViewOnlyAccess` + permissões pontuais documentadas pelo Prowler).

## Como verificar
Execute `prowler -v` e `prowler aws --list-services` para verificar a instalação e a cobertura de serviços.

## Conexões
- [[prowler-compliance-frameworks-cis-nist-pci-dss-soc2-iso27001-nis2-ens]] — Veja também: Prowler Frameworks de Conformidade (`--compliance`) e `Prowler ThreatScore`: auditoria automatizada `CIS`, `NIST`, `PCI-DSS`, `SOC2`, `ISO 27001` e `MITRE ATT&CK`.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://docs.prowler.com/introduction) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
