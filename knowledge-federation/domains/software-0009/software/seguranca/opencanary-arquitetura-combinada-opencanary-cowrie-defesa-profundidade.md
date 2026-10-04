---
id: software.seguranca.tranche12.001170
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

# Arquitetura de Deception em Camadas: Combinando **OpenCanary** (Detecção Multiprotocolo Rápida) e **Cowrie** (Análise Comportamental Pós-Login)

## Em uma frase
Quando usar o **OpenCanary**, quando usar o **Cowrie**, e como combinar ambos em uma arquitetura corporativa de **Deception Engineering** de classe mundial?

## Por que importa
O **OpenCanary** é um honeypot **multiprotocolo de baixa interação** focado em **alerta imediato de intrusão na rede interna**: na porta `22`, o módulo SSH do OpenCanary registra a versão do cliente SSH, captura o usuário/senha ou chave pública tentada (`logtype 4002`) e **rejeita o login** (ele não abre um shell interativo para o atacante digitar comandos). Já o **Cowrie** é um honeypot **especializado em SSH e Telnet de média/alta interação**, projetado para **deixar o atacante entrar no shell falso**, observar toda a sua sequência de comandos pós-exploração e capturar seus scripts e malwares!

## Como funciona
Em uma arquitetura combinada no mesmo servidor de Deception: o **OpenCanary** assume as portas `80`, `443`, `445` (SMB), `1433` (MSSQL), `3306` (MySQL), `3389` (RDP), `6379` (Redis) e `5355/UDP` (LLMNR), enquanto você deixa `"ssh.enabled": false` e `"telnet.enabled": false` no `opencanary.conf` para que as portas **`22` e `23` sejam atendidas pelo Cowrie**!

## Exemplo
```bash
# Verificar com ss -tulnp em um no integrado de Deception que o OpenCanary atende HTTP/MySQL/Redis e o Cowrie atende SSH/Telnet
sudo ss -tulnp | grep -E "(opencanaryd|twistd|cowrie)"
```

## Limites e trade-offs
Com essa divisão de responsabilidades no mesmo host, qualquer tentativa de acesso Web, SMB, Banco de Dados ou RDP dispara imediatamente o alerta do OpenCanary, e qualquer atacante que tente login SSH ou Telnet é capturado na sessão interativa completa do Cowrie com gravação `ttylog` e coleta de artefatos!

## Como verificar
Encaminhe tanto o `/var/log/opencanary.log` quanto o `var/log/cowrie/cowrie.json` para o mesmo índice de Deception no seu SIEM com severidade máxima no SOC.

## Conexões
- [[opencanary-mapeamento-logtypes-regras-sigma-siem-automacao-soar]] — Veja também: Tabela de **`logtype`** do OpenCanary e Automação de Resposta (**SOAR / Active Response**) no SIEM.
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Referência cruzada direta com cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm.
- [[cowrie-deception-engineering-intranet-deteccao-movimentacao-lateral-ssh]] — Referência cruzada direta com cowrie-deception-engineering-intranet-deteccao-movimentacao-lateral-ssh.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
