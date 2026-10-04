---
id: software.seguranca.tranche12.001161
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
fontes: ["https://raw.githubusercontent.com/thinkst/opencanary/master/README.md", "https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **OpenCanary (`thinkst/opencanary`)**: Honeypot Multiprotocolo de Baixa Interação para Detecção de Intrusão em Redes Internas

## Em uma frase
Por que a **Thinkst Canary** criou o **OpenCanary** (a versão open-source oficial do famoso appliance comercial *Thinkst Canary*), e por que honeypots internos de baixa interação estão entre os controles de segurança com **maior relação sinal-ruído (quase zero falso positivo)** em redes corporativas?

## Por que importa
Enquanto SIEMs e EDRs precisam analisar milhões de eventos legítimos por segundo para tentar separar um ataque de uma atividade administrativa normal, um nó do **OpenCanary** posicionado em uma VLAN interna **não possui nenhuma função de negócio legítima**: portanto, **qualquer pacote que tente enumerar um compartilhamento SMB, fazer login em um banco MySQL/MSSQL/PostgreSQL/Redis, abrir uma página de login de NAS (`nasLogin`) ou escanear portas naquele IP é, por definição, uma atividade anômala ou um invasor em reconhecimento interno**!

## Como funciona
Escrito em Python 3.10+ (Twisted) com consumo mínimo de memória e CPU (roda perfeitamente em um Raspberry Pi, container ou micro-VM), o daemon **`opencanaryd`** é controlado por um único arquivo JSON (**`/etc/opencanaryd/opencanary.conf`**) capaz de emular simultaneamente mais de **18 protocolos de rede**!

## Exemplo
```bash
# Instalar o OpenCanary em um ambiente virtual Python, gerar o arquivo inicial /etc/opencanaryd/opencanary.conf e iniciar com drop de privilegios
python3 -m venv ./opencanary-env && source ./opencanary-env/bin/activate
pip install opencanary
sudo ./opencanary-env/bin/opencanaryd --copyconfig
sudo chmod 600 /etc/opencanaryd/opencanary.conf
sudo ./opencanary-env/bin/opencanaryd --start --uid=nobody --gid=nogroup
```

## Limites e trade-offs
Atenção crítica de segurança destacada na documentação oficial do OpenCanary: como o `opencanaryd` inicia como `root` (para fazer bind em portas privilegiadas `< 1024`) antes de reduzir seus privilégios (`--uid=nobody --gid=nogroup`) e lê objetos Python de configuração de `logger` no `opencanary.conf`, **o arquivo `/etc/opencanaryd/opencanary.conf` DEVE pertencer a `root:root` com permissão `0600`** (caso contrário, um usuário local comum poderia escalar privilégio para `root` editando o logger)!

## Como verificar
Use `ip.ignorelist` no `opencanary.conf` para ignorar o endereço IP dos seus scanners internos oficiais de vulnerabilidade.

## Conexões
- [[opencanary-modulos-protocolos-http-https-naslogin-smb-samba-audit]] — Veja também: Emulação de **Servidores de Arquivos (SMB/Samba)** e **Painéis Web de Storage (`http.skin = nasLogin`)** no OpenCanary.
- [[opencanary-modulos-bancos-dados-mysql-mssql-redis-git-ssh-rdp]] — Referência cruzada direta com opencanary-modulos-bancos-dados-mysql-mssql-redis-git-ssh-rdp.
- [[cowrie-deception-engineering-intranet-deteccao-movimentacao-lateral-ssh]] — Referência cruzada direta com cowrie-deception-engineering-intranet-deteccao-movimentacao-lateral-ssh.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
