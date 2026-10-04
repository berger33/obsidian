---
id: software.seguranca.tranche12.001157
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

# Implantação Segura do Cowrie em Produção: Redirecionamento da Porta **`22` -> `2222`** via **`nftables`**, Gerenciamento do SSH Real e Hardening Docker

## Em uma frase
Se o Cowrie escuta na porta `2222` rodando como usuário não-privilegiado (`cowrie`), mas os atacantes na internet ou na rede interna escaneiam a porta padrão **`22` (SSH)** e **`23` (Telnet)**, como expor o Cowrie na porta `22` mantendo o acesso administrativo legítimo ao servidor Linux real?

## Por que importa
A arquitetura padrão recomendada pela documentação oficial do Cowrie consiste em duas etapas simples: **(1)** Altere a porta do daemon **`sshd` real** do servidor host para uma porta administrativa alta (por exemplo, `Port 22022` em `/etc/ssh/sshd_config`, restrita via firewall apenas à VPN/Bastion de administração); e **(2)** Adicione uma regra **`prerouting` de DNAT no `nftables`** (ou `iptables`) redirecionando todo o tráfego de entrada TCP da porta **`22` para `2222`** (e da porta **`23` para `2223`**)!

## Como funciona
Dessa forma, o processo Python do Cowrie continua rodando com privilégios mínimos (ou isolado dentro de um container Docker rootless), enquanto qualquer atacante que conecte na porta `22` do servidor cai transparentemente dentro do honeypot!

## Exemplo
```bash
# Redirecionar com nftables as portas padrao 22 (SSH) e 23 (Telnet) para as portas nao-privilegiadas 2222 e 2223 do Cowrie
sudo nft add table ip nat
sudo nft 'add chain ip nat prerouting { type nat hook prerouting priority dstnat; policy accept; }'
sudo nft add rule ip nat prerouting tcp dport 22 redirect to :2222
sudo nft add rule ip nat prerouting tcp dport 23 redirect to :2223
```

## Limites e trade-offs
Regra crítica de segurança antes de reiniciar o `sshd` na porta `22022`: **teste a nova conexão SSH administrativa em uma segunda janela de terminal antes de fechar sua sessão atual** e verifique com `sshd -t` se a configuração está válida!

## Como verificar
Ao rodar o Cowrie em Docker (`cowrie/cowrie:latest`), monte volumes persistentes do host para `etc/` (configurações customizadas), `var/log/cowrie/` (logs JSON) e `var/lib/cowrie/` (capturas de malware e TTY logs).

## Conexões
- [[cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel]] — Veja também: Telemetria Estruturada do Cowrie (**`var/log/cowrie/cowrie.json`**): Eventos `eventid`, Fingerprints **HASSH** e Integração com SIEM e **MISP**.
- [[cowrie-anti-fingerprinting-disfarce-honeypot-banners-uptime-rede]] — Veja também: Técnicas de **Anti-Fingerprinting** no Cowrie: Como Evitar que Atacantes e Scanners Identifiquem que o Servidor é um Honeypot.
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Referência cruzada direta com cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm.
- [[nftables-nat-masquerade-dnat-snat-redirecionamento-portas]] — Referência cruzada direta com nftables-nat-masquerade-dnat-snat-redirecionamento-portas.
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Referência cruzada direta com openssh-hardening-sshd-config-criptografia-autenticacao-restricoes.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
