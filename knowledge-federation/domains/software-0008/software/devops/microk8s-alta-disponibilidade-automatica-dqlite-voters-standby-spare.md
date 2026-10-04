---
id: software.devops.tranche17.001692
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://canonical.com/microk8s/docs/high-availability", "https://raw.githubusercontent.com/canonical/microk8s/master/README.md", "https://github.com/canonical/microk8s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Canonical MicroK8s: alta disponibilidade (HA) automática com `dqlite` e papéis `voter`, `standby` e `spare`

## Em uma frase
A partir de clusters com três ou mais nós, o MicroK8s habilita automaticamente a Alta Disponibilidade (HA) executando o plano de controle em todos os nós sobre o banco de dados distribuído embarcado **dqlite** (*distributed SQLite* baseado em Raft em C).

## Por que importa
Manter um cluster `etcd` tradicional separado em pequenos clusters de borda de 3 a 5 nós exige configuração manual de quórum e consome mais memória RAM e I/O de disco do que o `dqlite`.

## Como funciona
No cluster HA do MicroK8s, todos os nós executam o plano de controle master (permitindo rodar `microk8s *` de qualquer nó), enquanto o `dqlite` atribui automaticamente três papéis aos nós: **voters** (no mínimo 3 nós que replicam o banco e votam na eleição de líder), **standby** (nós não votantes que mantêm uma cópia sincronizada do banco prontos para assumir o lugar de um voter em até 30 segundos) e **spare** (nós extras que não replicam nem votam no banco).

## Exemplo
```bash
microk8s status
# Saída esperada em cluster de 3+ nós:
# high-availability: yes
#   datastore master nodes: 10.128.63.86:19001 10.128.63.166:19001 10.128.63.43:19001
#   datastore standby nodes: none
```

## Limites e trade-offs
Conforme documentado pela Canonical, se o nó líder do `dqlite` cair abruptamente, o cluster elege um novo líder em até **5 segundos**; e a promoção automática de um nó `standby` para `voter` leva até **30 segundos**.

## Como verificar
Execute `microk8s status` em um cluster de 3 nós e confirme que `high-availability: yes` exibe ao menos três endereços na porta `19001` em `datastore master nodes`.

## Conexões
- [[microk8s-arquitetura-snap-single-package-canonical-kubernetes]] — Veja também: Canonical MicroK8s: distribuição Kubernetes certificada em pacote único Snap para estações, CI/CD, IoT e borda.
- [[microk8s-clustering-add-node-join-leave-remove-node-force]] — Veja também: Canonical MicroK8s: formação de cluster (`add-node` / `join`) e remoção segura de nós (`leave` / `remove-node`).

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://canonical.com/microk8s/docs/high-availability) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
