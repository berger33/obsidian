---
id: software.seguranca.tranche12.001164
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

# Detecção Precoce de Reconhecimento de Rede com OpenCanary: Módulos **`portscan`**, **`snmp` (`161/UDP`)**, **`llmnr` (`5355/UDP`)**, **`tftp`** e **`ntp`**

## Em uma frase
Antes mesmo de tentar fazer login em qualquer serviço, a primeira ação de um invasor ou pentester ao acessar uma rede interna é rodar um **Port Scan (`nmap -sS`, `-sV`, `-O` OS Detection)**, consultar comunidades **SNMP (`public` / `private`)** em busca de roteadores e switches, ou escutar/envenenar resolução de nomes via **LLMNR (`5355/UDP`)**!

## Por que importa
O OpenCanary detecta todas essas técnicas silenciosas de reconhecimento através de módulos dedicados: **(1) `portscan.enabled: true`** — configura regras de log no firewall do Linux (`iptables` gravando em `/var/log/kern.log`) para detectar instantaneamente **SYN Scans (`portscan.synrate`)**, **Nmap OS Fingerprinting (`portscan.nmaposrate`)** e varreduras locais; **(2) `snmp.enabled: true`** (baseado em `scapy`) — escuta na porta `161/UDP` e registra o IP de origem e a *community string* (`public`, `private`) tentada pelo scanner; e **(3) `llmnr.enabled: true`** — envia consultas periódicas pelo hostname configurado (`llmnr.hostname`, ex.: `DC03`) e **dispara um alerta crítico caso uma ferramenta como o `Responder` tente responder falsificando o IP daquele hostname (LLMNR Poisoning)**!

## Como funciona
Esse módulo `llmnr` do OpenCanary é um detector brilhante e automático de ataques **`Responder` / `Inveigh`** na rede local!

## Exemplo
```json
{
  "device.node_id": "net-core-canary-01",
  "portscan.enabled": true,
  "portscan.logfile": "/var/log/kern.log",
  "portscan.synrate": 5,
  "portscan.nmaposrate": 5,
  "snmp.enabled": true,
  "snmp.port": 161,
  "llmnr.enabled": true,
  "llmnr.hostname": "FIN-SQL-PROD09",
  "llmnr.query_interval": 60
}
```

## Limites e trade-offs
Observe como o módulo **`llmnr`** funciona como um "canário na mina de carvão" contra envenenamento de resolução de nomes: ele pergunta na sub-rede a cada 60 segundos *"Quem é `FIN-SQL-PROD09`?"* (um nome que não existe no DNS!). Se qualquer máquina da VLAN responder *"Sou eu!"*, você acabou de pegar em flagrante um atacante rodando **Responder** naquela sub-rede!

## Como verificar
Nota técnica importante: no Linux moderno (Ubuntu 22.04/24.04, Debian 12), lembre-se de que o módulo `portscan` do OpenCanary utiliza a sintaxe do `iptables` e monitora `/var/log/kern.log` (certifique-se de que o daemon `rsyslog` está instalado e gravando logs do kernel em `/var/log/kern.log`).

## Conexões
- [[opencanary-modulos-bancos-dados-mysql-mssql-redis-git-ssh-rdp]] — Veja também: Armadilhas para **Bancos de Dados (`MySQL`, `MSSQL`, `Redis`)**, **Repositórios `Git` (`9418`)** e **Acesso Remoto (`RDP`, `VNC`, `SSH`, `Telnet`)** no OpenCanary.
- [[opencanary-customizacao-banners-perfis-servicos-perfis-industriais]] — Veja também: Módulo **`tcpbanner`** do OpenCanary: Emulando Protocolos Proprietários, Serviços Legados e Controladores Industriais (**ICS/OT**).
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[certipy-ataques-configuracao-ca-relay-esc6-esc8-esc11-epa-https]] — Referência cruzada direta com certipy-ataques-configuracao-ca-relay-esc6-esc8-esc11-epa-https.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
