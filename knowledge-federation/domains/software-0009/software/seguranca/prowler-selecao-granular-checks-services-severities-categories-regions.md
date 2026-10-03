---
id: software.seguranca.tranche02.000174
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

# Prowler Filtragem Granular de Execução: `--checks`, `--services`, `--severity`, `--category` e `--region` / `--excluded-checks`

## Em uma frase
Para executar verificações rápidas em pipelines de CI/CD ou focar em domínios específicos durante uma resposta a incidentes, o Prowler CLI oferece filtros precisos: **`-c` / `--checks`** (executa checks específicos), **`-s` / `--services`** (ex.: `iam s3 ec2 rds`), **`--severity`** (`critical high medium low informational`), **`--category`** (ex.: `internet-exposed`, `secrets`, `encryption`, ` forensics-ready`) e **`-f` / `--region`**, além de **`-e` / `--excluded-checks`** e **`--excluded-services`**.

## Por que importa
Rodar todos os 500+ checks em todas as 30 regiões da AWS leva vários minutos; se uma squad acabou de alterar apenas um módulo Terraform de S3 e IAM na região `sa-east-1`, filtrar por `-s s3 iam -f sa-east-1` entrega feedback em poucos segundos.

## Como funciona
Você pode explorar todo o catálogo localmente antes de rodar qualquer chamada na nuvem usando `--list-checks`, `--list-services` e `--list-categories`.

## Exemplo
```bash
# Auditando apenas falhas Críticas e Altas nos serviços IAM, S3 e KMS nas regiões sa-east-1 e us-east-1:
prowler aws \
  --services iam s3 kms \
  --severity critical high \
  --region sa-east-1 us-east-1
```

## Limites e trade-offs
Para descobrir rapidamente todos os recursos expostos publicamente na internet em uma conta recém-adquirida, execute `prowler aws --category internet-exposed`.

## Como verificar
Liste os checks de uma categoria com `prowler aws --list-checks --category encryption`.

## Conexões
- [[prowler-attack-paths-cartography-neo4j-amazon-neptune-grafos]] — Veja também: Prowler `Attack Paths`: análise de caminhos de ataque combinando inventário `Cartography` com achados do Prowler em `Neo4j` ou `Amazon Neptune`.
- [[prowler-mutelist-yaml-supressao-excecoes-accounts-regions-resources-tags]] — Veja também: Prowler `Mutelist` (`-w` / `--mutelist-file`): gerenciamento declarativo de exceções por conta, região, check, recurso e tags.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://docs.prowler.com/introduction) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
