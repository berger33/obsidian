---
id: software.seguranca.tranche12.001156
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

# Telemetria Estruturada do Cowrie (**`var/log/cowrie/cowrie.json`**): Eventos `eventid`, Fingerprints **HASSH** e Integração com SIEM e **MISP**

## Em uma frase
Toda atividade que ocorre dentro do Cowrie é registrada em tempo real no arquivo estruturado **`var/log/cowrie/cowrie.json`** (com fuso horário padrão `timezone = UTC`), além de contar com módulos nativos de *output* em `[output_*]` no `cowrie.cfg` para **Elasticsearch, Splunk HEC, Graylog, MySQL/PostgreSQL, Slack, Telegram, AbusesIPDB, VirusTotal e MISP**!

## Por que importa
Cada linha JSON em `cowrie.json` contém o identificador da sessão (`session`), o IP/porta de origem (`src_ip`, `src_port`), o `sensor` e um **`eventid`** padronizado, como: **`cowrie.session.connect`**, **`cowrie.client.kex`** (que inclui o hash **HASSH (`hassh` / `hasshAlgorithms`)** — o equivalente ao JA3 do TLS para identificar a ferramenta exata de cliente SSH usada pelo atacante, mesmo que ele mude o banner!), **`cowrie.login.success` / `cowrie.login.failed`**, **`cowrie.command.input`**, **`cowrie.session.file_download`** e **`cowrie.direct-tcpip.request`**!

## Como funciona
O cálculo automático do fingerprint **HASSH** em cada conexão permite agrupar campanhas de um mesmo ator de ameaça ou scanner específico (ex.: `libssh`, `Paramiko`, `Go crypto/ssh`, `Masscan/ZGrab`) através de múltiplos IPs de origem!

## Exemplo
```bash
# Extrair do arquivo var/log/cowrie/cowrie.json com jq o Top 10 de comandos executados pelos invasores e os fingerprints HASSH unicos
jq -r 'select(.eventid == "cowrie.command.input") | .input' ./var/log/cowrie/cowrie.json | sort | uniq -c | sort -nr | head -n 10
jq -r 'select(.eventid == "cowrie.client.kex") | "\(.hassh) -> \(.src_ip)"' ./var/log/cowrie/cowrie.json | sort -u | head -n 10
```

## Limites e trade-offs
Preste muita atenção aos eventos **`cowrie.direct-tcpip.request`** e **`cowrie.direct-tcpip.data`**: muitos invasores conectam em servidores SSH comprometidos não para abrir um shell, mas para usar o servidor como **Proxy SOCKS5 dinâmico (`ssh -D` / `ssh -L`)** para atacar alvos externos ou enviar spam; o Cowrie registra o destino exato (`dst_ip`, `dst_port`) e o payload de cada tentativa de tunelamento TCP!

## Como verificar
Habilite o módulo `[output_misp]` para publicar automaticamente no seu servidor **MISP** os hashes SHA-256 e URLs dos malwares inéditos capturados em `downloads/`.

## Conexões
- [[cowrie-modo-proxy-alta-interacao-backend-pool-qemu-libvirt]] — Veja também: Cowrie em **Modo Proxy de Alta Interação (`backend = proxy`)**: Orquestrando um Pool de VMs **QEMU/Libvirt (`backend_pool`)** Transparentemente.
- [[cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker]] — Veja também: Implantação Segura do Cowrie em Produção: Redirecionamento da Porta **`22` -> `2222`** via **`nftables`**, Gerenciamento do SSH Real e Hardening Docker.
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Referência cruzada direta com cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm.
- [[cowrie-captura-malware-downloads-ttylog-playlog-asciinema]] — Referência cruzada direta com cowrie-captura-malware-downloads-ttylog-playlog-asciinema.
- [[openssh-tunelamento-seguro-proxyjump-bastion-restricao-forwarding]] — Referência cruzada direta com openssh-tunelamento-seguro-proxyjump-bastion-restricao-forwarding.

## Fontes
- [Cowrie Official GitHub (`README.rst`) — Medium to High Interaction SSH and Telnet Honeypot](https://raw.githubusercontent.com/cowrie/cowrie/main/README.rst) — documentação oficial do Cowrie cobrindo os modos `shell`, `proxy` e `llm`, sistema de arquivos falso `fs.pickle`, utilitários `fsctl`/`createfs`/`playlog` e logs JSON; consultado em 2026-10-03.
- [Cowrie Official Configuration Reference (`src/cowrie/data/etc/cowrie.cfg.dist`)](https://raw.githubusercontent.com/cowrie/cowrie/main/src/cowrie/data/etc/cowrie.cfg.dist) — especificação completa dos parâmetros de configuração do Cowrie (`[honeypot]`, `auth_class`, `UserDB`, `AuthRandom`, `ttylog`, `download_limit_size`, `[backend_pool]`); consultado em 2026-10-03.
