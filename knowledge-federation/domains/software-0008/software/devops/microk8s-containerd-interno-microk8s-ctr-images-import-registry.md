---
id: software.devops.tranche17.001698
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

# Canonical MicroK8s: gerenciamento de imagens no `containerd` isolado (`microk8s ctr` e `microk8s images`)

## Em uma frase
O MicroK8s executa seu próprio daemon `containerd` isolado (escutando em `/var/snap/microk8s/common/run/containerd.sock`), separado de qualquer instalação do Docker ou `containerd` do sistema operacional host, expondo os comandos `microk8s ctr` e `microk8s images` para importar, exportar e inspecionar imagens.

## Por que importa
Um erro muito comum ao usar o MicroK8s localmente é construir uma imagem com `docker build -t minha-app:local .` no Docker do host e tentar referenciá-la em um Pod do MicroK8s: o `kubelet` do MicroK8s falhará com `ErrImagePull` porque o `containerd` interno do MicroK8s não compartilha o image store do Docker.

## Como funciona
Para disponibilizar uma imagem construída localmente sem subir para um registry externo, o desenvolvedor exporta e importa a imagem diretamente com `docker save minha-app:local | microk8s images import -` (ou `microk8s ctr image import -`), ou habilita o registry local embutido (`microk8s enable registry`, exposto em `localhost:32000`).

## Exemplo
```bash
docker save my-service:dev > my-service.tar
microk8s images import my-service.tar
microk8s images ls | grep my-service
```

## Limites e trade-offs
Em um cluster MicroK8s multi-nó, o comando `microk8s images import my-service.tar` distribui e importa automaticamente o tarball da imagem no `containerd` de todos os nós do cluster.

## Como verificar
Execute `microk8s images ls` (ou `microk8s ctr images ls`) após a importação e confirme que a imagem consta no namespace `k8s.io` do `containerd`.

## Conexões
- [[microk8s-customizacao-argumentos-servicos-var-snap-current-args]] — Veja também: Canonical MicroK8s: customização de flags de serviços (`kube-apiserver`, `kubelet`, `containerd`) em `/var/snap/microk8s/current/args/`.
- [[microk8s-inspect-diagnostico-troubleshooting-pacote-logs]] — Veja também: Canonical MicroK8s: diagnóstico automatizado de saúde e coleta de pacote de suporte com `microk8s inspect`.

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://canonical.com/microk8s/docs/high-availability) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
