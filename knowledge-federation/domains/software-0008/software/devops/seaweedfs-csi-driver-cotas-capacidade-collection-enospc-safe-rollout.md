---
id: software.devops.tranche18.001729
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

# SeaweedFS CSI Driver: aplicação de cotas de capacidade (`ENOSPC`) por `collection` e procedimento de *Safe Rollout*

## Em uma frase
Nos volumes provisionados pelo `seaweedfs-csi-driver`, o limite solicitado em `resources.requests.storage` (e eventuais expansões de PVC) é imposto como cota pelo processo FUSE da montagem CSI sobre a `collection` do SeaweedFS, retornando `ENOSPC` quando a capacidade é atingida.

## Por que importa
Sem imposição de cota no ponto de montagem FUSE de um sistema de arquivos compartilhado, um único Pod descontrolado gravando logs infinitos esgotaria todos os Volume Servers do cluster SeaweedFS.

## Como funciona
Por padrão, cada volume dinâmico recebe uma `collection` exclusiva (`<volume-id>`), garantindo que sua cota seja isolada e reportada fielmente no comando `df`. Além disso, como atualizar o DaemonSet do CSI interromperia processos FUSE ativos no nó, a documentação oficial recomenda `node.updateStrategy.type: OnDelete` para atualização segura (*Safe Rollout*) drenando os Pods consumidores nó a nó.

## Exemplo
```bash
#Instalando o CSI driver com múltiplos Filers para alta disponibilidade:
helm install seaweedfs-csi-driver ./deploy/helm/seaweedfs-csi-driver/ \
  --namespace seaweedfs-csi-driver \
  --set seaweedfsFiler="filer-0:8888\,filer-1:8888\,filer-2:8888"
```

## Limites e trade-offs
Se múltiplos volumes forem configurados manualmente na `StorageClass` para compartilhar o mesmo nome de `collection`, o uso de armazenamento será somado e compartilhado entre eles em vez de terem cotas individuais por diretório.

## Como verificar
Verifique dentro do Pod consumidor com `df -h` se o tamanho total reportado pelo ponto de montagem coincide exatamente com `resources.requests.storage` do PVC.

## Conexões
- [[seaweedfs-csi-driver-kubernetes-provisionamento-dinamico-estatico-rwx]] — Veja também: SeaweedFS CSI Driver: provisionamento dinâmico e estático de volumes `ReadWriteMany` no Kubernetes.
- [[seaweedfs-seguranca-aes256-gcm-jwt-volume-access-tls-fips]] — Veja também: SeaweedFS: segurança em repouso e trânsito com criptografia AES-256-GCM no Filer, mTLS, JWT Volume Access e builds FIPS.

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs-csi-driver) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
