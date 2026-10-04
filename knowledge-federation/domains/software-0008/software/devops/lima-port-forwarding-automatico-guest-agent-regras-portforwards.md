---
id: software.devops.tranche15.001435
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

# Lima: encaminhamento automático de portas (`portForwards`) entre a VM Linux e o localhost da máquina host

## Em uma frase
O agente convidado do Lima (`lima-guestagent`) monitora continuamente sockets TCP/UDP abertos dentro da VM (e nos containers nela executados) e cria túneis automáticos no `127.0.0.1` do host.

## Por que importa
Permite que o desenvolvedor inicie um servidor web ou container na porta `8080` dentro da VM Linux e acesse imediatamente `http://localhost:8080` no navegador do macOS sem configurar regras manuais de NAT a cada execução.

## Como funciona
A seção `portForwards` do arquivo de configuração da instância permite customizar o comportamento: encaminhar portas específicas para sockets Unix no host (como o `docker.sock`), ignorar faixas de portas internas (`ignore: true`), ou mapear `guestPortRange` para `hostPortRange` distintos quando há conflito com serviços locais do host.

## Exemplo
```yaml
portForwards:
  - guestSocket: "/var/run/docker.sock"
    hostSocket: "{{.Dir}}/sock/docker.sock"
  - guestPort: 8080
    hostPort: 18080
```

## Limites e trade-offs
Por padrão, portas vinculadas ao endereço de loopback no host (`127.0.0.1`) não ficam expostas para outras máquinas da rede local; caso seja necessário expor a porta externamente, deve-se configurar `hostIP: "0.0.0.0"` explicitamente na regra.

## Como verificar
Inicie um servidor HTTP de teste dentro da VM (`lima python3 -m http.server 8000`) e verifique no host com `curl -I http://127.0.0.1:8000`.

## Conexões
- [[lima-filesystem-mounts-virtiofs-reverse-sshfs-9p-writable]] — Veja também: Lima: montagem de sistemas de arquivos (`virtiofs`, `reverse-sshfs`, `9p`) e controle de escrita em diretórios do host.
- [[lima-multi-arch-emulacao-intel-on-arm-arm-on-intel-binfmt]] — Veja também: Lima: execução multi-arquitetura (Intel-on-ARM, ARM-on-Intel) e emulação transparente via QEMU/binfmt.

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://lima-vm.io/docs/config/) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
