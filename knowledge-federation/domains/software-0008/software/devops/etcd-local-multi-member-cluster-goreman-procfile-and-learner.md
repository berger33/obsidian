---
id: software.devops.tranche03.000295
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
fontes: ["https://raw.githubusercontent.com/etcd-io/etcd/main/README.md", "https://github.com/etcd-io/etcd"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cluster local de 3 membros (infra1, infra2, infra3), grpc-proxy e nó learner com goreman e Procfile

## Em uma frase
A subseção `Running a local etcd cluster` do README mostra como subir um cluster local de exemplo usando o gerenciador `goreman` (`github.com/mattn/goreman`) e o arquivo `./Procfile` do repositório: o comando `goreman start` inicia 3 membros do etcd (`infra1`, `infra2` e `infra3`) e opcionalmente o `grpc-proxy` do etcd, nos quais cada membro e proxy aceita leituras e escritas de chave-valor, orientando ainda seguir os comentários no `./Procfile` para adicionar um nó **learner** (`learner node`) ao cluster.

## Por que importa
O conceito de `learner node` mencionado no `Procfile` é fundamental para operações seguras em produção: um nó learner recebe o fluxo de replicação do log do líder até alcançar o estado atual sem participar ainda da contagem de quórum de votação Raft, evitando que a adição de um novo membro lento derrube o quórum do cluster.

## Como funciona
Utilize `goreman start` com o `./Procfile` oficial para simular localmente um cluster de 3 membros (`infra1`, `infra2`, `infra3`), testar o `grpc-proxy` e praticar a adição e promoção de um nó `learner` antes de executar manutenções em produção.

## Exemplo
Em um laboratório local, o engenheiro inicia os 3 membros com `goreman start` e segue o `Procfile` para adicionar um nó `learner` e observar a sincronização do log antes de promovê-lo a membro votante.

## Limites e trade-offs
Ao substituir ou adicionar membros em um cluster etcd de produção, adicione o novo nó primeiro como `learner` e aguarde a sincronização antes de promovê-lo, especialmente se o banco de dados for grande.

## Como verificar
Conferi a subseção Running a local etcd cluster no README oficial de etcd-io/etcd.

## Conexões
- [[etcd-official-iana-tcp-ports-2379-and-2380]] — Veja também: Portas TCP oficiais registradas na IANA: 2379 para clientes e 2380 para comunicação entre pares.
- [[etcd-operational-guides-clustering-security-and-tuning]] — Veja também: Guias operacionais essenciais: clustering multi-máquina, configuração, segurança TLS e tuning.

## Fontes
- [etcd — GitHub README](https://raw.githubusercontent.com/etcd-io/etcd/main/README.md) — Visão geral do etcd (banco chave-valor distribuído via consenso Raft, pilares Simple/Secure/Fast/Reliable, testes de robustez, 7 pacotes Go v3, portas IANA 2379/2380, cluster local via goreman/Procfile com learner node e reuniões).; consultado em 2026-10-03.
- [etcd — Repositório Oficial no GitHub](https://github.com/etcd-io/etcd) — Repositório oficial do etcd na CNCF com código-fonte Go, etcdctl/, tests/robustness/, Procfile, OWNERS e ADOPTERS.md.; consultado em 2026-10-03.
