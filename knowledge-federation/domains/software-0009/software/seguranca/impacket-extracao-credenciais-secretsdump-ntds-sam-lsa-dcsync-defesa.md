---
id: software.seguranca.tranche06.000584
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

# Impacket: Auditoria de Extração de Credenciais com `secretsdump.py` (`SAM` / `LSA Secrets` Remotos, Parsing Offline de `NTDS.dit` e **`DCSync`** `DRSUAPI`)

## Em uma frase
O script **`secretsdump.py`** do Impacket realiza a extração de hashes de contas locais (`SAM`), segredos de serviços e credenciais de domínio em cache (`SECURITY` / `LSA Secrets` / `NL$KM`) e hashes do Active Directory (`NTDS.dit`), operando tanto **remotamente pela rede** (sem executar nenhum agente binário na memória do alvo) quanto **offline** sobre arquivos de colmeia salvos localmente.

## Por que importa
Demonstra o risco crítico do privilégio de replicação de diretório (**`DCSync`**): qualquer conta que possua as permissões estendidas de controle de acesso `DS-Replication-Get-Changes` (`1131f6aa-9c07-11d1-f79f-00c04fc2dcd2`) e `DS-Replication-Get-Changes-All` (`1131f6ad-9c07-11d1-f79f-00c04fc2dcd2`) na raiz do domínio pode chamar os métodos RPC **`DsGetNCChanges`** (`MS-DRSR` / `DRSUAPI`) simulando ser um Domain Controller e receber os hashes NTLM e chaves Kerberos de qualquer usuário (incluindo `krbtgt`).

## Como funciona
Quando executado contra arquivos salvos localmente (`-sam sam.save -system system.save -ntds ntds.dit`), o `secretsdump.py` decifra a *BootKey* da colmeia `SYSTEM` e a *PEK* (*Password Encryption Key*) do `NTDS.dit` puramente em Python.

## Exemplo
```bash
# Auditar uma unica conta especifica via DRSUAPI (-just-dc-user) ou fazer parsing offline de hives coletadas
impacket-secretsdump -k -no-pass -just-dc-user "CORP/svc_backup_test" \
  corp.internal/sec_auditor@dc01.corp.internal

impacket-secretsdump -sam /cases/hives/SAM -system /cases/hives/SYSTEM -security /cases/hives/SECURITY LOCAL
```

## Limites e trade-offs
Em um teste autorizado em um domínio grande com dezenas de milhares de objetos, **jamais** rode `secretsdump.py` contra um Domain Controller sem a flag **`-just-dc-user <CONTA_DE_TESTE>`**: extrair o `NTDS.dit` inteiro gera alto tráfego RPC e deixa milhares de hashes sensíveis em disco.

## Como verificar
Audite as ACLs da raiz do objeto Domain no Active Directory (via BloodHound ou PowerShell) garantindo que apenas o grupo `Domain Controllers` e `Enterprise Domain Controllers` possuam `DS-Replication-Get-Changes-All`.

## Conexões
- [[impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec]] — Veja também: Impacket: Comparação Forense e de OPSEC dos 5 Métodos de Execução Remota (`psexec.py`, `smbexec.py`, `wmiexec.py`, `atexec.py` e `dcomexec.py`).
- [[impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials]] — Veja também: Impacket: Retransmissão Multiprocolo com `ntlmrelayx.py` (SMB, LDAP/LDAPS, HTTP **AD CS ESC8**, *RBCD*, *Shadow Credentials* e SOCKS Proxy).
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc]] — Referência cruzada direta com wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc.
- [[volatility3-registro-windows-memoria-hivelist-printkey-userassist-hashdump]] — Referência cruzada direta com volatility3-registro-windows-memoria-hivelist-printkey-userassist-hashdump.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
