---
id: software.seguranca.tranche02.000179
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

# Prowler Varreduras Multi-Conta em Escala: `AWS AssumeRole` (`-R`), `AWS Organizations` (`-O`), Subscrições Azure e Projetos GCP

## Em uma frase
Em ambientes corporativos com dezenas ou centenas de contas na nuvem, o Prowler suporta assumir Roles IAM entre contas na AWS via **`-R` / `--role <ARN>`** (com `--sts-endpoint-region` e `--external-id`), buscar metadados da **AWS Organizations (`-O` / `--organizations-role`)**, varrer múltiplas **Subscrições Azure (`prowler azure --sp-env-auth --subscription-ids ...`)** e varrer todos os **Projetos Google Cloud (`prowler gcp --organization-id ...`)**.

## Por que importa
Implantar e manter credenciais estáticas separadas em 150 contas AWS é inseguro; usar uma única Role de auditoria central que assume `arn:aws:iam::<ACCOUNT_ID>:role/ProwlerAuditRole` via AWS STS em cada conta membro segue o modelo Zero-Trust da AWS Organizations.

## Como funciona
Com um StackSet do AWS CloudFormation (ou módulo Terraform) implantando a role `ProwlerAuditRole` em todas as contas da organização, um único job orquestrador percorre todas as contas em paralelo e consolida os relatórios com tags da conta na AWS Organizations.

## Exemplo
```bash
# Executando o Prowler assumindo uma Role IAM de auditoria em uma conta membro via AWS STS:
prowler aws \
  --role arn:aws:iam::111122223333:role/ProwlerAuditRole \
  --session-duration 3600 \
  --external-id "corp-sec-audit-2026"
```

## Limites e trade-offs
Defina sempre um `sts:ExternalId` exclusivo na Trust Policy da Role de auditoria quando a conta orquestradora operar em contexto multi-tenant (*Confused Deputy Prevention*).

## Como verificar
Verifique a identidade STS assumida no início da execução do Prowler (`Caller Identity`).

## Conexões
- [[prowler-formatos-saida-ocsf-asff-security-hub-s3-defectdojo]] — Veja também: Prowler Formatos de Saída (`json-ocsf`, `json-asff`, `html`, `csv`) e Integração Nativa com `AWS Security Hub` e `S3`.
- [[prowler-custom-checks-python-metadata-guidelines-prowler-mcp-ai]] — Veja também: Prowler Extensibilidade: criação de Checks Customizados (`--checks-folder`), `Check Metadata Guidelines` e servidor `Prowler MCP`.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://docs.prowler.com/introduction) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
