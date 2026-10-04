---
id: software.seguranca.tranche06.000587
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
fontes: ["https://raw.githubusercontent.com/fortra/impacket/master/README.md", "https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md", "https://github.com/fortra/impacket"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Impacket: Auditoria de Microsoft SQL Server com `mssqlclient.py` (Autenticação Windows/SQL, `enable_xp_cmdshell`, *Impersonation* `EXECUTE AS` e *Linked Servers*)

## Em uma frase
O **`mssqlclient.py`** implementa o protocolo **TDS** (*Tabular Data Stream*) da Microsoft em Python puro, permitindo conectar a instâncias Microsoft SQL Server usando contas locais do banco ou **Autenticação Integrada do Windows** (`-windows-auth`, com senha, hash NTLM ou ticket Kerberos `-k`).

## Por que importa
Servidores de banco de dados MSSQL frequentemente possuem relações de confiança (*Linked Servers*) com outros bancos da corporação ou permitem que usuários de aplicação façam *impersonation* do login `sa` (`IMPERSONATE ANY LOGIN`); o console interativo do `mssqlclient.py` possui comandos embutidos para auditar essas cadeias rapidamente.

## Como funciona
Dentro do prompt `SQL>`, comandos nativos do `mssqlclient.py` incluem: **`enum_db`**, **`enum_links`** (lista *Linked Servers* e logins mapeados), **`enum_impersonate`** (identifica logins que a conta atual pode personificar via `exec_as_login <login>`), **`enable_xp_cmdshell`** / **`disable_xp_cmdshell`** e **`xp_cmdshell <cmd>`** (além de `sp_start_job` e execução via OLE Automation).

## Exemplo
```bash
# Conectar ao MSSQL usando autenticacao Kerberos do dominio (-windows-auth -k) para auditar Linked Servers e Impersonation
impacket-mssqlclient -windows-auth -k -no-pass \
  corp.internal/sec_auditor@sqlprod01.corp.internal
```

## Limites e trade-offs
Se você habilitar `xp_cmdshell` temporariamente durante um teste autorizado (`enable_xp_cmdshell`), execute sempre **`disable_xp_cmdshell`** imediatamente após coletar a evidência para restaurar a configuração de segurança original da instância SQL.

## Como verificar
Execute `enum_links` e `enum_impersonate` no prompt do `mssqlclient.py` para mapear caminhos de movimentação lateral entre instâncias SQL.

## Conexões
- [[impacket-enumeracao-msrpc-rpcdump-samrdump-lookupsid-netview-services]] — Veja também: Impacket: Enumeração MSRPC e Controle de Serviços (`rpcdump.py`, `samrdump.py`, `lookupsid.py`, `netview.py`, `reg.py` e `services.py`).
- [[impacket-compartilhamentos-smbclient-smbserver-transferencia-segura-smb2]] — Veja também: Impacket: Inspeção de Compartilhamentos com `smbclient.py` e Servidor SMB Efêmero com `smbserver.py` (`-smb2support` e Autenticação).
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[responder-utilitarios-runfinger-findsqlsrv-icmp-redirect-multirelay]] — Referência cruzada direta com responder-utilitarios-runfinger-findsqlsrv-icmp-redirect-multirelay.
- [[netexec-protocolos-mssql-ssh-rdp-ftp-vnc-auditoria-multi-servico]] — Referência cruzada direta com netexec-protocolos-mssql-ssh-rdp-ftp-vnc-auditoria-multi-servico.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
