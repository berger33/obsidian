---
id: software.devops.tranche15.001439
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

# Lima: modo `plain`, variáveis de ambiente (`env`), política de `sudo` e endurecimento de acesso SSH

## Em uma frase
O Lima oferece controles de isolamento como o `plain mode` (`plain: true`), injeção controlada de variáveis de ambiente (`env`) e restrição de privilégios `sudo` dentro da máquina virtual.

## Por que importa
Para servidores de build ou ambientes de teste que simulam servidores Linux reais na nuvem, desativar as automações opinativas de desktop (como montagens automáticas de home, port-forwarding dinâmico e containerd pré-instalado) reproduz uma VM limpa padrão.

## Como funciona
Quando `plain: true` (ou `limactl start --plain`) é ativado, o Lima desabilita montagens automáticas, port forwarding automático, instalação embutida do containerd/nerdctl e o agente convidado, operando como uma VM pura acessível via SSH em `127.0.0.1`.

## Exemplo
```bash
limactl start --name=clean-vm --plain template:ubuntu-lts
limactl shell clean-vm uname -a
```

## Limites e trade-offs
No modo `plain`, como o `lima-guestagent` não é iniciado, portas abertas dentro da VM não serão encaminhadas automaticamente para o localhost do host a menos que regras estáticas de SSH sejam definidas.

## Como verificar
Inspecione a configuração efetiva da instância em `~/.lima/<nome>/lima.yaml` e teste o acesso SSH isolado com `limactl shell <nome>`.

## Conexões
- [[lima-disks-adicionais-provision-scripts-probes-cloud-init]] — Veja também: Lima: discos extras (`disks`), scripts de provisionamento (`provision`) e verificações de prontidão (`probes`).
- [[lima-sbom-cyclonedx-app-vs-mod-seguranca-supply-chain]] — Veja também: Lima: geração de SBOM CycloneDX em duas visões (`app` vs `mod`) para auditoria de cadeia de suprimentos.

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://lima-vm.io/docs/config/) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
