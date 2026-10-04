---
id: software.devops.tranche18.001727
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

# SeaweedFS `Cloud Drive` e Replicação Ativo-Ativo: cache local acelerado de buckets de nuvem e sincronização multi-cluster

## Em uma frase
O recurso **Cloud Drive** do SeaweedFS monta buckets externos (Amazon S3, GCS, Azure, Backblaze B2, Wasabi) dentro do cluster local servindo listagens e leituras na velocidade dos discos locais e gravando de volta na nuvem de forma assíncrona no layout nativo do bucket.

## Por que importa
Ler os mesmos objetos repetidamente de uma nuvem pública gera cobranças elevadas de *egress* e chamadas de API (`LIST`/`HEAD`), além de alta latência para clusters on-premises ou de borda.

## Como funciona
No Cloud Drive, os metadados são baixados uma única vez (tornando `ls`, `stat` e varreduras de diretório gratuitas em chamadas de nuvem), o conteúdo é cacheado na capacidade agregada do cluster (ou pré-aquecido por regras de pasta/padrão/idade) e as escritas locais completam em latência local com write-back assíncrono. Adicionalmente, o SeaweedFS oferece **replicação ativo-ativo ou ativo-passivo** contínua e retomável entre clusters distintos e CDC via webhooks.

## Exemplo
```bash
# Conectando ao weed shell para configurar ou verificar montagens remotas:
weed shell -master=localhost:9333 <<< "remote.mount.buckets"
```

## Limites e trade-offs
Como o Cloud Drive grava os objetos de volta na nuvem preservando o layout nativo do bucket remoto, outras ferramentas externas podem continuar lendo o bucket na nuvem diretamente sem depender do SeaweedFS.

## Como verificar
Verifique o status de sincronização e as regras de cache/uncache do Cloud Drive através do `weed shell` e das métricas Prometheus.

## Conexões
- [[seaweedfs-lakehouse-s3-tables-apache-iceberg-rest-catalog-lance]] — Veja também: SeaweedFS Lakehouse: S3 Table Buckets com catálogo REST Apache Iceberg e tabelas vetoriais Lance integrados.
- [[seaweedfs-csi-driver-kubernetes-provisionamento-dinamico-estatico-rwx]] — Veja também: SeaweedFS CSI Driver: provisionamento dinâmico e estático de volumes `ReadWriteMany` no Kubernetes.

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
