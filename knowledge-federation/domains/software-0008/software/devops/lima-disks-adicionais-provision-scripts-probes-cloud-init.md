---
id: software.devops.tranche15.001438
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
fontes: ["https://lima-vm.io/docs/config/", "https://raw.githubusercontent.com/lima-vm/lima/master/README.md", "https://github.com/lima-vm/lima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lima: discos extras (`disks`), scripts de provisionamento (`provision`) e verificações de prontidão (`probes`)

## Em uma frase
O arquivo de configuração do Lima permite anexar discos virtuais persistentes extras (`disks`) a várias instâncias ou preservá-los entre recriações de VM, além de automatizar a configuração inicial com blocos `provision` e `probes`.

## Por que importa
Permite separar dados pesados (como cache do `/var/lib/containerd` ou bancos de dados de desenvolvimento) do disco raiz da VM e garantir que `limactl start` só retorne quando todos os daemons internos estiverem prontos.

## Como funciona
O usuário cria discos gerenciados com `limactl disk create <nome> --size 50G`, referencia-os em `disks:` no YAML da instância, define scripts de bootstrap em `provision:` (modos `system`, `user`, `boot` ou `dependency`) e declara scripts de verificação em `probes:` que o Lima aguarda passarem antes de declarar a VM pronta.

## Exemplo
```bash
limactl disk create data-disk --size 20G
limactl disk ls
```

## Limites e trade-offs
Um disco adicional gerenciado pelo Lima fica bloqueado (`locked`) enquanto estiver anexado a uma instância em execução e não deve ser montado simultaneamente em modo de escrita por duas VMs sem um filesystem de cluster.

## Como verificar
Liste os discos virtuais gerenciados e seu status de anexação com `limactl disk ls`.

## Conexões
- [[lima-redes-user-v2-socket-vmnet-bridged-comunicacao-vms]] — Veja também: Lima: modos de rede (`user-v2`, `socket_vmnet`, `vzNAT`) e comunicação direta entre múltiplas VMs.
- [[lima-plain-mode-ssh-sudo-environment-variables-isolamento]] — Veja também: Lima: modo `plain`, variáveis de ambiente (`env`), política de `sudo` e endurecimento de acesso SSH.

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://lima-vm.io/docs/config/) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
