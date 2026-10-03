---
id: software.devops.tranche17.001696
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

# Canonical MicroK8s: governança de versões via canais Snap (`--channel=1.xx/stable`) e controle de updates

## Em uma frase
O MicroK8s utiliza o sistema de *tracks* e *channels* da Snap Store (`1.30/stable`, `1.31/stable`, `latest/beta`, `latest/edge`) para permitir tanto acompanhar releases do Kubernetes no mesmo dia do lançamento upstream quanto fixar o cluster em uma série minor específica.

## Por que importa
Em ambientes de borda ou produção, atualizações automáticas silenciosas que saltem para uma nova versão minor do Kubernetes sem janela de manutenção podem quebrar APIs depreciadas; por outro lado, patches de segurança da mesma série minor precisam ser aplicados rapidamente.

## Como funciona
Ao instalar com `snap install microk8s --classic --channel=1.31/stable`, o pacote recebe apenas atualizações de patch (`1.31.x`) dentro da track `1.31`, nunca pulando para `1.32` até que o administrador execute explicitamente `snap refresh microk8s --channel=1.32/stable`. Além disso, `snap refresh --hold microk8s` permite congelar atualizações automáticas até a janela de manutenção.

## Exemplo
```bash
sudo snap refresh --hold=forever microk8s
sudo snap refresh microk8s --channel=1.31/stable
sudo snap info microk8s
```

## Limites e trade-offs
Ao atualizar a track minor de um cluster MicroK8s multi-nó via `snap refresh`, atualize todos os nós do cluster para o mesmo canal para evitar desvio de versão entre os processos do plano de controle.

## Como verificar
Execute `snap info microk8s` para verificar o canal seguido (`tracking`), a versão instalada e o status de retenção de refresh.

## Conexões
- [[microk8s-sistema-addons-enable-disable-dns-dashboard-storage-gpu]] — Veja também: Canonical MicroK8s: arquitetura de add-ons curados (`microk8s enable` / `disable`) em `${SNAP}/actions/`.
- [[microk8s-customizacao-argumentos-servicos-var-snap-current-args]] — Veja também: Canonical MicroK8s: customização de flags de serviços (`kube-apiserver`, `kubelet`, `containerd`) em `/var/snap/microk8s/current/args/`.

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://canonical.com/microk8s/docs/high-availability) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
