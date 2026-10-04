---
id: software.devops.tranche18.001731
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
fontes: ["https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md", "https://piraeus.io/docs/stable/explanation/components/", "https://github.com/piraeusdatastore/piraeus-operator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Piraeus Datastore: armazenamento em bloco replicado cloud-native no Kubernetes com LINSTOR e DRBD

## Em uma frase
O Piraeus Datastore (projeto CNCF Sandbox licenciado sob Apache 2.0) gerencia clusters de armazenamento de alta performance no Kubernetes integrando a pilha completa **LINSTOR**, **DRBD** (replicação de bloco no kernel Linux), **LINSTOR CSI Driver** e **High-Availability Controller** por meio do **Piraeus Operator v2**.

## Por que importa
Sistemas de armazenamento definidos por software que processam I/O inteiramente em user-space sofrem penalidades de latência e CPU; o Piraeus utiliza o módulo de kernel DRBD9 para replicação síncrona ou assíncrona em nível de bloco com overhead mínimo e orquestração declarativa via CRDs Kubernetes.

## Como funciona
Instalado com `kubectl apply --server-side` no namespace `piraeus-datastore`, o Piraeus Operator reconcilia o CRD `LinstorCluster` e implanta automaticamente nove componentes coordenados: `piraeus-operator`, `piraeus-operator-gencert`, `linstor-controller`, `linstor-satellite`, `linstor-csi-controller`, `linstor-csi-node`, `linstor-csi-nfs-server`, `linstor-affinity-controller` e `ha-controller`.

## Exemplo
```bash
kubectl apply --server-side -f "https://github.com/piraeusdatastore/piraeus-operator/releases/latest/download/manifest.yaml"
kubectl wait pod --for=condition=Ready -n piraeus-datastore -l app.kubernetes.io/component=piraeus-operator
```

## Limites e trade-offs
Se você ainda estiver executando o Piraeus Operator legado v1, a documentação oficial recomenda manter a v1 até concluir o procedimento planejado de migração para o Piraeus Operator v2.

## Como verificar
Execute `kubectl get pods -n piraeus-datastore -o custom-columns=NAME:.metadata.name,COMPONENT:.metadata.labels.app\.kubernetes\.io/component` para verificar todos os componentes.

## Conexões
- [[piraeus-operator-linstorcluster-gencert-tls-sem-cert-manager]] — Veja também: Piraeus Operator e `piraeus-operator-gencert`: reconciliação do `LinstorCluster` e rotação autônoma de certificados TLS.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://piraeus.io/docs/stable/explanation/components/) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
