---
id: software.seguranca.tranche06.000581
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

# Fortra Impacket: Arquitetura da Biblioteca Python de Protocolos de Rede (`ImpactPacket`, `SMBConnection`, `DCERPC v5`, `Kerberos` e `LDAP`)

## Em uma frase
**Impacket** (`fortra/impacket`, originalmente criada pela Core Security e mantida pela Fortra) é a coleção de classes Python que implementa do zero a construção e o parsing byte a byte de protocolos de rede de baixo nível (Ethernet, IPv4/IPv6, TCP, UDP, ICMP, ARP) e toda a pilha de protocolos corporativos da Microsoft (**NMB/SMB1-3**, **MSRPC v5**, **NTLMSSP**, **Kerberos v5**, **LDAP** e **TDS/MSSQL**).

## Por que importa
É o alicerce programático sobre o qual quase todas as ferramentas modernas de auditoria de Active Directory (incluindo o próprio NetExec, BloodHound.py e Certipy) são construídas, além de fornecer mais de 60 scripts oficiais de exemplo (`examples/*.py`, instalados como `impacket-<nome>`).

## Como funciona
Todos os módulos de aplicação do Impacket compartilham uma interface uniforme de autenticação que aceita transparentemente: **senha em texto claro** (`DOMINIO/usuario:senha@alvo`), **Pass-the-Hash NTLM** (`-hashes LMHASH:NTHASH`), **Pass-the-Ticket Kerberos** (`-k -no-pass` lendo o arquivo `.ccache` apontado pela variável de ambiente `KRB5CCNAME`) ou **chave Kerberos AES-128/AES-256** (`-aesKey <hex>`).

## Exemplo
```bash
# Exemplo de autenticacao via Kerberos Ticket (KRB5CCNAME) sem enviar senha nem hash NTLM pela rede
export KRB5CCNAME=/cases/pentest/auditor_admin.ccache
impacket-smbclient -k -no-pass corp.internal/sec_auditor@filesrv01.corp.internal
```

## Limites e trade-offs
Ao realizar auditorias em ambientes monitorados por EDR/SIEM, preferir autenticação Kerberos com **`-k -no-pass`** ou **`-aesKey`** sobre FQDN (nunca endereço IP numérico, pois o Kerberos exige o SPN com o FQDN do host) evita gerar eventos de logon NTLM (`4624` com `AuthenticationPackageName = NTLM`).

## Como verificar
Execute `pytest -m "not remote"` na árvore de código do Impacket para validar localmente os parsers e serializadores de pacotes sem precisar de um Domain Controller ativo.

## Conexões
- [[impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden]] — Veja também: Impacket: Auditoria de Protocolo Kerberos (`GetNPUsers.py` AS-REP Roasting, `GetUserSPNs.py` Kerberoasting, `getTGT.py`, `getST.py` e `ticketer.py`).
- [[impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec]] — Referência cruzada direta com impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec.
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Referência cruzada direta com netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
