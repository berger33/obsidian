---
id: software.seguranca.tranche10.000912
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

# CloudQuery: Configuração Fina de **Fontes (`tables`, `skip_tables`, `concurrency`)** e Escalonamento Inteligente (`dfs`, `round-robin`, `shuffle`)

## Em uma frase
Um plugin de nuvem completo como o `cloudquery/aws` possui mais de **350 tabelas de nível superior e centenas de relações filhas** (cobrindo todos os serviços da AWS): tentar sincronizar `tables: ["*"]` em 50 contas AWS e 30 regiões sem filtro levaria horas e consumiria milhões de chamadas de API.

## Por que importa
Por isso, o manifesto `kind: source` do CloudQuery permite selecionar com precisão cirúrgica e suporte a globbing quais tabelas extrair (**`tables`**) e quais tabelas caras ou irrelevantes pular (**`skip_tables`**, além de **`skip_dependent_tables: true`** quando você não precisa das sub-tabelas filhas!).

## Como funciona
Para otimizar o throughput sem sofrer *throttling* (`ThrottlingException`) das APIs da nuvem, você ajusta a **Concorrência de Goroutines (`concurrency`, ex.: `10000`)** e a **Estratégia do Escalonador (`scheduler`)**: **`dfs`** (*depth-first search*), **`round-robin`** ou **`shuffle`** (que embaralha a ordem de coleta entre contas e serviços para distribuir uniformemente as chamadas de API pelos limites de taxa da AWS/GCP!)!

## Exemplo
```yaml
# aws-source.yml — Coleta focada em IAM, Rede e Armazenamento com estrategia shuffle para evitar rate-limit da AWS
kind: source
spec:
  name: aws
  path: cloudquery/aws
  registry: cloudquery
  version: "v27.0.0"
  concurrency: 10000
  scheduler: shuffle
  tables:
    - "aws_iam_*"
    - "aws_s3_buckets"
    - "aws_ec2_instances"
    - "aws_ec2_security_groups"
    - "aws_rds_instances"
    - "aws_kms_keys"
  skip_tables:
    - "aws_iam_SimulatePrincipalPolicy"
  destinations: ["postgresql"]
  spec:
    regions: ["sa-east-1", "us-east-1"]
```

## Limites e trade-offs
A estratégia **`scheduler: shuffle`** é especialmente recomendada ao sincronizar múltiplas contas/regiões na AWS ou GCP: em vez de martelar a API de `ec2` em todas as contas ao mesmo tempo (estourando a cota de EC2), o `shuffle` espalha as requisições entre S3, IAM, RDS, KMS e EC2 simultaneamente!

## Como verificar
Use `cloudquery tables config.yml` para gerar a documentação local de todas as tabelas e colunas que serão sincronizadas pelo seu arquivo YAML.

## Conexões
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Veja também: **CloudQuery (`cloudquery/cloudquery`)**: Arquitetura **ELT (*Extract-Load-Transform*)** de Alta Performance baseada em **Apache Arrow** e Plugins gRPC.
- [[cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append]] — Veja também: CloudQuery: Modos de Escrita no Destino (**`overwrite-delete-stale`**, **`overwrite`** e **`append`**) e Migração Automática de Schema (`migrate_mode`).
- [[cloudquery-descoberta-multi-conta-aws-organizations-gcp-folders-azure]] — Referência cruzada direta com cloudquery-descoberta-multi-conta-aws-organizations-gcp-folders-azure.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
