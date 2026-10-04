---
id: software.seguranca.tranche11.001020
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura Comparativa de Ferramentas Open-Source de Segurança Cloud: Quando Usar **Scout Suite vs Prowler vs Steampipe/Powerpipe vs CloudQuery vs Cartography**

## Em uma frase
Com cinco grandes ferramentas open-source de segurança de nuvem no nosso arsenal (**Scout Suite**, **Prowler**, **Steampipe/Powerpipe**, **CloudQuery** e **CNCF Cartography**), como o arquiteto de segurança escolhe a ferramenta certa (ou a combinação ideal) para cada cenário?

## Por que importa
Veja a matriz de especialização técnica: **(1) NCC Group Scout Suite** — imbatível para **Consultoria, Pentest Cloud e Auditoria Point-in-Time Offline**: você roda 1 comando, desconecta da conta e navega por toda a configuração e achados no painel HTML local (`--fetch-local`) sem precisar de banco de dados! **(2) Prowler** — o padrão de mercado para **Conformidade Contínua e Remediação** em AWS/Azure/GCP/K8s (+40 frameworks CIS/ENS/NIS2/PCI/HIPAA e saída nativa para AWS Security Hub/OCSF)!

## Como funciona
**(3) Steampipe & Powerpipe** — ideal para **Investigação Ad-Hoc Zero-ETL via SQL** em tempo real; **(4) CloudQuery** — motor **ELT em Apache Arrow** para sincronizar milhões de ativos em um Data Lake central (Postgres/BigQuery/Snowflake/DuckDB); e **(5) CNCF Cartography** — o motor de **Grafo Neo4j** para descobrir **Caminhos de Ataque Multi-Hop (`Attack Paths`)** cruzando Identidade (Okta/Entra), Nuvem (AWS/GCP/Azure), Kubernetes e CVEs (CISA KEV/EPSS)!

## Exemplo
```bash
# Pipeline complementar de Auditoria Cloud: Coleta Offline Interativa (Scout Suite) + Grafo de Caminhos de Ataque (Cartography)
scout aws --profile secops-audit --report-dir /cases/audit/scout --no-browser
cartography --neo4j-uri bolt://127.0.0.1:7687 --selected-modules aws
```

## Limites e trade-offs
Em uma arquitetura corporativa madura de **CNAPP / CSPM Open-Source**, essas ferramentas se complementam perfeitamente: o **CloudQuery** ou **Cartography** mantém o inventário e grafo central contínuo, o **Prowler** alimenta o Security Hub/SIEM diariamente, o **Steampipe** responde a perguntas SQL rápidas durante incidentes e o **Scout Suite** gera os pacotes de evidência HTML autocontidos para auditorias externas!

## Como verificar
Verifique sempre que todas as ferramentas acima utilizem exclusivamente roles IAM temporárias (`STS AssumeRole`) com privilégio mínimo somente-leitura.

## Conexões
- [[scoutsuite-extracao-dados-jq-automacao-cicd-defectdojo-ingestao]] — Veja também: Automação e Integração do Scout Suite em Pipelines CI/CD: Parsing do Payload JSON (`scoutsuite_results_*.js`) com **`jq`** e Ingestão no **DefectDojo**.
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Referência cruzada direta com scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup.
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.
- [[steampipe-comparacao-zero-etl-vs-cloudquery-elt-decisao-cspm]] — Referência cruzada direta com steampipe-comparacao-zero-etl-vs-cloudquery-elt-decisao-cspm.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
