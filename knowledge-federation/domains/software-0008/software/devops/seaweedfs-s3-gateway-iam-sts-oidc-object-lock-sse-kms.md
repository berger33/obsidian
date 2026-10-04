---
id: software.devops.tranche18.001725
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

# SeaweedFS S3 Gateway: API S3 completa (73 operações de objeto/bucket, 39 IAM, 5 STS), Object Lock e SSE-KMS

## Em uma frase
O S3 Gateway do SeaweedFS expõe em um único endpoint (porta `8333`) **73 operações S3 de bucket/objeto**, **36 operações de S3 Tables**, **39 operações de IAM** e **5 operações de STS** (incluindo federação com OIDC, LDAP e `ServiceAccounts` do Kubernetes).

## Por que importa
Aplicações corporativas e ferramentas de backup (`restic`, `velero`, `rclone`, `Spark`, `Trino`) exigem recursos avançados da API AWS S3 — como *Object Lock* (WORM com retenção e *legal hold*), versionamento, políticas de bucket com variáveis, credenciais temporárias STS e criptografia SSE-KMS.

## Como funciona
No SeaweedFS, cada bucket S3 é mapeado para sua própria `collection` interna (tornando a deleção de um bucket inteiro instantânea), com suporte a **SSE-S3**, **SSE-KMS** (integrado a OpenBao, HashiCorp Vault, AWS KMS, Azure Key Vault e GCP KMS) e **SSE-C**, além da operação atômica `RenameObject` e cotas/rate-limiting por bucket.

## Exemplo
```bash
AWS_ACCESS_KEY_ID=admin AWS_SECRET_ACCESS_KEY=change-me \
  aws --endpoint-url http://localhost:8333 s3api create-bucket \
  --bucket immutable-backups --object-lock-enabled-for-bucket
```

## Limites e trade-offs
Ao habilitar `s3.enableAuth: true` no Helm chart do SeaweedFS, configure as credenciais iniciais em `s3.credentials` ou gerencie usuários, grupos e políticas dinamicamente pela API IAM embutida.

## Como verificar
Execute `aws --endpoint-url http://localhost:8333 s3 ls` e teste a emissão de credenciais temporárias via `sts assume-role-with-web-identity`.

## Conexões
- [[seaweedfs-filer-stateless-metadata-stores-leveldb-postgres-tikv-redis]] — Veja também: SeaweedFS `Filer`: camada stateless de diretórios e suporte a mais de 15 bancos de metadados plugáveis.
- [[seaweedfs-lakehouse-s3-tables-apache-iceberg-rest-catalog-lance]] — Veja também: SeaweedFS Lakehouse: S3 Table Buckets com catálogo REST Apache Iceberg e tabelas vetoriais Lance integrados.

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
