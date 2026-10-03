---
id: software.devops.tranche09.000810
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/siderolabs/talos/main/README.md", "https://docs.siderolabs.com/talos/v1.9/learn-more/architecture", "https://github.com/siderolabs/talos"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Talos Linux: identidade de nó na partição STATE, descoberta de cluster e malha criptografada KubeSpan (WireGuard)

## Em uma frase
O Talos Linux armazena a configuração da máquina, os dados de identidade para descoberta de cluster (`Cluster Discovery`) e as informações do **KubeSpan** (malha de rede ponto a ponto sobre WireGuard integrada ao SO) na partição persistente `STATE`.

## Por que importa
Em clusters Kubernetes híbridos que abrangem máquinas bare-metal em data centers locais e instâncias em nuvens públicas diferentes, conectar os nós entre si geralmente exige configurar VPNs externas complexas e manter listas estáticas de IPs de pares. A documentação de arquitetura do Talos (`File system partitions`) destaca o papel da partição `STATE` para a identidade do nó, descoberta automática de membros e KubeSpan.

## Como funciona
Durante o boot do nó Talos, o `machined` monta a partição **`STATE`** (criptografável por hardware TPM2/LUKS), onde residem: (1) o arquivo de configuração declarativa da máquina (`config.yaml`); (2) a identidade criptográfica do nó para o serviço **Cluster Discovery** (que permite aos nós do mesmo cluster descobrirem automaticamente os endereços IP e endpoints uns dos outros); e (3) as chaves e metadados do **KubeSpan**, que estabelece automaticamente túneis **WireGuard** ponto a ponto (full mesh) no kernel Linux entre todos os nós do cluster, atravessando NAT/firewalls e criptografando todo o tráfego de controle e dados entre os servidores sem exigir configuração manual de peers WireGuard.

## Exemplo
```bash
# Inspecionar os membros descobertos automaticamente no cluster e o status dos peers KubeSpan via talosctl
talosctl -n 10.0.0.10 get members
talosctl -n 10.0.0.10 get kubespanpeerstatuses
```

## Limites e trade-offs
Como a partição `STATE` guarda a configuração da máquina e a identidade criptográfica do nó no cluster, se a partição `STATE` for apagada durante um reset sem preservação, o nó perde sua identidade e configuração locais, voltando ao modo de manutenção inicial e aguardando um novo `talosctl apply-config`.

## Como verificar
Execute `talosctl -n <ip-do-no> get discoveredvolumes` para verificar a presença e o estado da partição `STATE` e `talosctl -n <ip-do-no> get members` para confirmar o registro de descoberta de todos os nós do cluster.

## Conexões
- [[talos-observabilidade-troubleshooting-api-logs-pcap-dashboard]] — Veja também: Talos Linux: diagnóstico e observabilidade sem SSH via talosctl (dashboard, logs, dmesg, pcap e leitura de /proc).
- [[talos-linux-sistema-operacional-imutavel-api-kubernetes]] — Referência cruzada direta com talos-linux-sistema-operacional-imutavel-api-kubernetes.
- [[talos-particoes-disco-camadas-rootfs-squashfs-overlayfs]] — Referência cruzada direta com talos-particoes-disco-camadas-rootfs-squashfs-overlayfs.
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Referência cruzada direta com clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes.

## Fontes
- [Talos Linux Documentation — What is Talos (Immutability, Minimalism, Ephemerality & API-Driven Management)](https://raw.githubusercontent.com/siderolabs/talos/main/README.md) — Visão geral oficial do Talos Linux detalhando ausência de shell/SSH, cerca de 12 binários no sistema de arquivos, partições efêmeras criptografadas com KMS/TPM e recomendações CIS/NIST; consultado em 2026-10-03.
- [Talos Linux Documentation — Architecture & Design Philosophy (PID 1 machined, squashfs, udevd, containerd & COSI)](https://docs.siderolabs.com/talos/v1.9/learn-more/architecture) — Documentação oficial de arquitetura e filosofia do Talos Linux explicando o binário init machined (PID 1), montagem do rootfs squashfs, serviços em containers containerd e sistema de recursos COSI; consultado em 2026-10-03.
- [Sidero Labs Talos — Official GitHub README.md](https://github.com/siderolabs/talos) — README oficial do repositório siderolabs/talos; consultado em 2026-10-03.
