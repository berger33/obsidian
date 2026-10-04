---
id: software.devops.tranche17.001691
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

# Canonical MicroK8s: distribuição Kubernetes certificada em pacote único Snap para estações, CI/CD, IoT e borda

## Em uma frase
O Canonical MicroK8s é uma distribuição Kubernetes leve, 100% conformante e certificada pela CNCF, empacotada como um único pacote `snap` imutável que funciona em mais de 42 distribuições Linux (bem como em macOS e Windows via Multipass).

## Por que importa
Instalar todas as dependências de um cluster Kubernetes em laptops de desenvolvedores, appliances IoT ou runners de CI sem poluir bibliotecas do sistema operacional host exige um formato de pacote autossuficiente com atualizações transacionais.

## Como funciona
Instalado com `sudo snap install microk8s --classic`, o pacote traz todas as baterias incluídas (`containerd`, `kubelet`, `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, `dqlite`, `calico` e utilitários como `microk8s kubectl` e `microk8s ctr`). O grupo de sistema `microk8s` permite delegar acesso administrativo sem `sudo` aos desenvolvedores.

## Exemplo
```bash
sudo snap install microk8s --classic --channel=1.31/stable
sudo usermod -a -G microk8s "$USER"
microk8s status --wait-ready
microk8s kubectl get nodes
```

## Limites e trade-offs
Para usar um binário `kubectl` externo já instalado na estação com o cluster MicroK8s, basta exportar a configuração gerada por `microk8s config > ~/.kube/config` (ou `microk8s kubectl config view --raw > ~/.kube/config`).

## Como verificar
Execute `microk8s status --wait-ready` e `microk8s kubectl get nodes -o wide` para confirmar que o nó local subiu em estado `Ready`.

## Conexões
- [[microk8s-alta-disponibilidade-automatica-dqlite-voters-standby-spare]] — Veja também: Canonical MicroK8s: alta disponibilidade (HA) automática com `dqlite` e papéis `voter`, `standby` e `spare`.

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://canonical.com/microk8s/docs/high-availability) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
