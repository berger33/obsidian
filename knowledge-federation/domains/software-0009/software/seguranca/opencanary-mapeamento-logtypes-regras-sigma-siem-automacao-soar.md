---
id: software.seguranca.tranche12.001169
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

# Tabela de **`logtype`** do OpenCanary e Automação de Resposta (**SOAR / Active Response**) no SIEM

## Em uma frase
Para escrever regras de detecção precisas no seu SIEM (ou regras **Sigma** customizadas para os logs JSON do OpenCanary) e acionar playbooks de contenção automática (**SOAR**), é essencial conhecer os códigos numéricos de **`logtype`** emitidos pelo `opencanaryd`!

## Por que importa
Os códigos seguem uma numeração estruturada por protocolo: **`1000`** (Boot/Start do daemon), **`2000`** (FTP login attempt), **`3000`** (HTTP GET request) e **`3001`** (HTTP POST login attempt), **`4000`** (SSH connection), **`4001`** (SSH remote version) e **`4002`** (SSH login attempt), **`5001`** (Portscan SYN), **`5002`** (Nmap OS scan), **`6001`** (Telnet login attempt), **`7001`** (HTTP Proxy request), **`8001`** (MySQL login attempt), **`9001`** (MSSQL login attempt — SQL Auth) e **`9002`** (MSSQL login attempt — Windows Auth), **`11001`** (NTP monlist), **`12001`** (Redis command), **`13001`** (TCP Banner), **`14001`** (VNC), **`15001`** (SIP), **`16001`** (Git clone request), **`17001`** (Portscan Nmap NULL/XMAS) e **`18001`** (LLMNR query response)!

## Como funciona
Sabendo esses códigos, você pode classificar no SIEM: eventos de reconhecimento (`3000`, `4000`, `5001`) como severidade **Alta**, e eventos de tentativa explícita de autenticação ou exploração (`2000`, `3001`, `4002`, `8001`, `9001`, `12001`, `18001` LLMNR Poisoning) como severidade **Crítica (P1)**!

## Exemplo
```bash
# Filtrar do arquivo /var/log/opencanary.log apenas eventos de tentativa de autenticacao (FTP, HTTP, SSH, Telnet, MySQL, MSSQL) ou LLMNR Poisoning
jq 'select(.logtype | IN(2000, 3001, 4002, 6001, 8001, 9001, 9002, 12001, 18001)) | {
  utc_time: .utc_time,
  sensor: .node_id,
  logtype: .logtype,
  attacker_ip: .src_host,
  dst_port: .dst_port,
  details: .logdata
}' /var/log/opencanary.log
```

## Limites e trade-offs
Cuidado ao configurar ações de **bloqueio automático por IP (Active Response)** em cima de protocolos baseados em **UDP sem handshake (`snmp` `161/UDP`, `ntp` `123/UDP`, `tftp` `69/UDP`)**: como o endereço IP de origem de um único pacote UDP pode ser falsificado (*IP Spoofing*) na rede local por um atacante que queira provocar negação de serviço contra o IP do Domain Controller, **só acione isolamento automático de host em eventos que completaram um handshake TCP de 3 vias ou em alertas correlacionados com o EDR**!

## Como verificar
Essa distinção entre protocolos TCP (com handshake completado) e pacotes UDP unitários evita ataques de *Self-DoS* contra sua automação SOAR.

## Conexões
- [[opencanary-integracao-canarytokens-breadcrumbs-active-directory-dns]] — Veja também: Estratégia de **Breadcrumbs (Iscas)** para Atrair Atacantes ao OpenCanary: Registros **DNS Internos**, **SPNs no Active Directory** e Arquivos `.env`.
- [[opencanary-arquitetura-combinada-opencanary-cowrie-defesa-profundidade]] — Veja também: Arquitetura de Deception em Camadas: Combinando **OpenCanary** (Detecção Multiprotocolo Rápida) e **Cowrie** (Análise Comportamental Pós-Login).
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[opencanary-alertas-logger-syslog-webhook-slack-correlator-siem]] — Referência cruzada direta com opencanary-alertas-logger-syslog-webhook-slack-correlator-siem.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
