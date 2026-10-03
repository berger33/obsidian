---
id: software.devops.tranche17.001697
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

# Canonical MicroK8s: customização de flags de serviços (`kube-apiserver`, `kubelet`, `containerd`) em `/var/snap/microk8s/current/args/`

## Em uma frase
No MicroK8s, cada serviço supervisionado (`kube-apiserver`, `kubelet`, `kube-controller-manager`, `kube-scheduler`, `kube-proxy`, `containerd`, `dqlite`) lê seus argumentos de inicialização a partir de um arquivo de texto correspondente em `/var/snap/microk8s/current/args/`.

## Por que importa
Como o pacote Snap em `/snap/microk8s/current/` é um sistema de arquivos SquashFS somente leitura, toda customização de flags do plano de controle, parâmetros de OIDC, Feature Gates ou configuração do `containerd` deve residir na área gravável `/var/snap/microk8s/current/`.

## Como funciona
Para adicionar uma flag (por exemplo `--oidc-issuer-url` no `kube-apiserver` ou `--max-pods=150` no `kubelet`), o administrador edita `/var/snap/microk8s/current/args/kube-apiserver` (ou `args/kubelet`) e reinicia o MicroK8s (`microk8s stop && microk8s start`). As configurações personalizadas em `/var/snap/microk8s/current/args/` e `certs/` são preservadas durante atualizações de patch via `snap refresh`.

## Exemplo
```bash
ls -la /var/snap/microk8s/current/args/
grep -E "^--" /var/snap/microk8s/current/args/kube-apiserver | head -n 10
```

## Limites e trade-offs
Para configurar espelhos ou registries privados no `containerd` do MicroK8s, edite os arquivos por domínio dentro de `/var/snap/microk8s/current/args/certs.d/<registry>/hosts.toml` em vez do arquivo legado `containerd-template.toml`.

## Como verificar
Inspecione `/var/snap/microk8s/current/args/kubelet` e verifique os argumentos efetivos do processo em execução com `ps -ef | grep kubelet`.

## Conexões
- [[microk8s-canais-snap-tracks-atualizacoes-transacionais-refresh-hold]] — Veja também: Canonical MicroK8s: governança de versões via canais Snap (`--channel=1.xx/stable`) e controle de updates.
- [[microk8s-containerd-interno-microk8s-ctr-images-import-registry]] — Veja também: Canonical MicroK8s: gerenciamento de imagens no `containerd` isolado (`microk8s ctr` e `microk8s images`).

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://canonical.com/microk8s/docs/high-availability) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
