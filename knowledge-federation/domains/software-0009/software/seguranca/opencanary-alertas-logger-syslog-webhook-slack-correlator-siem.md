---
id: software.seguranca.tranche12.001166
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

# Arquitetura de Alertas e **`PyLogger`** do OpenCanary: **Syslog RFC, Webhooks (Slack/Teams), SMTP, HPFeeds** e **`opencanary-correlator`**

## Em uma frase
Quando um atacante interage com qualquer porta do OpenCanary, como o alerta chega imediatamente ao seu SIEM (Splunk, Elastic, Sentinel, Wazuh, QRadar) ou canal de resposta a incidentes do SOC no Slack/Teams, sem inundar a equipe com 500 mensagens separadas se o atacante rodar um scan de portas rápido?

## Por que importa
Na seção `"logger"` do `/etc/opencanaryd/opencanary.conf`, a classe `PyLogger` (baseada no `logging.config.dictConfig` do Python) suporta múltiplos **Handlers simultâneos**: **`logging.FileHandler`** (`/var/tmp/opencanary.log`), **`logging.handlers.SysLogHandler`** (enviando eventos formatados via UDP/TCP para o coletor Syslog do SIEM), **`opencanary.logger.WebhookHandler`** (para Slack, Microsoft Teams ou Mattermost), **`SMTPHandler`** (e-mail direto) e **`hpfeeds`**!

## Como funciona
Para ambientes com dezenas de sensores OpenCanary espalhados pelas VLANs, a Thinkst disponibiliza o **`opencanary-correlator`** (`thinkst/opencanary-correlator`): um agregador central em Python + Redis que recebe os eventos de todos os sensores, **consolida múltiplos eventos disparados pelo mesmo IP de origem dentro de uma janela curta em um único incidente consolidado** e envia o alerta enriquecido para a equipe!

## Exemplo
```json
{
  "logger": {
    "class": "PyLogger",
    "kwargs": {
      "formatters": {
        "syslog_rfc": {
          "format": "opencanaryd[%(process)-5s:%(thread)d]: %(name)s %(levelname)-5s %(message)s"
        }
      },
      "handlers": {
        "file": {
          "class": "logging.FileHandler",
          "filename": "/var/log/opencanary.log"
        },
        "syslog": {
          "class": "logging.handlers.SysLogHandler",
          "address": ["10.10.5.50", 514],
          "socktype": "ext://socket.SOCK_DGRAM",
          "formatter": "syslog_rfc"
        }
      }
    }
  }
}
```

## Limites e trade-offs
Cada evento gerado pelo OpenCanary é um objeto JSON estruturado contendo **`dst_host`**, **`dst_port`**, **`src_host`**, **`src_port`**, **`local_time`**, **`utc_time`**, **`node_id`**, **`logtype`** (código numérico do tipo de evento, ex.: `2000` para FTP login, `3001` para HTTP login, `4002` para SSH login, `5001` para Portscan SYN) e **`logdata`** (com as credenciais ou parâmetros capturados)!

## Como verificar
Use `"logtype.ignorelist"` no `opencanary.conf` caso queira suprimir códigos específicos de `logtype` ruidosos em determinada VLAN.

## Conexões
- [[opencanary-customizacao-banners-perfis-servicos-perfis-industriais]] — Veja também: Módulo **`tcpbanner`** do OpenCanary: Emulando Protocolos Proprietários, Serviços Legados e Controladores Industriais (**ICS/OT**).
- [[opencanary-implantacao-docker-host-network-ansible-frota-sensores]] — Veja também: Implantação de Frota de Sensores OpenCanary com **Docker (`--network host`)** e **Ansible**: Preservando o IP Real de Origem (`src_host`).
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[opencanary-modulos-protocolos-http-https-naslogin-smb-samba-audit]] — Referência cruzada direta com opencanary-modulos-protocolos-http-https-naslogin-smb-samba-audit.
- [[cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel]] — Referência cruzada direta com cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
