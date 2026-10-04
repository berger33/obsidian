---
id: software.seguranca.tranche12.001162
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

# Emulação de **Servidores de Arquivos (SMB/Samba)** e **Painéis Web de Storage (`http.skin = nasLogin`)** no OpenCanary

## Em uma frase
Quando um invasor ou operador de ransomware entra em uma rede interna corporativa, quais são os dois primeiros alvos que ele procura imediatamente para roubar backups e dados confidenciais? **Compartilhamentos de rede Windows (`SMB` porta `445`)** e **interfaces Web de administração de storages NAS (Synology / QNAP / NetApp nas portas `80`/`443`/`8080`)**!

## Por que importa
No `/etc/opencanaryd/opencanary.conf`, habilitar **`"http.enabled": true`** e **`"https.enabled": true`** com **`"http.skin": "nasLogin"`** levanta instantaneamente uma página convincente de login de Storage NAS (`Apache/2.2.22 (Ubuntu)` customizável) que registra qualquer tentativa de login HTTP/HTTPS (`logtype 3000/3001`) com usuário, senha, User-Agent e IP do invasor!

## Como funciona
Paralelamente, o módulo **SMB (`"smb.enabled": true`, `"smb.auditfile": "/var/log/samba-audit.log"`)** integra-se ao módulo **`vfs_full_audit`** do Samba para monitorar uma pasta compartilhada "isca" (ex.: `\\FIN-NAS-02\Backups_Cofre$`): no instante em que o invasor lista a pasta ou abre um arquivo `.xlsx`/`.kdbx` falso dentro do compartilhamento, o OpenCanary parseia o log de auditoria do Samba e dispara um alerta crítico em tempo real!

## Exemplo
```json
{
  "device.node_id": "fin-nas-02-canary",
  "http.enabled": true,
  "http.port": 80,
  "http.banner": "nginx/1.24.0",
  "http.skin": "nasLogin",
  "https.enabled": true,
  "https.port": 443,
  "https.skin": "nasLogin",
  "smb.enabled": true,
  "smb.auditfile": "/var/log/samba-audit.log"
}
```

## Limites e trade-offs
Ao configurar o Samba para o módulo SMB do OpenCanary no Linux, certifique-se de configurar o `syslog` / `rsyslog` para gravar a facilidade `local7` em `/var/log/samba-audit.log` e defina a pasta compartilhada como **somente-leitura (`read only = yes`)** para que ninguém possa depositar arquivos reais no honeypot.

## Como verificar
Você também pode criar skins HTML customizadas no diretório `data/http/skin/` copiando o layout exato do portal de intranet ou VPN da sua empresa.

## Conexões
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Veja também: Arquitetura do **OpenCanary (`thinkst/opencanary`)**: Honeypot Multiprotocolo de Baixa Interação para Detecção de Intrusão em Redes Internas.
- [[opencanary-modulos-bancos-dados-mysql-mssql-redis-git-ssh-rdp]] — Veja também: Armadilhas para **Bancos de Dados (`MySQL`, `MSSQL`, `Redis`)**, **Repositórios `Git` (`9418`)** e **Acesso Remoto (`RDP`, `VNC`, `SSH`, `Telnet`)** no OpenCanary.
- [[opencanary-alertas-logger-syslog-webhook-slack-correlator-siem]] — Referência cruzada direta com opencanary-alertas-logger-syslog-webhook-slack-correlator-siem.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
