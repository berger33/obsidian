---
id: software.seguranca.tranche10.000904
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/turbot/steampipe/main/README.md", "https://raw.githubusercontent.com/turbot/powerpipe/main/README.md", "https://steampipe.io/docs/reference/cli/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **Powerpipe (`turbot/powerpipe`)**: Execução de +5.000 Controles de Conformidade (**CIS Benchmarks, NIST 800-53, PCI DSS, SOC 2, HIPAA**) sobre o Steampipe

## Em uma frase
Enquanto o **Steampipe** fornece a camada de acesso SQL às APIs, o **Powerpipe** (`turbot/powerpipe`, licença AGPLv3, sucessor dedicado dos antigos comandos `steampipe check`/`dashboard`) é o motor em Go para **Execução de Benchmarks de Conformidade e Dashboards as Code em HCL**!

## Por que importa
No **Powerpipe Hub (`hub.powerpipe.io`)**, existem dezenas de **Mods Open-Source** prontos (`aws_compliance`, `azure_compliance`, `gcp_compliance`, `kubernetes_compliance`, `github_compliance`, `terraform_compliance`) totalizando **mais de 5.000 controles automatizados** mapeados para **CIS Benchmarks, NIST SP 800-53, PCI DSS v4.0, SOC 2, HIPAA, GDPR e FedRAMP**!

## Como funciona
Cada controle em um Mod do Powerpipe executa uma query SQL parametrizada (no Steampipe, Postgres, DuckDB ou SQLite) que avalia cada recurso da nuvem e retorna o status **`ok`**, **`alarm`**, **`info`**, **`skip`** ou **`error`** junto com a razão exata (`reason`)!

## Exemplo
```bash
# Inicializar um workspace Powerpipe, instalar o Mod oficial de conformidade AWS e rodar o benchmark CIS v3.0
mkdir -p /cases/cspm/aws-audit && cd /cases/cspm/aws-audit
powerpipe mod init
powerpipe mod install github.com/turbot/steampipe-mod-aws-compliance
powerpipe benchmark run aws_compliance.benchmark.cis_v300 --output json > cis_v300_results.json
```

## Limites e trade-offs
A separação entre **Steampipe** (motor SQL FDW) e **Powerpipe** (motor de benchmarks/dashboards) trouxe uma vantagem arquitetural importante: o Powerpipe é **agnóstico de banco de dados**, podendo rodar os mesmos controles e dashboards quer em tempo real contra o `steampipe service`, quer contra um banco PostgreSQL/DuckDB populado pelo **CloudQuery**!

## Como verificar
Explore a árvore de sub-benchmarks disponíveis com `powerpipe benchmark list` antes de disparar uma avaliação.

## Conexões
- [[steampipe-agregadores-multi-conta-connections-spc-aws-organizations]] — Veja também: Steampipe: Conexões Multi-Conta e **Agregadores (`type = "aggregator"`)** em `~/.steampipe/config/*.spc` para Varrer **AWS Organizations / GCP Folders**.
- [[steampipe-autoria-controles-customizados-powerpipe-hcl-policy-as-code]] — Veja também: Powerpipe HCL: Autoria de **Controles e Benchmarks Customizados (*Policy-as-Code*)** com SQL (`status`, `reason`, `resource` e Dimensões).
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.

## Fontes
- [Turbot Steampipe Official GitHub — Zero-ETL SQL Engine & PostgreSQL FDW Architecture](https://raw.githubusercontent.com/turbot/steampipe/main/README.md) — repositório oficial do Steampipe cobrindo arquitetura Zero-ETL sobre PostgreSQL FDW, plugins multi-cloud e distribuições SQLite/Postgres; consultado em 2026-10-03.
- [Turbot Powerpipe Official GitHub — Dashboards & 5,000+ Compliance Benchmarks as Code in HCL](https://raw.githubusercontent.com/turbot/powerpipe/main/README.md) — repositório oficial do Powerpipe cobrindo execução de benchmarks CIS/NIST/PCI/SOC2/HIPAA e controles customizados em HCL; consultado em 2026-10-03.
- [Steampipe Official CLI & Exit Codes Reference Documentation](https://steampipe.io/docs/reference/cli/overview) — documentação oficial de subcomandos CLI (`query`, `service`, `plugin`), flags globais e códigos de saída do Steampipe; consultado em 2026-10-03.
