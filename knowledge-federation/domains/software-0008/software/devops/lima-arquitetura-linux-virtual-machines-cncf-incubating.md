---
id: software.devops.tranche15.001431
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/lima-vm/lima/master/README.md", "https://lima-vm.io/docs/config/", "https://github.com/lima-vm/lima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lima (Linux Machines): máquinas virtuais Linux na CNCF com compartilhamento automático de arquivos e portas

## Em uma frase
O Lima (projeto CNCF Incubating) provisiona e gerencia máquinas virtuais Linux em macOS, Linux e NetBSD com compartilhamento transparente de sistema de arquivos e encaminhamento automático de portas localhost, de forma análoga ao WSL2.

## Por que importa
Criado originalmente para levar o `containerd` e o `nerdctl` a usuários de macOS, o Lima tornou-se a camada fundacional de virtualização usada por ferramentas como Rancher Desktop, Colima, Finch e Podman Desktop.

## Como funciona
Por meio da CLI `limactl`, o usuário inicia uma VM padrão (`limactl start`, que provisiona Ubuntu com 4 vCPUs, 4 GiB de RAM e 100 GiB de disco) e executa comandos Linux diretamente do terminal do host prefixando-os com `lima` (ex.: `lima uname -a` ou `lima nerdctl run --rm hello-world`).

## Exemplo
```bash
limactl start
lima uname -a
lima nerdctl run --rm hello-world
limactl list
```

## Limites e trade-offs
Na configuração padrão do Lima, o diretório home do usuário (`~`) é montado na VM em modo somente leitura (*read-only*) por segurança, evitando que processos dentro da VM modifiquem acidentalmente arquivos sensíveis do host.

## Como verificar
Execute `limactl list` e `lima df -h` para confirmar que a instância `default` está em estado `Running` com os pontos de montagem ativos.

## Conexões
- [[lima-templates-docker-kubernetes-podman-distros-linux]] — Veja também: Lima: catálogo de templates prontos (`template:docker`, `template:k8s`, Podman e múltiplas distribuições Linux).

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://lima-vm.io/docs/config/) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
