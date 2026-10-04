---
id: software.seguranca.tranche12.001167
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

# Implantação de Frota de Sensores OpenCanary com **Docker (`--network host`)** e **Ansible**: Preservando o IP Real de Origem (`src_host`)

## Em uma frase
Se você rodar o container Docker do OpenCanary com mapeamento de portas bridge padrão (`docker run -p 80:80 -p 3306:3306`), um problema clássico de rede em containers pode ocorrer: dependendo da configuração do `docker-proxy` e NAT do host, o honeypot pode enxergar o IP do gateway da bridge `docker0` (`172.17.0.1`) como `src_host` em vez do IP real do atacante, além de o módulo `portscan` não ter visibilidade da interface física do host!

## Por que importa
Por esse motivo, a documentação oficial do OpenCanary recomenda que, ao implantar via Docker em hosts Linux, você utilize o modo de rede **`host` (`--network host` ou `network_mode: host` no `docker-compose.yml`)** e monte o seu arquivo `/etc/opencanaryd/opencanary.conf` customizado como volume somente-leitura (`:ro`)!

## Como funciona
Com um playbook **Ansible** simples que distribui personas diferentes de `opencanary.conf` para micro-VMs ou Raspberry Pis em cada segmento de rede (DMZ, Rede de Servidores, Rede de Bancos de Dados, Rede de Estações/Wi-Fi Corporativo), você constrói uma malha corporativa completa de detecção de movimentação lateral em menos de uma tarde!

## Exemplo
```bash
# Executar o OpenCanary em container Docker no Linux utilizando --network host para preservar 100% da fidelidade de rede (src_host)
docker run -d \
  --name opencanary-sensor \
  --restart unless-stopped \
  --network host \
  -v /etc/opencanaryd/opencanary.conf:/root/.opencanary.conf:ro \
  -v /var/log/opencanary:/var/tmp \
  thinkst/opencanary:latest
```

## Limites e trade-offs
Ao montar `/etc/opencanaryd/opencanary.conf` com a flag **`:ro` (*read-only*)** dentro do container, você garante por isolamento do kernel que o arquivo de configuração nunca possa ser modificado pelo processo em execução.

## Como verificar
Monitore a saúde dos seus sensores (`heartbeat`) verificando periodicamente se o processo `opencanaryd` está ativo e enviando logs para o coletor central.

## Conexões
- [[opencanary-alertas-logger-syslog-webhook-slack-correlator-siem]] — Veja também: Arquitetura de Alertas e **`PyLogger`** do OpenCanary: **Syslog RFC, Webhooks (Slack/Teams), SMTP, HPFeeds** e **`opencanary-correlator`**.
- [[opencanary-integracao-canarytokens-breadcrumbs-active-directory-dns]] — Veja também: Estratégia de **Breadcrumbs (Iscas)** para Atrair Atacantes ao OpenCanary: Registros **DNS Internos**, **SPNs no Active Directory** e Arquivos `.env`.
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker]] — Referência cruzada direta com cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
