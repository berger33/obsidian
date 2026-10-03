---
id: software.devops.tranche19.001889
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml", "https://raw.githubusercontent.com/slackhq/nebula/master/README.md", "https://github.com/slackhq/nebula"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nebula Tuning de Alta Performance: ajuste de `routines`, `listen.batch`, buffers de socket (`read_buffer`/`write_buffer`) e MTU

## Em uma frase
Para workloads de alto throughput (10 Gbps+) em servidores multi-core, o `config.yml` do Nebula expõe controles de baixo nível: **`routines`** (múltiplas threads/filas TUN e sockets UDP), **`listen.batch`** (número de pacotes lidos por syscall `recvmmsg`), **`read_buffer`/`write_buffer`** e **`tun.mtu`**.

## Por que importa
Por padrão, processar toda a criptografia `AES-256-GCM` e leituras da interface TUN em uma única goroutine limita o throughput máximo ao clock de um único núcleo de CPU.

## Como funciona
Em kernels Linux modernos com suporte a multi-queue TUN e `SO_REUSEPORT`, aumentar `routines` (ex.: `4` ou `8`) distribui o processamento criptográfico e de pacotes entre múltiplos núcleos, enquanto `listen.batch: 64` e buffers de 10 MB (`10485760`) reduzem drasticamente o overhead de chamadas de sistema sob tráfego intenso.

## Exemplo
```yaml
listen:
  host: "::"
  port: 4242
  batch: 64
  read_buffer: 10485760
  write_buffer: 10485760

routines: 4

tun:
  dev: nebula1
  mtu: 1300
```

## Limites e trade-offs
Note o aviso da documentação oficial: em Linux 5.10+ com UDP GRO, cada slot de recepção aloca 64 KiB, portanto `batch: 64` consome ~4 MiB de buffer por `routine`; em dispositivos embarcados com pouca memória, reduza `batch` e mantenha `routines: 1`.

## Como verificar
Valide a configuração de tuning com `nebula -test -config config.yml` e meça o ganho de throughput entre dois hosts com `iperf3`.

## Conexões
- [[nebula-local-remote-allow-list-filtragem-interfaces-docker-cni]] — Veja também: Nebula `local_allow_list` e `remote_allow_list`: filtragem de interfaces virtuais (`docker.*`, `cni.*`) anunciadas ao Lighthouse.
- [[nebula-observabilidade-prometheus-stats-sshd-interno-diagnostico]] — Veja também: Nebula Observabilidade e Diagnóstico: exportação de métricas `stats` (Prometheus/Graphite) e servidor `sshd` interno de inspeção.

## Fontes
- [Nebula GitHub — README.md (Scalable Overlay Networking Tool, Noise Protocol ECDH/AES-256-GCM, nebula-cert PKI, Lighthouses & Curve P256/FIPS 140-3)](https://raw.githubusercontent.com/slackhq/nebula/master/examples/config.yml) — README oficial do slackhq/nebula apresentando a arquitetura peer-to-peer autenticada por certificados, criação de CA/hosts e suporte a P256/FIPS; consultado em 2026-10-03.
- [Nebula Official Configuration Reference — examples/config.yml (PKI, Static Host Map, Lighthouse, Allow Lists, Listen Batch/Buffers, Punchy, Relay, TUN & Firewall)](https://raw.githubusercontent.com/slackhq/nebula/master/README.md) — Arquivo oficial comentado de referência config.yml do Nebula detalhando pki.blocklist, SIGHUP reload, static_host_map, lighthouse, punchy, relay, unsafe_routes e firewall; consultado em 2026-10-03.
- [Nebula — Official GitHub Repository](https://github.com/slackhq/nebula) — Repositório oficial MIT do Nebula; consultado em 2026-10-03.
