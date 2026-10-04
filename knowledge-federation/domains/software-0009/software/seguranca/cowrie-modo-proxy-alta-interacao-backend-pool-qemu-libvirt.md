---
id: software.seguranca.tranche12.001155
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst", "https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cowrie em **Modo Proxy de Alta Interação (`backend = proxy`)**: Orquestrando um Pool de VMs **QEMU/Libvirt (`backend_pool`)** Transparentemente

## Em uma frase
Para 95% das botnets automatizadas e atacantes oportunistas, o emulador Python do Cowrie (`backend = shell`) é mais do que suficiente; mas e quando você quer estudar um **atacante humano avançado (APT)** que compila exploits locais de kernel em C, executa binários ELF complexos ou testa ferramentas que perceberiam as limitações de um shell emulado?

## Por que importa
Para esse cenário, o Cowrie oferece o **Modo Proxy (`backend = proxy`)** combinado com o **`[backend_pool]`**: o Cowrie atua como um proxy man-in-the-middle SSH/Telnet que gerencia automaticamente um **pool de máquinas virtuais Linux reais (Ubuntu, Debian, OpenWrt, ARM/MIPS) rodando sobre QEMU/KVM**!

## Como funciona
Quando o atacante conecta no Cowrie, o `backend_pool` aloca instantaneamente uma VM limpa (usando snapshots *copy-on-write* `qcow2` sobre uma imagem base), encaminha toda a sessão SSH/Telnet para aquela VM real enquanto o Cowrie no meio intercepta e grava 100% dos comandos, arquivos transferidos via SFTP/SCP e logs TTY e, assim que o atacante desconecta (ou atinge o `vm_unused_timeout`), a VM é destruída ou revertida ao snapshot limpo!

## Exemplo
```ini
# Configuracao de exemplo em etc/cowrie.cfg para operar o Cowrie em modo Proxy de Alta Interacao com pool local de VMs QEMU
[honeypot]
backend = proxy

[proxy]
backend = pool
pool_host = 127.0.0.1
pool_port = 6415
backend_user = root
backend_pass = SenhaInternaDaVM

[backend_pool]
pool_only = false
max_vms = 3
vm_unused_timeout = 600
save_snapshots = true
```

## Limites e trade-offs
Com **`save_snapshots = true`** no `[backend_pool]`, o Cowrie preserva o disco diferencial `qcow2` das VMs que sofreram intrusão — permitindo que você passe o **AIDE** ou monte o disco posteriormente para inspecionar todos os arquivos modificados pelo invasor dentro da VM real!

## Como verificar
Ao operar em modo `proxy` de alta interação, **isole rigorosamente a sub-rede das VMs QEMU com `nftables`** (bloqueando acesso à rede interna e limitando a taxa de conexões de saída) para impedir que o atacante use a VM do honeypot como plataforma de ataque contra terceiros na internet!

## Conexões
- [[cowrie-captura-malware-downloads-ttylog-playlog-asciinema]] — Veja também: Coleta Automática de Malware (**`var/lib/cowrie/downloads/`**) e Replay Visual de Sessões TTY com **`playlog`** e **`asciinema`**.
- [[cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel]] — Veja também: Telemetria Estruturada do Cowrie (**`var/log/cowrie/cowrie.json`**): Eventos `eventid`, Fingerprints **HASSH** e Integração com SIEM e **MISP**.
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Referência cruzada direta com cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm.
- [[cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker]] — Referência cruzada direta com cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker.
- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Referência cruzada direta com nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
