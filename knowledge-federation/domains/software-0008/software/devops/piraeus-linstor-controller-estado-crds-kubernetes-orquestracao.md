---
id: software.devops.tranche18.001733
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

# Piraeus `linstor-controller`: gerenciamento central de posicionamento de volumes persistido em objetos Kubernetes

## Em uma frase
O `linstor-controller` é o cérebro de controle do Piraeus Datastore: ele calcula o posicionamento de recursos (*resource placement*), configura réplicas DRBD e orquestra operações globais do cluster armazenando todo o seu banco de dados de configuração diretamente como objetos Custom Resource do Kubernetes.

## Por que importa
Na arquitetura legada de LINSTOR fora do Kubernetes, o controlador dependia de um banco SQL externo ou `etcd` separado para guardar o estado dos volumes; no Piraeus v2, usar a própria API do Kubernetes (CRDs) elimina a necessidade de manter outro banco de dados para o controlador.

## Como funciona
O `linstor-controller` mantém conexões ativas com todos os Pods `linstor-satellite` nos worker nodes, enviando instruções de criação/deleção de volumes e expondo a API REST consumida pelo `linstor-csi-controller` e pelo `piraeus-operator`.

## Exemplo
```bash
kubectl exec -n piraeus-datastore deploy/linstor-controller -- linstor node list
kubectl exec -n piraeus-datastore deploy/linstor-controller -- linstor storage-pool list
```

## Limites e trade-offs
Como o `linstor-controller` opera apenas no plano de controle (fora do caminho de dados I/O), se o Pod do `linstor-controller` reiniciar, os volumes DRBD já montados nos nós continuam lendo, gravando e replicando blocos normalmente sem qualquer interrupção.

## Como verificar
Execute `linstor node list` e `linstor resource list` dentro do `deploy/linstor-controller` para inspecionar o estado de todos os nós e volumes.

## Conexões
- [[piraeus-operator-linstorcluster-gencert-tls-sem-cert-manager]] — Veja também: Piraeus Operator e `piraeus-operator-gencert`: reconciliação do `LinstorCluster` e rotação autônoma de certificados TLS.
- [[piraeus-linstor-satellite-daemonset-por-no-uts-network-namespaces]] — Veja também: Piraeus `linstor-satellite`: arquitetura de um DaemonSet por nó e isolamento de namespaces Linux (`UTS` e `Network`).

## Fontes
- [Piraeus Operator v2 GitHub — README.md (Managing LINSTOR, DRBD, CSI Driver & High-Availability Controller in Kubernetes)](https://piraeus.io/docs/stable/explanation/components/) — README oficial do piraeusdatastore/piraeus-operator v2 demonstrando deploy server-side e provisionamento declarativo via LinstorCluster; consultado em 2026-10-03.
- [Piraeus Datastore Official Documentation — Understanding Components (Operator, gencert, Controller, Satellite, CSI, NFS Reactor, Affinity & HA Controller)](https://raw.githubusercontent.com/piraeusdatastore/piraeus-operator/v2/README.md) — Documentação oficial de arquitetura dos 9 componentes do Piraeus Datastore, incluindo namespaces UTS/Network dos Satellites, DRBD Reactor RWX e HA failover; consultado em 2026-10-03.
- [Piraeus Operator — Official GitHub Repository](https://github.com/piraeusdatastore/piraeus-operator) — Repositório oficial Apache-2.0 do Piraeus Operator na CNCF; consultado em 2026-10-03.
