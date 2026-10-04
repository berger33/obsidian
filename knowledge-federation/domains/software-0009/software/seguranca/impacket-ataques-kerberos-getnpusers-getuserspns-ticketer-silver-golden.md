---
id: software.seguranca.tranche06.000582
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

# Impacket: Auditoria de Protocolo Kerberos (`GetNPUsers.py` AS-REP Roasting, `GetUserSPNs.py` Kerberoasting, `getTGT.py`, `getST.py` e `ticketer.py`)

## Em uma frase
A suíte de exemplos Kerberos do Impacket audita falhas de configuração em contas de Active Directory e chaves de serviço: **`GetNPUsers.py`**, **`GetUserSPNs.py`**, **`getTGT.py`**, **`getST.py`**, **`ticketer.py`** e **`ticketConverter.py`**.

## Por que importa
Se uma conta de usuário tiver a flag `UF_DONT_REQUIRE_PREAUTH` (*Do not require Kerberos preauthentication*) habilitada, qualquer pessoa pode solicitar um `AS-REP` para essa conta via **`GetNPUsers.py`** (mesmo sem credenciais prévias se tiver uma lista de usuários) e quebrar a senha offline (**AS-REP Roasting**, Hashcat `-m 18200`). Já qualquer usuário autenticado pode usar **`GetUserSPNs.py -request`** para solicitar tickets de serviço (`TGS`) de contas de usuário que possuam `servicePrincipalName` (SPN) cadastrado (**Kerberoasting**, Hashcat `-m 13100` para RC4 ou `-m 19700` para AES-256).

## Como funciona
Complementarmente, **`getTGT.py`** solicita um Ticket-Granting Ticket e salva em `.ccache`, **`getST.py -impersonate <admin> -spn <cifs/alvo>`** exercita delegação Kerberos (*Constrained Delegation* `S4U2Self` + `S4U2Proxy` e *Resource-Based Constrained Delegation — RBCD*), e **`ticketer.py`** constrói tickets *Silver* ou *Golden* em laboratório para validar detecções de SIEM.

## Exemplo
```bash
# Auditar o dominio em busca de contas com Kerberos Pre-Auth desabilitado (AS-REP) e contas de servico (Kerberoasting)
impacket-GetNPUsers corp.internal/sec_auditor -k -no-pass -dc-ip 10.10.10.5 -request -format hashcat
impacket-GetUserSPNs corp.internal/sec_auditor -k -no-pass -dc-ip 10.10.10.5 -request -outputfile /tmp/tgs_audit.txt
```

## Limites e trade-offs
Para mitigar **Kerberoasting**, migre contas de serviço tradicionais com SPN para **Group Managed Service Accounts (gMSA)** (senhas aleatórias de 120 caracteres trocadas automaticamente pelo AD a cada 30 dias) e desabilite `RC4_HMAC_MD5` nas contas de serviço exigindo exclusivamente `AES128` / `AES256`.

## Como verificar
Verifique na saída de `impacket-GetNPUsers` que zero contas do domínio possuem `UF_DONT_REQUIRE_PREAUTH` e que todos os tickets retornados por `GetUserSPNs` usam `etype 18` (AES-256) com senhas longas/gMSA.

## Conexões
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Veja também: Fortra Impacket: Arquitetura da Biblioteca Python de Protocolos de Rede (`ImpactPacket`, `SMBConnection`, `DCERPC v5`, `Kerberos` e `LDAP`).
- [[impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec]] — Veja também: Impacket: Comparação Forense e de OPSEC dos 5 Métodos de Execução Remota (`psexec.py`, `smbexec.py`, `wmiexec.py`, `atexec.py` e `dcomexec.py`).
- [[responder-captura-kerberos-asrep-roasting-force-ntlm-downgrade]] — Referência cruzada direta com responder-captura-kerberos-asrep-roasting-force-ntlm-downgrade.
- [[netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao]] — Referência cruzada direta com netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
