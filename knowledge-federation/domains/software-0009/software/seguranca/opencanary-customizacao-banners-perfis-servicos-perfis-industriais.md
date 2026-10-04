---
id: software.seguranca.tranche12.001165
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

# Módulo **`tcpbanner`** do OpenCanary: Emulando Protocolos Proprietários, Serviços Legados e Controladores Industriais (**ICS/OT**)

## Em uma frase
E se você precisar emular um protocolo que não possui um módulo dedicado no OpenCanary — como uma porta de gerenciamento de mainframe, uma impressora corporativa JetDirect (`9100`), um serviço Memcached (`11211`), um agente Zabbix ou uma porta TCP de equipamento industrial?

## Por que importa
O módulo **`tcpbanner`** do OpenCanary permite configurar até `N` ouvintes TCP customizados (`tcpbanner_1` até `tcpbanner_10`, controlado por `"tcpbanner.maxnum": 10`) em qualquer porta TCP, definindo: **(1) `initbanner`** (banner enviado pelo honeypot assim que o cliente estabelece a conexão TCP), **(2) `datareceivedbanner`** (resposta enviada após o cliente mandar dados), e **(3) `alertstring.enabled` / `alertstring`** (gatilho especial caso os dados enviados pelo atacante contenham uma string específica)!

## Como funciona
Com apenas 8 linhas de JSON no `opencanary.conf`, você cria um emulador sob medida para qualquer serviço TCP interno da sua organização!

## Exemplo
```json
{
  "tcpbanner.enabled": true,
  "tcpbanner.maxnum": 2,
  "tcpbanner_1.enabled": true,
  "tcpbanner_1.port": 11211,
  "tcpbanner_1.initbanner": "",
  "tcpbanner_1.datareceivedbanner": "STAT pid 1492\r\nSTAT version 1.6.14\r\nEND\r\n",
  "tcpbanner_1.alertstring.enabled": true,
  "tcpbanner_1.alertstring": "stats"
}
```

## Limites e trade-offs
O módulo `tcpbanner` também suporta parâmetros de `keep_alive` (`tcpbanner_1.keep_alive.enabled`, `keep_alive_secret`, `keep_alive_interval`), permitindo manter conexões persistentes monitoradas.

## Como verificar
Use `nmap -sV -p <porta>` contra o seu `tcpbanner` em homologação para validar se o Nmap classifica o serviço exatamente como o software alvo que você deseja mimetizar.

## Conexões
- [[opencanary-deteccao-varredura-rede-portscan-snmp-llmnr-ntp-tftp]] — Veja também: Detecção Precoce de Reconhecimento de Rede com OpenCanary: Módulos **`portscan`**, **`snmp` (`161/UDP`)**, **`llmnr` (`5355/UDP`)**, **`tftp`** e **`ntp`**.
- [[opencanary-alertas-logger-syslog-webhook-slack-correlator-siem]] — Veja também: Arquitetura de Alertas e **`PyLogger`** do OpenCanary: **Syslog RFC, Webhooks (Slack/Teams), SMTP, HPFeeds** e **`opencanary-correlator`**.
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[cowrie-anti-fingerprinting-disfarce-honeypot-banners-uptime-rede]] — Referência cruzada direta com cowrie-anti-fingerprinting-disfarce-honeypot-banners-uptime-rede.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
