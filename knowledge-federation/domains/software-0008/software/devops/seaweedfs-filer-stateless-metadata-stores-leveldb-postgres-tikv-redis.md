---
id: software.devops.tranche18.001724
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

# SeaweedFS `Filer`: camada stateless de diretórios e suporte a mais de 15 bancos de metadados plugáveis

## Em uma frase
O componente `Filer` do SeaweedFS traduz caminhos hierárquicos de diretórios e nomes de arquivos (`/buckets/app/relatorio.pdf`) para `file ids` de blobs nos Volume Servers, mantendo os próprios processos `weed filer` totalmente **stateless** ao persistir metadados de diretório em um banco externo plugável.

## Por que importa
Se o servidor de diretórios guardasse seu estado apenas na memória local, não seria possível escalar dezenas de instâncias de `Filer` e `S3 Gateway` horizontalmente atrás de um balanceador de carga.

## Como funciona
O `Filer` suporta nativamente desde motores embarcados locais (`LevelDB2`, `RocksDB`, `SQLite`) até bancos distribuídos de produção que a organização já opera: **PostgreSQL**, **MySQL/MariaDB**, **TiDB**, **CockroachDB**, **TiKV**, **FoundationDB**, **Redis**, **Cassandra**, **MongoDB**, **etcd**, **YDB** e **ArangoDB** (configurados em `filer.toml`).

## Exemplo
```toml
# /etc/seaweedfs/filer.toml usando PostgreSQL para escalar múltiplos Filers:
[postgres2]
enabled = true
hostname = "pg-ha.internal"
port = 5432
username = "seaweed"
password = "secret"
database = "seaweed_filer"
```

## Limites e trade-offs
Para clusters Kubernetes em produção com `filer.replicas: 2` ou mais, substitua o store local padrão (`leveldb2`) por um banco compartilhado (como PostgreSQL, MySQL, Redis ou TiKV) ou configure replicação de Filer Store para que todos os Filers enxerguem a mesma árvore.

## Como verificar
Suba duas réplicas de `weed filer` apontando para o mesmo banco PostgreSQL, crie um arquivo no Filer 1 via HTTP POST e faça download imediato pelo Filer 2.

## Conexões
- [[seaweedfs-erasure-coding-volumes-mornos-cloud-tiering-rust-volume]] — Veja também: SeaweedFS: Erasure Coding em segundo plano para dados mornos, Cloud Tiering e Volume Server em Rust.
- [[seaweedfs-s3-gateway-iam-sts-oidc-object-lock-sse-kms]] — Veja também: SeaweedFS S3 Gateway: API S3 completa (73 operações de objeto/bucket, 39 IAM, 5 STS), Object Lock e SSE-KMS.

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
