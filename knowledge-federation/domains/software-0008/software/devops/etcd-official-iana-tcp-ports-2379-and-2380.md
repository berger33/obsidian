---
id: software.devops.tranche03.000294
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/etcd-io/etcd/main/README.md", "https://etcd.io/docs/latest/op-guide/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Portas TCP oficiais registradas na IANA: 2379 para clientes e 2380 para comunicação entre pares

## Em uma frase
As subseções `Running etcd` e `etcd TCP ports` do README documentam que as portas TCP oficiais do etcd registradas na IANA (`iana.org/assignments/service-names-port-numbers`) são a porta **2379** para requisições de clientes (`client communication / client requests`) e a porta **2380** para comunicação servidor-a-servidor entre membros do cluster (`server-to-server / peer communication`), demonstrando em seguida o uso do cliente de linha de comando `etcdctl put mykey "this is awesome"` e `etcdctl get mykey`.

## Por que importa
Em regras de firewall de nós do plano de controle (control plane nodes) e políticas de rede, confundir a porta de clientes (`2379`, acessada pelo `kube-apiserver` e pelo `etcdctl`) com a porta de consenso Raft entre nós (`2380`, exclusiva entre os membros do etcd) ou deixar ambas abertas para os pods de aplicações compromete totalmente a segurança do cluster.

## Como funciona
Restrinja no firewall e nas NetworkPolicies a porta `2380` estritamente à comunicação mútua entre os nós membros do etcd e a porta `2379` apenas aos clientes autorizados (como o `kube-apiserver`), exigindo mTLS em ambas.

## Exemplo
Ao diagnosticar a saúde de um nó de control plane, o administrador verifica a conectividade entre pares na porta `2380` e testa a leitura autenticada com `etcdctl` na porta `2379`.

## Limites e trade-offs
Nunca exponha a porta `2379` ou `2380` do etcd para a rede geral de pods de usuários nem para a internet pública.

## Como verificar
Conferi as subseções Running etcd e etcd TCP ports no README oficial de etcd-io/etcd.

## Conexões
- [[etcd-v3-go-packages-and-client-library]] — Veja também: Os sete pacotes Go v3 fundamentais do etcd e instalação do cliente go.etcd.io/etcd/client/v3.
- [[etcd-local-multi-member-cluster-goreman-procfile-and-learner]] — Veja também: Cluster local de 3 membros (infra1, infra2, infra3), grpc-proxy e nó learner com goreman e Procfile.

## Fontes
- [etcd — GitHub README](https://raw.githubusercontent.com/etcd-io/etcd/main/README.md) — Visão geral do etcd (banco chave-valor distribuído via consenso Raft, pilares Simple/Secure/Fast/Reliable, testes de robustez, 7 pacotes Go v3, portas IANA 2379/2380, cluster local via goreman/Procfile com learner node e reuniões).; consultado em 2026-10-03.
- [etcd Documentation — Operating etcd & Guides](https://etcd.io/docs/latest/op-guide/) — Guia operacional oficial do etcd cobrindo instalação, clustering, configuração, segurança TLS e tuning.; consultado em 2026-10-03.
