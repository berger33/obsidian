---
id: software.devops.tranche17.001699
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

# Canonical MicroK8s: diagnóstico automatizado de saúde e coleta de pacote de suporte com `microk8s inspect`

## Em uma frase
O comando `microk8s inspect` executa uma bateria automatizada de verificações de saúde nos serviços systemd do snap, módulos de kernel, configurações de rede/firewall, certificados e estado do `dqlite`, gerando ao final um tarball completo (`inspection-report-*.tar.gz`) para diagnóstico.

## Por que importa
Quando um nó apresenta falha de CNI, bloqueio por `ufw`/`iptables`, falta de memória ou falha de quórum no `dqlite`, coletar manualmente `journalctl` de uma dezena de daemons do snap (`snap.microk8s.daemon-kubelite`, `daemon-containerd`, `daemon-cluster-agent`) atrasa a resolução do incidente.

## Como funciona
Ao rodar `microk8s inspect`, o script verifica se todos os daemons estão ativos, aponta avisos imediatos no terminal (por exemplo, se o encaminhamento IPv4 estiver desabilitado ou se o firewall estiver bloqueando o tráfego pod-to-pod na interface `cni0`/`vxlan.calico`) e empacota logs, argumentos de `args/` e saídas de `kubectl` em `/var/snap/microk8s/current/inspection-report-*.tar.gz`.

## Exemplo
```bash
sudo microk8s inspect
ls -lh /var/snap/microk8s/current/inspection-report-*.tar.gz
```

## Limites e trade-offs
Como o pacote gerado por `microk8s inspect` contém configurações e logs detalhados dos processos do nó, revise e sanitize dados sensíveis antes de anexar o tarball em tickets públicos.

## Como verificar
Execute `sudo microk8s inspect` e verifique no resumo do terminal que todos os daemons (`daemon-kubelite`, `daemon-containerd`, `daemon-k8s-dqlite`) aparecem como ` is running`.

## Conexões
- [[microk8s-containerd-interno-microk8s-ctr-images-import-registry]] — Veja também: Canonical MicroK8s: gerenciamento de imagens no `containerd` isolado (`microk8s ctr` e `microk8s images`).
- [[microk8s-execucao-multiplataforma-multipass-lxd-incus-ci]] — Veja também: Canonical MicroK8s: execução multiplataforma (macOS/Windows via Multipass) e laboratórios HA em containers LXD/Incus.

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://canonical.com/microk8s/docs/high-availability) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
