---
id: software.devops.tranche18.001721
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

# SeaweedFS: arquitetura inspirada no Facebook Haystack com leitura de disco $O(1)$ (`Master`, `Volume Server` e `Filer`)

## Em uma frase
O SeaweedFS (licenciado sob Apache 2.0) é um sistema de armazenamento distribuído altamente escalável cujo único binário `weed` serve simultaneamente uma Object Store compatível com S3, um sistema de arquivos POSIX e um Lakehouse com S3 Tables/Iceberg com complexidade de leitura e escrita $O(1)$.

## Por que importa
Em sistemas de arquivos tradicionais, ler um arquivo pequeno de 4 KB exige múltiplas leituras de disco para percorrer inodes e diretórios, e o servidor central de metadados (como o NameNode do HDFS) estoura a memória RAM ao tentar rastrear bilhões de arquivos individuais.

## Como funciona
Baseado no artigo *Haystack* do Facebook, o SeaweedFS divide responsabilidades: 1) **Master Servers** (1 ou grupo Raft de 3) rastreiam apenas **volumes** (alguns milhares de volumes para bilhões de arquivos) e distribuem `file ids`, ficando fora do caminho de leitura; 2) **Volume Servers** empacotam milhares de blobs em grandes arquivos de volume append-only, mantendo apenas **16 bytes de índice em RAM por blob** e **40 bytes de metadados em disco**, lendo qualquer blob em **1 único seek de disco**; e 3) **Filer Servers** (stateless) adicionam hierarquia de diretórios, S3, WebDAV, SFTP e FUSE.

## Exemplo
```bash
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
S3_BUCKET=my-bucket \
./weed mini -dir=./data
```

## Limites e trade-offs
O comando `weed mini` sobe em um único processo o Master, Volume Server, Filer, S3 (porta `8333`), WebDAV, Iceberg REST Catalog e Admin UI, auto-ajustado para operação em nó único ou desenvolvimento.

## Como verificar
Suba `weed mini` e execute `aws --endpoint-url http://localhost:8333 s3 cp README.md s3://my-bucket/` para validar o caminho completo de escrita e leitura.

## Conexões
- [[seaweedfs-replicacao-rack-datacenter-aware-placement-001-011-100]] — Veja também: SeaweedFS: política de replicação ciente de topologia (`ReplicaPlacement` de 3 dígitos XYZ por Data Center, Rack e Nó).

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
