---
id: software.devops.tranche18.001715
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
fontes: ["https://juicefs.com/docs/community/architecture/", "https://raw.githubusercontent.com/juicedata/juicefs/main/README.md", "https://github.com/juicedata/juicefs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# JuiceFS Kubernetes CSI Driver: volumes `ReadWriteMany` compartilhados via Mount Pods ou modo Sidecar

## Em uma frase
O **JuiceFS CSI Driver** permite provisionar e compartilhar volumes `ReadWriteMany` (`RWX`) entre milhares de Pods em um cluster Kubernetes, executando o cliente JuiceFS em **Mount Pods** dedicados por nó (ou como **sidecar** em ambientes serverless como AWS Fargate / Knative).

## Por que importa
Executar o cliente FUSE dentro do processo principal do `csi-node` DaemonSet faria com que qualquer atualização ou reinício do DaemonSet CSI derrubasse todas as montagens FUSE dos Pods de aplicação em execução no nó.

## Como funciona
Por padrão, o JuiceFS CSI Driver gerencia o ciclo de vida de *Mount Pods* independentes no namespace do CSI (compartilhando o mesmo Mount Pod entre vários Pods de aplicação no mesmo nó que montam o mesmo PVC e preservando a montagem durante upgrades do CSI). Opcionalmente, o modo Sidecar injeta o container do cliente JuiceFS diretamente no Pod da aplicação via webhook.

## Exemplo
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: juicefs-sc
provisioner:csi.juicefs.com
parameters:
  csi.storage.k8s.io/provisioner-secret-name: juicefs-secret
  csi.storage.k8s.io/provisioner-secret-namespace: kube-system
  csi.storage.k8s.io/node-publish-secret-name: juicefs-secret
  csi.storage.k8s.io/node-publish-secret-namespace: kube-system
```

## Limites e trade-offs
Na `StorageClass` do JuiceFS CSI (`provisioner: csi.juicefs.com`), garanta um espaço após `provisioner:` no manifesto YAML (`provisioner: csi.juicefs.com`) e armazene as credenciais do Metadata Engine e do Object Storage no `Secret` referenciado.

## Como verificar
Crie um PVC com `accessModes: [ReadWriteMany]` usando a `StorageClass` do JuiceFS e verifique a criação automática do Mount Pod no namespace `kube-system`.

## Conexões
- [[juicefs-escolha-metadata-engine-redis-tikv-postgresql-mysql-sqlite]] — Veja também: JuiceFS: seleção de Metadata Engine (`Redis`, `TiKV`, `PostgreSQL`, `MySQL`, `SQLite`) por escala e durabilidade.
- [[juicefs-cache-multinivel-memoria-disco-ssd-warmup-ai-training]] — Veja também: JuiceFS: aceleração de leitura com cache local de metadados e blocos em SSD/NVMe e `juicefs warmup`.

## Fontes
- [JuiceFS GitHub — README.md (High-Performance POSIX Cloud-Native File System, Object Storage + Metadata Engine Architecture)](https://juicefs.com/docs/community/architecture/) — README oficial do juicedata/juicefs apresentando compatibilidade POSIX/Hadoop/S3, consistência forte, locks globais, criptografia e compressão; consultado em 2026-10-03.
- [JuiceFS Official Documentation — Architecture (JuiceFS Client, Data Storage, Metadata Engine & Chunks/Slices/Blocks Layout)](https://raw.githubusercontent.com/juicedata/juicefs/main/README.md) — Documentação oficial de arquitetura do JuiceFS detalhando Chunks de 64 MiB, Slices append-only, Blocks de 4 MiB, compactação e métodos de acesso; consultado em 2026-10-03.
- [JuiceFS — Official GitHub Repository](https://github.com/juicedata/juicefs) — Repositório oficial Apache-2.0 do JuiceFS; consultado em 2026-10-03.
