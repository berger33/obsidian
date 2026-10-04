---
id: software.seguranca.tranche06.000597
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md", "https://www.netexec.wiki/getting-started/installation", "https://github.com/Pennyw0rth/NetExec"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# NetExec (`nxc mssql`, `ssh`, `rdp`, `ftp`, `vnc`): Auditoria Multiprocolo Híbrida Windows/Linux, Capturas de Tela RDP e Privileged Escalation

## Em uma frase
Além dos protocolos centrais de Active Directory, o NetExec audita bancos de dados e serviços multiplataforma através de **`nxc mssql`** (porta 1433), **`nxc ssh`** (porta 22), **`nxc rdp`** (porta 3389), **`nxc ftp`** (porta 21) e **`nxc vnc`** (porta 5900).

## Por que importa
Administradores frequentemente reutilizam a mesma senha entre sua conta do Active Directory, o login `sa` de bancos **MSSQL** (`--local-auth` no `nxc mssql`) e contas `root`/`sudo` de servidores **Linux SSH**; testar uma credencial descoberta nos 9 protocolos do NetExec revela esses caminhos híbridos.

## Como funciona
No módulo **`nxc rdp`**, é possível validar se uma conta tem permissão de login via *Remote Desktop* (NLA — *Network Level Authentication*) em dezenas de servidores sem precisar abrir janelas gráficas, além de tirar capturas de tela automatizadas de sessões abertas (`--screenshot` / `--screentime`); já no **`nxc mssql`**, flags nativas executam consultas SQL (`-q "SELECT @@VERSION;"`) e testam privilégios `sysadmin`.

## Exemplo
```bash
# Auditar instancias MSSQL com consulta SQL e verificar acesso SSH em servidores Linux da sub-rede
nxc mssql 10.10.30.0/24 -u 'sec_auditor' -p 'AuditPass!2026' -q "SELECT name, is_srvrolemember('sysadmin') FROM sys.databases;"
nxc ssh 10.10.40.0/24 -u 'sec_auditor' -p 'AuditPass!2026' --sudo-check
```

## Limites e trade-offs
No módulo `nxc ssh`, a flag **`--sudo-check`** verifica automaticamente se o usuário autenticado possui permissões `sudo` no servidor Linux, marcando o host com `(Pwn3d!)` quando há escalação administrativa disponível.

## Como verificar
Cruze os resultados no `nxcdb` (`proto mssql`, `proto ssh`, `proto rdp`) para gerar a matriz completa de serviços onde cada credencial de teste obteve acesso.

## Conexões
- [[netexec-protocolos-winrm-wmi-execucao-remota-powershell-dpapi]] — Veja também: NetExec (`nxc winrm` & `nxc wmi`): Auditoria de Gerenciamento Remoto Windows (WS-Management Portas `5985`/`5986` e WMI) e Execução (`-x` / `-X`).
- [[netexec-modulos-auditoria-adcs-petitpotam-nopac-zerologon-slinky]] — Veja também: NetExec: Catálogo de Módulos (`-M` / `--list-modules`) para Auditoria de **AD CS**, **Coerção RPC** (`coerce_plus`), **WebDAV** e **LAPS**.
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Referência cruzada direta com netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces.
- [[impacket-cliente-mssqlclient-xp-cmdshell-linked-servers-trusted-links]] — Referência cruzada direta com impacket-cliente-mssqlclient-xp-cmdshell-linked-servers-trusted-links.
- [[netexec-gerenciamento-banco-nxcdb-credenciais-hosts-exportacao]] — Referência cruzada direta com netexec-gerenciamento-banco-nxcdb-credenciais-hosts-exportacao.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
