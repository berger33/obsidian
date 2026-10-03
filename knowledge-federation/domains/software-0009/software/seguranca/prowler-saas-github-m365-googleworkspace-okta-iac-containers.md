---
id: software.seguranca.tranche02.000177
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
fontes: ["https://docs.prowler.com/introduction", "https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md", "https://github.com/prowler-cloud/prowler"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Prowler SaaS, IaC e Containers (`github`, `m365`, `googleworkspace`, `okta`, `iac`, `image`): postura unificada além da IaaS

## Em uma frase
Conforme a matriz oficial de *Supported Providers* (`docs.prowler.com/introduction`), o Prowler expande o CSPM para provedores **SaaS** (**`github`**, **`m365`**, **`googleworkspace`**, **`okta`**, **`mongodbatlas`**, **`vercel`**, **`cloudflare`**), **Infrastructure as Code (`iac`)** e **Container Images (`image`)**.

## Por que importa
Um atacante frequentemente entra na nuvem comprometendo primeiro a organização do **GitHub** (repositório sem proteção de branch, Action insegura, MFA desativado na organização), o tenant do **Okta / Microsoft 365** ou um manifesto **IaC** antes do deploy.

## Como funciona
Com o provedor `prowler github` (autenticado via Personal Access Token, OAuth App Token ou GitHub App), você audita configurações de segurança de toda a sua organização e repositórios GitHub usando a mesma CLI, os mesmos relatórios OCSF e o mesmo painel do Prowler que já usa para AWS/Azure/GCP!

## Exemplo
```bash
# Auditando a postura de segurança de uma organização no GitHub e de um diretório IaC local:
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_..."
prowler github --organizations minha-org-corp

# Escaneando código de infraestrutura (Terraform/CloudFormation/Kubernetes) com o provedor IaC do Prowler:
prowler iac --scan-path ./infra-terraform
```

## Limites e trade-offs
No provedor `prowler image`, o Prowler inspeciona imagens de container locais ou em registries remotos, unificando vulnerabilidades de imagem e postura de nuvem no mesmo relatório.

## Como verificar
Execute `prowler github --list-checks` para inspecionar os controles CIS GitHub Benchmark implementados.

## Conexões
- [[prowler-auditoria-kubernetes-clusters-kubeconfig-in-cluster-rbac-pss]] — Veja também: Prowler para Kubernetes (`prowler kubernetes`): auditoria CIS Kubernetes Benchmark, RBAC, Pod Security e NetworkPolicies.
- [[prowler-formatos-saida-ocsf-asff-security-hub-s3-defectdojo]] — Veja também: Prowler Formatos de Saída (`json-ocsf`, `json-asff`, `html`, `csv`) e Integração Nativa com `AWS Security Hub` e `S3`.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://docs.prowler.com/introduction) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
