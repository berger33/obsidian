---
id: software.devops.tranche17.001695
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
fontes: ["https://raw.githubusercontent.com/canonical/microk8s/master/README.md", "https://canonical.com/microk8s/docs/high-availability", "https://github.com/canonical/microk8s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Canonical MicroK8s: arquitetura de add-ons curados (`microk8s enable` / `disable`) em `${SNAP}/actions/`

## Em uma frase
O MicroK8s instala por padrão um Kubernetes upstream enxuto (*barebones*) e inclui uma coleção curada de add-ons ativáveis com um único comando (`microk8s enable <addon>`) — cobrindo `dns`, `dashboard`, `hostpath-storage`, `ingress`, `metallb`, `observability`, `istio`, `knative`, `gpu` e `registry`.

## Por que importa
Em vez de obrigar o desenvolvedor ou engenheiro de borda a procurar URLs de manifestos compatíveis com sua versão exata do Kubernetes para ter CoreDNS, armazenamento local, GPU NVIDIA ou registro OCI, o MicroK8s empacota esses manifestos e scripts validados dentro do próprio snap.

## Como funciona
Os manifestos e scripts de ativação ficam em `${SNAP}/actions/` (apontando para `/snap/microk8s/current/actions/`) e repositórios de add-ons da comunidade/core. Ao executar `microk8s enable dns dashboard`, o MicroK8s aplica os manifestos parametrizados e, quando necessário, ajusta argumentos do `kubelet` ou `containerd`.

## Exemplo
```bash
microk8s status
microk8s enable dns hostpath-storage ingress
microk8s kubectl get pods -A
```

## Limites e trade-offs
Em um cluster HA multi-nó, certos add-ons que baixam binários de cliente para o host (como `microk8s enable helm`) disponibilizam esse binário CLI apenas no nó onde o comando `microk8s enable` foi executado.

## Como verificar
Execute `microk8s status` para listar todos os add-ons `enabled` e `disabled` e confirme a saúde dos Pods criados em `kube-system` e `ingress`.

## Conexões
- [[microk8s-failure-domains-ha-conf-distribuicao-voters-dqlite]] — Veja também: Canonical MicroK8s: configuração de domínios de falha (`failure-domain` em `ha-conf`) para eleições do `dqlite`.
- [[microk8s-canais-snap-tracks-atualizacoes-transacionais-refresh-hold]] — Veja também: Canonical MicroK8s: governança de versões via canais Snap (`--channel=1.xx/stable`) e controle de updates.

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://canonical.com/microk8s/docs/high-availability) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
