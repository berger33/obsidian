---
id: software.seguranca.tranche12.001163
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

# Armadilhas para **Bancos de Dados (`MySQL`, `MSSQL`, `Redis`)**, **Repositórios `Git` (`9418`)** e **Acesso Remoto (`RDP`, `VNC`, `SSH`, `Telnet`)** no OpenCanary

## Em uma frase
Desenvolvedores e engenheiros de DevOps frequentemente deixam strings de conexão de bancos de dados (`mysql://`, `redis://`, `Server=tcp:10.20.30.40,1433`) em arquivos de configuração ou variáveis de ambiente. E se você plantar credenciais "isca" (*honeytokens*) apontando para o endereço IP de um sensor **OpenCanary** na sub-rede de bancos de dados?

## Por que importa
No `opencanary.conf`, você pode ativar simultaneamente os emuladores de protocolo de **`mysql`** (porta `3306`, simulando handshake nativo do MySQL Server e capturando o usuário e hash de autenticação), **`mssql`** (porta `1433`, simulando Microsoft SQL Server `2012`/`2019` e capturando logins SQL Auth e NTLMSSP Windows Auth!), **`redis`** (porta `6379`, capturando comandos como `AUTH`, `INFO`, `CONFIG SET`, `SLAVEOF` usados por malwares de cryptomining!) e **`git`** (porta `9418`, alertando quando alguém tenta dar `git clone git://...` no repositório falso)!

## Como funciona
Somados aos módulos **`rdp`** (`3389`), **`vnc`** (`5000`), **`ssh`** (`22`) e **`telnet`** (`23`, que suporta lista de credenciais falsas `telnet.honeycreds` com hashes PBKDF2-SHA512), o sensor cobre todos os protocolos usados por atacantes na fase de movimentação lateral!

## Exemplo
```json
{
  "device.node_id": "prd-db-replica-04",
  "mysql.enabled": true,
  "mysql.port": 3306,
  "mysql.banner": "8.0.36-0ubuntu0.22.04.1",
  "mssql.enabled": true,
  "mssql.port": 1433,
  "mssql.version": "2019",
  "redis.enabled": true,
  "redis.port": 6379,
  "git.enabled": true,
  "git.port": 9418,
  "rdp.enabled": true,
  "rdp.port": 3389
}
```

## Limites e trade-offs
Dica de ouro de Deception Engineering: **não ative todos os 18 protocolos de uma vez no mesmo endereço IP** (um servidor que roda simultaneamente FTP, Telnet, SMB Windows, MSSQL, MySQL, Redis, Git, SIP e SNMP parece imediatamente um honeypot no Nmap!). Em vez disso, crie **personas coerentes por VLAN**: um sensor com persona de *Banco de Dados Linux* (`ssh` + `mysql` + `redis`), outro com persona de *Servidor Windows/SQL* (`smb` + `rdp` + `mssql`) e outro com persona de *Storage NAS* (`http` + `https` + `ftp` + `snmp`)!

## Como verificar
Plante a string de conexão da persona de Banco de Dados dentro de um arquivo `.env` falso nas máquinas da sua DMZ para detectar invasores no exato segundo em que tentarem usar a credencial vazada.

## Conexões
- [[opencanary-modulos-protocolos-http-https-naslogin-smb-samba-audit]] — Veja também: Emulação de **Servidores de Arquivos (SMB/Samba)** e **Painéis Web de Storage (`http.skin = nasLogin`)** no OpenCanary.
- [[opencanary-deteccao-varredura-rede-portscan-snmp-llmnr-ntp-tftp]] — Veja também: Detecção Precoce de Reconhecimento de Rede com OpenCanary: Módulos **`portscan`**, **`snmp` (`161/UDP`)**, **`llmnr` (`5355/UDP`)**, **`tftp`** e **`ntp`**.
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens]] — Referência cruzada direta com pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
