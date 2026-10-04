---
id: software.devops.tranche17.001693
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

# Canonical MicroK8s: formação de cluster (`add-node` / `join`) e remoção segura de nós (`leave` / `remove-node`)

## Em uma frase
O MicroK8s gerencia a adição e remoção de nós no cluster por meio dos comandos `microk8s add-node`, `microk8s join`, `microk8s leave` e `microk8s remove-node` (incluindo o modo `--worker` apenas para planos de dados).

## Por que importa
Adicionar ou descomissionar máquinas de um cluster com datastore distribuído (`dqlite`) exige sincronizar certificados e reconfigurar o quórum de votantes para não quebrar o consenso.

## Como funciona
No nó inicial, `microk8s add-node` gera um token único de uso imediato (`microk8s join <ip>:25000/<token>`). Executar esse comando no segundo e terceiro nós forma o cluster HA automaticamente (ou adiciona um worker puro se `--worker` for passado no `join`). Para remover um nó graciosamente, executa-se primeiro `microk8s leave` no nó que está saindo e depois `microk8s remove-node <node>` em um nó remanescente (ou `microk8s remove-node <node> --force` se o nó tiver sofrido falha permanente).

## Exemplo
```bash
# No nó existente:
microk8s add-node

# No novo nó ingressante:
microk8s join 10.128.63.86:25000/567a21bdfc9a64738ef4b3286b2b8a69
```

## Limites e trade-offs
Ao remover um nó de um cluster existente ou atualizar um cluster antigo pré-1.19 para HA, sempre execute `microk8s kubectl drain <node> --ignore-daemonsets` antes de rodar `microk8s leave` no nó.

## Como verificar
Após adicionar o terceiro nó com `microk8s join`, verifique `microk8s kubectl get nodes` e `microk8s status` para confirmar a ativação automática do HA.

## Conexões
- [[microk8s-alta-disponibilidade-automatica-dqlite-voters-standby-spare]] — Veja também: Canonical MicroK8s: alta disponibilidade (HA) automática com `dqlite` e papéis `voter`, `standby` e `spare`.
- [[microk8s-failure-domains-ha-conf-distribuicao-voters-dqlite]] — Veja também: Canonical MicroK8s: configuração de domínios de falha (`failure-domain` em `ha-conf`) para eleições do `dqlite`.

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://canonical.com/microk8s/docs/high-availability) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
