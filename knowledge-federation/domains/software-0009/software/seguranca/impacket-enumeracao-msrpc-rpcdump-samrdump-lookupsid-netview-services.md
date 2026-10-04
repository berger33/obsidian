---
id: software.seguranca.tranche06.000586
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

# Impacket: Enumeração MSRPC e Controle de Serviços (`rpcdump.py`, `samrdump.py`, `lookupsid.py`, `netview.py`, `reg.py` e `services.py`)

## Em uma frase
Os utilitários de inspeção MSRPC do Impacket permitem auditar quais interfaces RPC estão expostas em um servidor Windows (**`rpcdump.py`**), enumerar contas e grupos via protocolo SAMR (**`samrdump.py`**), resolver SIDs de domínio por força bruta de RID (**`lookupsid.py`**), consultar o Registro remotamente (**`reg.py`**) e gerenciar serviços Windows (**`services.py`**).

## Por que importa
Enquanto ferramentas baseadas em agentes exigem execução de código no host, `reg.py` (usando a interface `[MS-RRP]` *Remote Registry Protocol* em `\pipe\winreg`) e `services.py` (usando `[MS-SCMR]` em `\pipe\svcctl`) operam inteiramente por chamadas RPC nativas do Windows.

## Como funciona
O **`lookupsid.py`** conecta ao pipe `\pipe\lsarpc` (`[MS-LSAT]` *Local Security Authority Translation Methods*) e chama `LsarLookupSids2` iterando os RIDs sequenciais (`500`, `501`, `512`, `1000..15000`) concatenados ao SID do domínio para mapear todos os nomes de usuários, grupos e computadores existentes no AD.

## Exemplo
```bash
# Listar endpoints MSRPC expostos na porta 135 e enumerar SIDs/RIDs de usuarios do dominio ate o RID 2000
impacket-rpcdump @srv-app01.corp.internal | head -n 30
impacket-lookupsid -k -no-pass corp.internal/sec_auditor@dc01.corp.internal 2000
```

## Limites e trade-offs
No Windows 10/11 e Windows Server modernos, a política **Network access: Restrict clients allowed to make remote calls to SAM** (`RestrictRemoteSam`) restringe quem pode consultar o pipe `\pipe\samr` remotamente.

## Como verificar
Verifique com `impacket-samrdump` usando uma conta de usuário comum se o servidor aplica a restrição `STATUS_ACCESS_DENIED` nas chamadas remotas ao SAM.

## Conexões
- [[impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials]] — Veja também: Impacket: Retransmissão Multiprocolo com `ntlmrelayx.py` (SMB, LDAP/LDAPS, HTTP **AD CS ESC8**, *RBCD*, *Shadow Credentials* e SOCKS Proxy).
- [[impacket-cliente-mssqlclient-xp-cmdshell-linked-servers-trusted-links]] — Veja também: Impacket: Auditoria de Microsoft SQL Server com `mssqlclient.py` (Autenticação Windows/SQL, `enable_xp_cmdshell`, *Impersonation* `EXECUTE AS` e *Linked Servers*).
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec]] — Referência cruzada direta com impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec.
- [[netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks]] — Referência cruzada direta com netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
