---
id: software.seguranca.tranche06.000588
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

# Impacket: Inspeção de Compartilhamentos com `smbclient.py` e Servidor SMB Efêmero com `smbserver.py` (`-smb2support` e Autenticação)

## Em uma frase
Os scripts **`smbclient.py`** e **`smbserver.py`** fornecem um cliente interativo SMB1/SMB2/SMB3 e um servidor SMB standalone em Python para transferência de arquivos e testes de conectividade sem precisar instalar e configurar o daemon completo do Samba.

## Por que importa
Durante uma auditoria ou resposta a incidentes, `smbclient.py` permite navegar em compartilhamentos remotos (`shares`, `use <share>`, `ls`, `cd`, `get`, `put`, `info`, `who`) autenticando com ticket Kerberos ou hash NTLM.

## Como funciona
Já o **`smbserver.py`** expõe instantaneamente uma pasta local como compartilhamento SMB na rede; como versões modernas do Windows desabilitam o protocolo legado SMBv1 por completo, é obrigatório passar a flag **`-smb2support`** e definir credenciais explícitas (`-username <user> -password <pass>`) para compatibilidade com políticas do Windows 10/11/Server que bloqueiam acesso convidado não-autenticado (*Insecure Guest Logons*).

## Exemplo
```bash
# Iniciar um servidor SMB2/3 efemero autenticado para receber logs de triagem de uma estacao Windows
sudo impacket-smbserver -smb2support \
  -username collector -password "TempAuditPass!2026" \
  TRIAGE /cases/triage-incoming
```

## Limites e trade-offs
Nunca inicie `impacket-smbserver` expondo diretórios sensíveis da máquina do operador nem sem `-username`/`-password` em uma VLAN compartilhada, pois qualquer host da sub-rede poderia listar ou baixar os arquivos.

## Como verificar
Conecte a partir da máquina Windows de teste com `net use \\<IP>\TRIAGE /u:collector` e confirme o recebimento dos arquivos com suporte SMB2.

## Conexões
- [[impacket-cliente-mssqlclient-xp-cmdshell-linked-servers-trusted-links]] — Veja também: Impacket: Auditoria de Microsoft SQL Server com `mssqlclient.py` (Autenticação Windows/SQL, `enable_xp_cmdshell`, *Impersonation* `EXECUTE AS` e *Linked Servers*).
- [[impacket-gestao-contas-acl-addcomputer-dacledit-rbcd-laps-dpapi]] — Veja também: Impacket: Auditoria de Objetos de Diretório e Criptografia (`addcomputer.py`, `dacledit.py`, `rbcd.py`, `GetLAPSPassword.py` e **`dpapi.py`**).
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark]] — Referência cruzada direta com wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark.
- [[netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks]] — Referência cruzada direta com netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
