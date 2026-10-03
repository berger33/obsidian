---
id: software.devops.tranche18.001726
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md", "https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md", "https://github.com/seaweedfs/seaweedfs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SeaweedFS Lakehouse: S3 Table Buckets com catálogo REST Apache Iceberg e tabelas vetoriais Lance integrados

## Em uma frase
O SeaweedFS funciona como um *Data Lakehouse* completo em um único binário ao fornecer **S3 Table Buckets** (36 operações da API S3 Tables) com **Iceberg REST Catalog** e namespace **Lance** nativos embutidos, além de manutenção automatizada de tabelas.

## Por que importa
Montar um Lakehouse tradicional exige implantar, proteger e fazer backup de serviços extras separados (como Hive Metastore, AWS Glue ou Polaris) além de agendar jobs externos para compactar pequenos arquivos Parquet e expirar snapshots do Iceberg.

## Como funciona
Ao definir `S3_TABLE_BUCKET=warehouse` (para Apache Iceberg) ou `warehouse:LANCE` (para dados vetoriais e multimodais com Lance/LanceDB), motores como **Spark**, **Trino**, **DuckDB**, **Dremio**, **ClickHouse**, **Apache Doris** e **RisingWave** consultam e gravam nas mesmas tabelas concorrentemente com commits atômicos *compare-and-swap*, enquanto o SeaweedFS executa compactação, expiração de snapshots e limpeza de arquivos órfãos automaticamente.

## Exemplo
```bash
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
S3_TABLE_BUCKET=warehouse \
./weed mini -dir=./data
```

## Limites e trade-offs
As permissões de acesso no Lakehouse do SeaweedFS são governadas no nível de bucket, namespace e tabela usando políticas IAM/bucket padrão da API S3 Tables.

## Como verificar
Inicie o `weed mini` com `S3_TABLE_BUCKET=warehouse` e conecte o DuckDB ou PyIceberg ao endpoint do catálogo REST embutido para criar e consultar uma tabela Iceberg.

## Conexões
- [[seaweedfs-s3-gateway-iam-sts-oidc-object-lock-sse-kms]] — Veja também: SeaweedFS S3 Gateway: API S3 completa (73 operações de objeto/bucket, 39 IAM, 5 STS), Object Lock e SSE-KMS.
- [[seaweedfs-cloud-drive-cache-remoto-writeback-replicacao-ativo-ativo]] — Veja também: SeaweedFS `Cloud Drive` e Replicação Ativo-Ativo: cache local acelerado de buckets de nuvem e sincronização multi-cluster.

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
