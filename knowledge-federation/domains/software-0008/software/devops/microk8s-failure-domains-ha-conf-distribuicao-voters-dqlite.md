---
id: software.devops.tranche17.001694
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

# Canonical MicroK8s: configuração de domínios de falha (`failure-domain` em `ha-conf`) para eleições do `dqlite`

## Em uma frase
Em clusters MicroK8s distribuídos entre múltiplos racks ou zonas de disponibilidade, o arquivo `/var/snap/microk8s/current/args/ha-conf` permite associar cada nó a um identificador inteiro de domínio de falha (`failure-domain=<int>`).

## Por que importa
Se um cluster de 6 nós estiver dividido entre 2 racks (3 servidores no Rack 1 e 3 servidores no Rack 2) sem consciência de topologia, o `dqlite` poderia escolher todos os 3 nós `voters` dentro do Rack 1; se o switch do Rack 1 desligasse, o cluster inteiro perderia o quórum.

## Como funciona
Ao gravar `failure-domain=1` nos nós do Rack 1, `failure-domain=2` no Rack 2 e `failure-domain=3` no Rack 3 em `/var/snap/microk8s/current/args/ha-conf` (seguido de `microk8s stop && microk8s start`), o motor do `dqlite` espalha automaticamente os nós `voters` e `standby` entre domínios de falha distintos.

## Exemplo
```bash
echo "failure-domain=42" | sudo tee /var/snap/microk8s/current/args/ha-conf
sudo microk8s stop
sudo microk8s start
sudo microk8s status
```

## Limites e trade-offs
Qualquer alteração no arquivo `/var/snap/microk8s/current/args/ha-conf` exige reiniciar os serviços do MicroK8s naquele nó (`microk8s stop` seguido de `microk8s start`) para que o daemon do `dqlite` recarregue sua topologia.

## Como verificar
Verifique o conteúdo de `/var/snap/microk8s/current/args/ha-conf` em cada nó e confirme em `microk8s status` a distribuição equilibrada dos `datastore master nodes`.

## Conexões
- [[microk8s-clustering-add-node-join-leave-remove-node-force]] — Veja também: Canonical MicroK8s: formação de cluster (`add-node` / `join`) e remoção segura de nós (`leave` / `remove-node`).
- [[microk8s-sistema-addons-enable-disable-dns-dashboard-storage-gpu]] — Veja também: Canonical MicroK8s: arquitetura de add-ons curados (`microk8s enable` / `disable`) em `${SNAP}/actions/`.

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://canonical.com/microk8s/docs/high-availability) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
