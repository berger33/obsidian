---
id: software.seguranca.tranche06.000596
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

# NetExec (`nxc winrm` & `nxc wmi`): Auditoria de Gerenciamento Remoto Windows (WS-Management Portas `5985`/`5986` e WMI) e Execução (`-x` / `-X`)

## Em uma frase
Os módulos **`nxc winrm`** (protocolo *Windows Remote Management / WS-Management* nas portas TCP `5985` HTTP e `5986` HTTPS) e **`nxc wmi`** (protocolo *Windows Management Instrumentation* sobre DCOM/RPC) permitem auditar permissões de administração remota mesmo quando o acesso administrativo via SMB (`445`) está bloqueado por firewall ou restrito.

## Por que importa
Usuários pertencentes ao grupo **`Remote Management Users`** (ou `Administrators`) podem autenticar via WinRM e executar comandos Cmd (`-x "whoami /all"`) ou expressões PowerShell (`-X '$PSVersionTable'`) sem precisar abrir conexões administrativas no compartilhamento `ADMIN$` do SMB.

## Como funciona
O módulo `nxc smb` / `nxc winrm` / `nxc wmi` permite ainda escolher o método subjacente de execução remota com **`--exec-method`** (`wmiexec`, `mmcexec`, `smbexec`, `atexec`) e auditar cofres locais de credenciais (`--sam`, `--lsa`, `--dpapi`).

## Exemplo
```bash
# Verificar acesso administrativo via WinRM (5985/5986) e executar comando PowerShell de auditoria de configuracao
nxc winrm 10.10.20.0/24 -u 'sec_auditor' -p 'AuditPass!2026' -X 'Get-MpComputerStatus | Select-Object AMServiceEnabled,RealTimeProtectionEnabled'
```

## Limites e trade-offs
Por padrão no Windows Server 2012 R2 e superiores, o serviço WinRM (`5985/TCP`) já vem habilitado de fábrica e aceita payloads cifrados com a chave de sessão SPNEGO (Kerberos/NTLM) mesmo na porta 5985.

## Como verificar
Audite quais contas pertencem ao grupo local `Remote Management Users` nas estações e servidores usando `nxc smb <alvo> --local-groups "Remote Management Users"`.

## Conexões
- [[netexec-autenticacao-kerberos-ccache-aeskey-kdchost-opsec]] — Veja também: NetExec: Operação 100% Kerberos (`-k`, `--use-kcache`, `--aesKey` e `--kdcHost`) em Redes com NTLM Restrito.
- [[netexec-protocolos-mssql-ssh-rdp-ftp-vnc-auditoria-multi-servico]] — Veja também: NetExec (`nxc mssql`, `ssh`, `rdp`, `ftp`, `vnc`): Auditoria Multiprocolo Híbrida Windows/Linux, Capturas de Tela RDP e Privileged Escalation.
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Referência cruzada direta com netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces.
- [[impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec]] — Referência cruzada direta com impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
