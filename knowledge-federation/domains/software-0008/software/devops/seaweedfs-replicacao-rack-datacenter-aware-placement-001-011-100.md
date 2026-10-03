---
id: software.devops.tranche18.001722
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

# SeaweedFS: política de replicação ciente de topologia (`ReplicaPlacement` de 3 dígitos XYZ por Data Center, Rack e Nó)

## Em uma frase
O SeaweedFS controla a durabilidade e a localização física dos volumes por meio de um código de posicionamento de replicação de **3 dígitos (`XYZ`)**, onde `X` é o número de cópias adicionais em outros Data Centers, `Y` no mesmo Data Center mas em outros Racks e `Z` no mesmo Rack mas em outros nós.

## Por que importa
Declarar apenas "quero 3 réplicas" sem informar a topologia física de racks e data centers pode colocar todas as cópias no mesmo rack; por outro lado, replicar tudo entre dataCenters distantes quando bastava tolerar a falha de 1 servidor encarece o tráfego WAN.

## Como funciona
Os códigos seguem aritmética direta (total de cópias = $1 + X + Y + Z$): `"000"` significa sem replicação (1 cópia); `"001"` cria 1 cópia extra em outro servidor do mesmo rack (2 cópias no total); `"010"` cria 1 cópia extra em outro rack (2 cópias); `"011"` cria 3 cópias (1 local, 1 em outro nó do mesmo rack e 1 em outro rack); e `"100"` replica entre 2 data centers.

## Exemplo
```yaml
# Trecho do values.yaml do Helm chart do SeaweedFS:
global:
  seaweedfs:
    enableReplication: true
    replicationPlacement: "001"
master:
  replicas: 3
volume:
  replicas: 3
```

## Limites e trade-offs
O número de réplicas de `Volume Servers` ativos na topologia deve ser no mínimo igual a $1 + X + Y + Z$; caso contrário, o Master recusará alocar volumes para aquele `replicationPlacement`.

## Como verificar
Inspecione a topologia e os volumes alocados no cluster consultando o endpoint HTTP do Master (`curl http://localhost:9333/dir/status`).

## Conexões
- [[seaweedfs-arquitetura-haystack-o1-disk-read-master-volume-filer]] — Veja também: SeaweedFS: arquitetura inspirada no Facebook Haystack com leitura de disco $O(1)$ (`Master`, `Volume Server` e `Filer`).
- [[seaweedfs-erasure-coding-volumes-mornos-cloud-tiering-rust-volume]] — Veja também: SeaweedFS: Erasure Coding em segundo plano para dados mornos, Cloud Tiering e Volume Server em Rust.

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
