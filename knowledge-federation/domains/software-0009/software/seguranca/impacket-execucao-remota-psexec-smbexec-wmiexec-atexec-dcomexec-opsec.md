---
id: software.seguranca.tranche06.000583
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

# Impacket: Comparação Forense e de OPSEC dos 5 Métodos de Execução Remota (`psexec.py`, `smbexec.py`, `wmiexec.py`, `atexec.py` e `dcomexec.py`)

## Em uma frase
O Impacket fornece cinco implementações distintas de execução remota de comandos para administradores de domínio, cada uma usando um transporte MSRPC diferente e deixando **artefatos forenses completamente diferentes** no Windows alvo: **`psexec.py`**, **`smbexec.py`**, **`wmiexec.py`**, **`atexec.py`** e **`dcomexec.py`**.

## Por que importa
Entender a mecânica exata de cada script é essencial tanto para o Red Team (evitar deixar binários em disco capturados pelo antivírus) quanto para o Blue Team / DFIR (saber qual Event ID e qual processo pai procurar no Timesketch/Velociraptor).

## Como funciona
**(1) `psexec.py`** faz upload de um binário executável de serviço com nome aleatório de 8 letras (`[A-Za-z]{8}.exe`) para `ADMIN$\` e cria/inicia um serviço Windows via `\pipe\svcctl` (muito barulhento: grava PE em disco e gera Event ID `7045`/`4697`); **(2) `smbexec.py`** não envia binário PE, mas cria um serviço temporário que executa `%COMSPEC% /Q /c echo <cmd> ^> \\127.0.0.1\C$\__output 2^>^&1 > %TEMP%\execute.bat & ...`; **(3) `wmiexec.py`** invoca `Win32_Process.Create` sobre **DCOM/WMI** (porta 135 + porta alta RPC), gerando comandos filhos do processo **`WmiPrvSE.exe`** e gravando a saída em `ADMIN$\__<timestamp>` (ou sem tocar SMB com `-nooutput`); **(4) `atexec.py`** cria uma tarefa agendada efêmera via `\pipe\atsvc` (`ITaskSchedulerService`, Event ID `4698`); e **(5) `dcomexec.py`** abusa de métodos COM expostos (`MMC20.Application`, `ShellWindows`, `ShellBrowserWindow`).

## Exemplo
```bash
# Executar comando pontual de auditoria via WMI sem criar servicos Windows (processo pai no alvo: WmiPrvSE.exe)
impacket-wmiexec -k -no-pass corp.internal/sec_auditor@srv-app01.corp.internal "whoami /all"
```

## Limites e trade-offs
Em investigações DFIR, processos `cmd.exe /Q /c ... 1> \\127.0.0.1\ADMIN$\__17... 2>&1` cujo processo pai é **`WmiPrvSE.exe`** são a assinatura clássica de `impacket-wmiexec` padrão.

## Como verificar
Crie regras Sigma no SIEM/Velociraptor monitorando processos filhos de `WmiPrvSE.exe`, `mmc.exe` (`dcomexec`), `svchost.exe -k netsvcs -s Schedule` (`atexec`) e criação de serviços em `%COMSPEC%` (`smbexec`).

## Conexões
- [[impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden]] — Veja também: Impacket: Auditoria de Protocolo Kerberos (`GetNPUsers.py` AS-REP Roasting, `GetUserSPNs.py` Kerberoasting, `getTGT.py`, `getST.py` e `ticketer.py`).
- [[impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa]] — Veja também: Impacket: Auditoria de Extração de Credenciais com `secretsdump.py` (`SAM` / `LSA Secrets` Remotos, Parsing Offline de `NTDS.dit` e **`DCSync`** `DRSUAPI`).
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[timesketch-deteccao-ameacas-regras-sigma-tsctl-sigma-analyzer]] — Referência cruzada direta com timesketch-deteccao-ameacas-regras-sigma-tsctl-sigma-analyzer.
- [[wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc]] — Referência cruzada direta com wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
