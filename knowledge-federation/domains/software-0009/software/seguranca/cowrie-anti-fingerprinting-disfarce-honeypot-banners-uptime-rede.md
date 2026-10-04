---
id: software.seguranca.tranche12.001158
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

# Técnicas de **Anti-Fingerprinting** no Cowrie: Como Evitar que Atacantes e Scanners Identifiquem que o Servidor é um Honeypot

## Em uma frase
Scanners especializados de grupos de ameaça (e ferramentas como `kippo-detect` ou scripts de verificação de botnets) testam indicadores conhecidos dos padrões de fábrica do Cowrie para abortar o ataque caso detectem um honeypot!

## Por que importa
Para blindar sua instância do Cowrie contra detecção (*Anti-Fingerprinting*), você deve customizar no mínimo cinco indicadores em `etc/cowrie.cfg` e `honeyfs/`: **(1) `hostname`**: troque o padrão famoso `svr04` por um nome que siga a convenção real de nomenclatura da sua empresa (ex.: `prd-k8s-worker-09` ou `srv-erp-db02`); **(2) `[ssh] version`**: substitua o banner SSH padrão por exatamente a mesma string `SSH-2.0-OpenSSH_...` emitida pelos seus servidores Linux reais; **(3) `fake_addr` e `internet_facing_ip`**: ajuste os IPs exibidos pelos comandos emulados `ifconfig`, `ip a`, `w`, `last` e `netstat`; **(4) `boot_offset`**: defina um tempo de atividade realista (em segundos) para `/proc/uptime` e `uptime`; e **(5) Usuários e processos em `honeyfs/`**: substitua o usuário padrão `phil` em `/etc/passwd` e a lista estática do comando `ps`!

## Como funciona
Esses 5 minutos de customização multiplicam drasticamente o engajamento de atacantes humanos reais dentro do honeypot!

## Exemplo
```ini
# Ajustes essenciais de Anti-Fingerprinting em etc/cowrie.cfg para mimetizar um servidor Ubuntu 24.04 corporativo real
[honeypot]
hostname = srv-fin-batch03
fake_addr = 10.40.12.88
boot_offset = 4838400

[ssh]
version = SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.5
ciphers = chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr
```

## Limites e trade-offs
Não esqueça de regenerar ou customizar também os arquivos de sistema lidos frequentemente por scripts de fingerprinting em `honeyfs/proc/cpuinfo`, `honeyfs/proc/meminfo`, `honeyfs/proc/version` e `honeyfs/etc/issue`!

## Como verificar
Teste sua instância do Cowrie conectando via `ssh -v` e executando `uname -a`, `id`, `w`, `ps aux`, `cat /etc/passwd` e `df -h` sob a perspectiva de um invasor.

## Conexões
- [[cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker]] — Veja também: Implantação Segura do Cowrie em Produção: Redirecionamento da Porta **`22` -> `2222`** via **`nftables`**, Gerenciamento do SSH Real e Hardening Docker.
- [[cowrie-modo-llm-inteligencia-artificial-emulacao-dinamica-comandos]] — Veja também: Emulação Dinâmica de Comandos com **IA Generativa (`backend = llm`)** no Cowrie: Como Responder a Qualquer Comando Inédito do Atacante.
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Referência cruzada direta com cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm.
- [[cowrie-sistema-arquivos-falso-fs-pickle-fsctl-createfs-honeyfs]] — Referência cruzada direta com cowrie-sistema-arquivos-falso-fs-pickle-fsctl-createfs-honeyfs.
- [[opencanary-customizacao-banners-perfis-servicos-perfis-industriais]] — Referência cruzada direta com opencanary-customizacao-banners-perfis-servicos-perfis-industriais.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
