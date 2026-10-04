---
id: software.seguranca.tranche06.000589
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

# Impacket: Auditoria de Objetos de Diretório e Criptografia (`addcomputer.py`, `dacledit.py`, `rbcd.py`, `GetLAPSPassword.py` e **`dpapi.py`**)

## Em uma frase
Para auditar permissões de objetos no Active Directory e a criptografia de credenciais do Windows, o Impacket inclui **`addcomputer.py`**, **`dacledit.py`**, **`rbcd.py`**, **`GetLAPSPassword.py`** / **`laps.py`** e **`dpapi.py`**.

## Por que importa
Por padrão no Active Directory, o atributo **`ms-DS-MachineAccountQuota`** na raiz do domínio vale **`10`**, o que permite que qualquer usuário comum do domínio crie até 10 contas de computador no AD usando **`addcomputer.py`** (frequentemente combinadas com **`rbcd.py`** ou ataques de spoofing de SPN/certificados). Já o **`dacledit.py`** permite ler, fazer backup (`-action backup`), modificar e restaurar DACLs de objetos do AD para auditar ACEs perigosas (`GenericAll`, `WriteDacl`, `WriteOwner`).

## Como funciona
Por sua vez, o **`dpapi.py`** decifra offline ou remotamente segredos protegidos pela **Windows DPAPI** (*Data Protection API*: `masterkeys`, `credential` files, `vault` e a chave privada de backup do domínio `backupkeys`), demonstrando como uma chave de backup DPAPI do domínio permite decifrar qualquer MasterKey de usuário da floresta.

## Exemplo
```bash
# Fazer leitura e backup seguro da DACL de um objeto de teste no AD antes de auditar permissoes com dacledit.py
impacket-dacledit -k -no-pass -action read \
  -target-dn "CN=AppServer01,CN=Computers,DC=corp,DC=internal" \
  corp.internal/sec_auditor
```

## Limites e trade-offs
A recomendação de hardening imediata para qualquer domínio Active Directory é alterar o atributo **`ms-DS-MachineAccountQuota` para `0`** na raiz do domínio, impedindo que usuários sem privilégio administrativo criem contas de máquina arbitrárias via `addcomputer.py`.

## Como verificar
Consulte `ms-DS-MachineAccountQuota` no domínio e utilize `impacket-dacledit -action backup` sempre antes de testar qualquer alteração de ACL em laboratório.

## Conexões
- [[impacket-compartilhamentos-smbclient-smbserver-transferencia-segura-smb2]] — Veja também: Impacket: Inspeção de Compartilhamentos com `smbclient.py` e Servidor SMB Efêmero com `smbserver.py` (`-smb2support` e Autenticação).
- [[impacket-desenvolvimento-scripts-customizados-dcerpc-smbconnection-pytest]] — Veja também: Impacket: Desenvolvimento de Scripts de Auditoria em Python com `SMBConnection` e `DCERPCTransportFactory`, e Suíte de Testes `pytest` / `tox`.
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials]] — Referência cruzada direta com impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials.
- [[netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao]] — Referência cruzada direta com netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
