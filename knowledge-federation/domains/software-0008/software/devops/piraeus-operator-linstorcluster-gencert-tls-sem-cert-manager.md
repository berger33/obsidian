---
id: software.devops.tranche18.001732
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
fontes: ["https://piraeus.io/docs/stable/explanation/components/", "https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md", "https://github.com/piraeusdatastore/piraeus-operator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Piraeus Operator e `piraeus-operator-gencert`: reconciliação do `LinstorCluster` e rotação autônoma de certificados TLS

## Em uma frase
O `piraeus-operator` cria e mantém todos os componentes da pilha LINSTOR a partir do recurso `LinstorCluster` (`piraeus.io/v1`), enquanto o Pod auxiliar `piraeus-operator-gencert` gera e renova autonomamente os certificados TLS do webhook de validação sem exigir instalação prévia do `cert-manager`.

## Por que importa
Em versões históricas, instalar o Piraeus exigia instalar e manter o `cert-manager` como pré-requisito obrigatório apenas para emitir o certificado do `ValidatingWebhookConfiguration`, adicionando uma dependência externa ao bootstrap de armazenamento do cluster.

## Como funciona
O componente `piraeus-operator-gencert` cria e mantém a Secret TLS `webhook-server-cert` consumida pelo `piraeus-operator` e atualiza o bundle CA na `ValidatingWebhookConfiguration`. Com o webhook ativo, o `piraeus-operator` registra automaticamente os satélites, cria os *storage pools* (LVM/LVM-Thin/ZFS) e mantém os labels dos nós.

## Exemplo
```yaml
apiVersion: piraeus.io/v1
kind: LinstorCluster
metadata:
  name: linstorcluster
spec: {}
```

## Limites e trade-offs
O `piraeus-operator` gerencia todos os componentes do Piraeus Datastore no namespace `piraeus-datastore`, exceto o próprio `piraeus-operator-gencert` que prepara os certificados antes da partida do operador.

## Como verificar
Aplique o manifesto `LinstorCluster` e verifique com `kubectl get linstorclusters` e `kubectl get secret webhook-server-cert -n piraeus-datastore` o bootstrap completo.

## Conexões
- [[piraeus-datastore-arquitetura-linstor-drbd-kubernetes-cncf-sandbox]] — Veja também: Piraeus Datastore: armazenamento em bloco replicado cloud-native no Kubernetes com LINSTOR e DRBD.
- [[piraeus-linstor-controller-estado-crds-kubernetes-orquestracao]] — Veja também: Piraeus `linstor-controller`: gerenciamento central de posicionamento de volumes persistido em objetos Kubernetes.

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://piraeus.io/docs/stable/explanation/components/) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
