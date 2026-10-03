---
id: software.devops.tranche15.001437
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

# Lima: modos de rede (`user-v2`, `socket_vmnet`, `vzNAT`) e comunicação direta entre múltiplas VMs

## Em uma frase
O subsistema `networks` do Lima permite escolher entre rede em espaço de usuário sem privilégios (`user-v2`), NAT nativo do Virtualization.framework (`vzNAT`) e redes compartilhadas ou em bridge via `socket_vmnet`.

## Por que importa
Quando o desenvolvedor cria um laboratório multi-nó (por exemplo, várias VMs Lima formando um cluster Kubernetes ou Nomad), as VMs precisam enxergar os endereços IP umas das outras e, opcionalmente, ser acessíveis diretamente a partir do host.

## Como funciona
O modo `user-v2` permite que múltiplas instâncias Lima comuniquem-se entre si em uma rede virtual puramente em user-space sem exigir `sudo` no host. Já o `socket_vmnet` (nas variantes `shared` ou `bridged`) atribui um endereço IP roteável à VM diretamente acessível a partir do macOS e, no modo `bridged`, na LAN física.

## Exemplo
```yaml
networks:
  - lima: user-v2
```

## Limites e trade-offs
O uso de `socket_vmnet` exige que o binário `socket_vmnet` esteja instalado em caminho seguro pertencente ao `root` e gerenciado como daemon privilegiado via `sudoers` no macOS.

## Como verificar
Dentro da VM, execute `lima ip addr` para inspecionar as interfaces de rede provisionadas (como `eth0` e `lima0`).

## Conexões
- [[lima-multi-arch-emulacao-intel-on-arm-arm-on-intel-binfmt]] — Veja também: Lima: execução multi-arquitetura (Intel-on-ARM, ARM-on-Intel) e emulação transparente via QEMU/binfmt.
- [[lima-disks-adicionais-provision-scripts-probes-cloud-init]] — Veja também: Lima: discos extras (`disks`), scripts de provisionamento (`provision`) e verificações de prontidão (`probes`).

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://lima-vm.io/docs/config/) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
