---
id: software.devops.tranche15.001432
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

# Lima: catálogo de templates prontos (`template:docker`, `template:k8s`, Podman e múltiplas distribuições Linux)

## Em uma frase
O Lima inclui dezenas de templates oficiais integrados que permitem instanciar ambientes pré-configurados de Docker, Kubernetes (`kubeadm` ou `k3s`), Podman e diversas distribuições Linux (Ubuntu, Debian, Fedora, Alpine, Arch, Rocky, openSUSE) com um único comando.

## Por que importa
Elimina a necessidade de escrever scripts manuais de cloud-init ou provisionamento para subir um daemon Docker isolado ou um cluster Kubernetes completo em macOS ou Linux.

## Como funciona
Ao executar `limactl start template:docker`, o Lima cria uma instância dedicada chamada `docker` e expõe o socket Unix do daemon no diretório da instância no host (`unix://{{.Dir}}/sock/docker.sock`). De modo similar, `limactl start template:k8s` provisiona o cluster e copia automaticamente o `kubeconfig.yaml` da VM para o host.

## Exemplo
```bash
limactl start template:docker
export DOCKER_HOST=$(limactl list docker --format 'unix://{{.Dir}}/sock/docker.sock')
docker ps

limactl start template:k8s
export KUBECONFIG=$(limactl list k8s --format '{{.Dir}}/copied-from-guest/kubeconfig.yaml')
kubectl get nodes
```

## Limites e trade-offs
Cada template iniciado cria uma máquina virtual independente com sua própria alocação de memória e CPU; pausar instâncias ociosas com `limactl stop <nome>` evita esgotar a RAM da estação de trabalho.

## Como verificar
Liste todos os templates disponíveis localmente com `limactl start --list-templates` e verifique os sockets exportados com `limactl list`.

## Conexões
- [[lima-arquitetura-linux-virtual-machines-cncf-incubating]] — Veja também: Lima (Linux Machines): máquinas virtuais Linux na CNCF com compartilhamento automático de arquivos e portas.
- [[lima-vm-types-vz-virtualization-framework-vs-qemu-rosetta]] — Veja também: Lima: backends de virtualização (`vz` Virtualization.framework vs `qemu`) e aceleração Rosetta 2 em Apple Silicon.

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://lima-vm.io/docs/config/) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
