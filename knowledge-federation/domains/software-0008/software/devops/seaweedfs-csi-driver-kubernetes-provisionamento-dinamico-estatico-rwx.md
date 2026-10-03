---
id: software.devops.tranche18.001728
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
fontes: ["https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md", "https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md", "https://github.com/seaweedfs/seaweedfs-csi-driver"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SeaweedFS CSI Driver: provisionamento dinâmico e estático de volumes `ReadWriteMany` no Kubernetes

## Em uma frase
O `seaweedfs-csi-driver` permite que clusters Kubernetes provisionem volumes `ReadWriteMany` (`RWX`) e `ReadWriteOnce` (`RWO`) dinâmicos ou estáticos respaldados por um cluster SeaweedFS, isolando cada volume dinâmico em sua própria pasta (`/buckets/<volume-id>`) e `collection`.

## Por que importa
Múltiplos Pods de um Deployment web ou pipeline de processamento distribuído precisam ler e gravar simultaneamente na mesma árvore de arquivos POSIX com opções customizadas de replicação e tipo de disco (`ssd` vs `hdd`).

## Como funciona
Instalado via Helm (`seaweedfs-csi-driver` apontando para um ou múltiplos endereços em `seaweedfsFiler`), o driver expõe uma `StorageClass` onde o operador pode customizar `collection`, `replication` (ex.: `"011"`) e `diskType` (ex.: `"ssd"`), ou criar um `PersistentVolume` estático apontando para um `path` específico compartilhado entre diferentes PVCs.

## Exemplo
```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: seaweedfs-ssd-ha
provisioner: seaweedfs-csi-driver
parameters:
  replication: "011"
  diskType: "ssd"
```

## Limites e trade-offs
Se o `kubelet` dos nós do cluster usar um diretório raiz customizado (`--root-dir` diferente do padrão `/var/lib/kubelet`), o caminho no manifesto do DaemonSet do `seaweedfs-csi-driver` deve ser ajustado para corresponder ao `--root-dir` real do `kubelet`.

## Como verificar
Aplique um PVC com a `StorageClass` `seaweedfs-storage`, monte-o em um Pod e execute `kubectl exec <pod> -- df -h` para confirmar o ponto de montagem FUSE.

## Conexões
- [[seaweedfs-cloud-drive-cache-remoto-writeback-replicacao-ativo-ativo]] — Veja também: SeaweedFS `Cloud Drive` e Replicação Ativo-Ativo: cache local acelerado de buckets de nuvem e sincronização multi-cluster.
- [[seaweedfs-csi-driver-cotas-capacidade-collection-enospc-safe-rollout]] — Veja também: SeaweedFS CSI Driver: aplicação de cotas de capacidade (`ENOSPC`) por `collection` e procedimento de *Safe Rollout*.

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs-csi-driver) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
