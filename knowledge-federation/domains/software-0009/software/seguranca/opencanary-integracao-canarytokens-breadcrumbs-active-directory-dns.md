---
id: software.seguranca.tranche12.001168
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

# Estratégia de **Breadcrumbs (Iscas)** para Atrair Atacantes ao OpenCanary: Registros **DNS Internos**, **SPNs no Active Directory** e Arquivos `.env`

## Em uma frase
Um sensor **OpenCanary** passivo já detecta qualquer invasor que faça um scan de sub-rede (`nmap` / `masscan`); mas e se o invasor for extremamente furtivo, **não fizer scan de portas** e apenas consultar o DNS interno, o Active Directory ou os arquivos da máquina que acabou de comprometer?

## Por que importa
É aqui que entra a arte de plantar **Breadcrumbs (*migalhas de pão*)** apontando diretamente para o IP dos seus sensores OpenCanary!

## Como funciona
Quatro *breadcrumbs* de altíssima eficácia e custo zero: **(1) Registros DNS `A` tentadores** na zona interna (ex.: `vault-backup.corp.interno`, `k8s-admin.corp.interno`, `sql-legacy.corp.interno` apontando para o IP do OpenCanary); **(2) Contas de serviço falsas no Active Directory com `ServicePrincipalName` (SPN)** apontando para o hostname do OpenCanary (quando o invasor rodar *Kerberoasting* ou enumerar SPNs no BloodHound, ele irá direto conectar na porta `1433`/`445` do seu OpenCanary!); **(3) Entradas em `~/.ssh/config` e histórico do `.bash_history`**; e **(4) Arquivos `.env` / `web.config` falsos** em compartilhamentos internos contendo o IP do sensor!

## Exemplo
```bash
# Exemplo de entradas de Breadcrumb em /etc/hosts ou ~/.ssh/config de servidores de aplicacao apontando para o sensor OpenCanary interno
cat <<'EOF' >> ~/.ssh/config
# Servidor legado de backup do cofre de chaves (acesso restrito)
Host vault-dr-backup
    HostName 10.40.99.250
    User admin_backup
    Port 22
EOF
```

## Limites e trade-offs
Quando um invasor toca no IP `10.40.99.250` porque leu aquele `~/.ssh/config` na máquina `srv-web-01`, o alerta do OpenCanary não apenas avisa que há um invasor na rede, mas **identifica imediatamente qual máquina (`srv-web-01`, `src_host`) já foi comprometida e está servindo de pivô para o atacante**!

## Como verificar
Mantenha um inventário confidencial no SOC mapeando qual *breadcrumb* aponta para qual IP/porta do OpenCanary para acelerar o diagnóstico de causa raiz durante um incidente.

## Conexões
- [[opencanary-implantacao-docker-host-network-ansible-frota-sensores]] — Veja também: Implantação de Frota de Sensores OpenCanary com **Docker (`--network host`)** e **Ansible**: Preservando o IP Real de Origem (`src_host`).
- [[opencanary-mapeamento-logtypes-regras-sigma-siem-automacao-soar]] — Veja também: Tabela de **`logtype`** do OpenCanary e Automação de Resposta (**SOAR / Active Response**) no SIEM.
- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Referência cruzada direta com opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst.
- [[opencanary-modulos-bancos-dados-mysql-mssql-redis-git-ssh-rdp]] — Referência cruzada direta com opencanary-modulos-bancos-dados-mysql-mssql-redis-git-ssh-rdp.
- [[pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens]] — Referência cruzada direta com pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens.

## Fontes
- [Thinkst OpenCanary Official GitHub — Multi-Protocol Network Honeypot Daemon](https://raw.githubusercontent.com/thinkst/opencanary/master/README.md) — repositório oficial do OpenCanary cobrindo arquitetura do daemon `opencanaryd`, requisitos de permissão do `/etc/opencanaryd/opencanary.conf` e módulos opcionais (`smb`, `snmp`, `portscan`); consultado em 2026-10-03.
- [Thinkst OpenCanary Default Configuration Schema (`opencanary/data/settings.json`)](https://raw.githubusercontent.com/thinkst/opencanary/master/opencanary/data/settings.json) — esquema oficial de configuração JSON do OpenCanary detalhando os protocolos suportados (`ftp`, `http`, `https`, `smb`, `mysql`, `mssql`, `ssh`, `redis`, `rdp`, `sip`, `snmp`, `ntp`, `tftp`, `tcpbanner`, `telnet`, `git`, `llmnr`, `vnc`) e `PyLogger`; consultado em 2026-10-03.
