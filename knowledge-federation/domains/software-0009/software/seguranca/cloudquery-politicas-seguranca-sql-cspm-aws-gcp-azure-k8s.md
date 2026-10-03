---
id: software.seguranca.tranche10.000915
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
fontes: ["https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md", "https://www.cloudquery.io/docs/cli/getting-started"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CloudQuery **CSPM Policies em SQL**: Execução de Views de Conformidade (**CIS, NIST, PCI DSS**) e Detecção de Exposição Pública sobre o Banco Sincronizado

## Em uma frase
Uma vez que os metadados de configuração da AWS, GCP, Azure e Kubernetes estão normalizados no **PostgreSQL** (ou BigQuery/Snowflake/DuckDB), toda verificação de segurança e conformidade vira **SQL puro de altíssima velocidade** — executando milhares de verificações em poucos segundos sobre o banco local sem fazer nenhuma chamada de rede adicional para os provedores de nuvem!

## Por que importa
O CloudQuery fornece pacotes de **Políticas e Views SQL de CSPM** (cobrindo **AWS Foundational Security Best Practices, CIS Benchmarks para AWS/GCP/Azure/Kubernetes, PCI DSS e NIST**) que criam Views padronizadas de resultados (`framework`, `check_id`, `title`, `account_id`, `resource_id`, `status` = `'fail'` / `'pass'`).

## Como funciona
Além das políticas de conformidade prontas, sua equipe de Engenharia de Detecção pode criar Views SQL customizadas que cruzam múltiplas tabelas em milissegundos (por exemplo: encontrar instâncias EC2 que possuem **simultaneamente** um IP público, um Security Group com porta aberta para `0.0.0.0/0` **e** uma IAM Instance Profile anexada com permissões administrativas)!

## Exemplo
```sql
-- Query CSPM Composta (Toxic Combination): Instancias EC2 expostas para 0.0.0.0/0 E com IAM Role anexada!
SELECT
  i.account_id,
  i.region,
  i.instance_id,
  i.public_ip_address,
  i.iam_instance_profile ->> 'Arn' AS instance_profile_arn,
  sg.group_id
FROM
  aws_ec2_instances AS i
  CROSS JOIN LATERAL jsonb_array_elements(i.security_groups) AS isg
  JOIN aws_ec2_security_groups AS sg ON sg.group_id = (isg ->> 'GroupId')
WHERE
  i.public_ip_address IS NOT NULL
  AND i.iam_instance_profile IS NOT NULL
  AND sg.ip_permissions::text LIKE '%0.0.0.0/0%';
```

## Limites e trade-offs
Veja por que essa query de **Combinação Tóxica (*Toxic Combination*)** é o coração das plataformas modernas de CNAPP: um Security Group aberto isolado pode ser apenas uma web-server estática, e uma IAM Role isolada em sub-rede privada tem superfície menor, mas **um ativo que combina exposição pública de rede + identidade IAM privilegiada na mesma máquina é um risco crítico imediato**!

## Como verificar
Materialize suas queries de combinações tóxicas como Views SQL e conecte-as ao Grafana ou Alertmanager para alertas contínuos.

## Conexões
- [[cloudquery-descoberta-multi-conta-aws-organizations-gcp-folders-azure]] — Veja também: CloudQuery em Escala Enterprise: Descoberta Automática de Contas via **AWS Organizations (`org`)**, **GCP Folders** e **Azure Subscriptions**.
- [[cloudquery-sincronizacao-incremental-state-backend-cursor-otimizacao]] — Veja também: CloudQuery: **Sincronização Incremental (`backend_options`)** com Cursor de Estado para Tabelas de Grande Volume.
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.
- [[steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2]] — Referência cruzada direta com steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
