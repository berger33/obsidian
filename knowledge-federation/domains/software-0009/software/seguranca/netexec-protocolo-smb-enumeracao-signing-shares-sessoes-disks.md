---
id: software.seguranca.tranche06.000592
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

# NetExec (`nxc smb`): Mapeamento de Sub-Redes SMB, Verificação de `signing:False` / `SMBv1:True`, Compartilhamentos (`--shares`) e Sessões (`--sessions`)

## Em uma frase
O módulo **`nxc smb`** é o ponto de partida de qualquer auditoria de rede interna Windows: mesmo **sem passar nenhuma credencial**, executar `nxc smb 10.10.20.0/24` identifica a versão e o build do Windows, o nome do host, o domínio Active Directory, se o servidor exige **SMB Signing (`signing:True` vs `signing:False`)** e se o protocolo obsoleto **SMBv1 (`SMBv1:True`)** ainda está ativo.

## Por que importa
Com credenciais de um usuário comum de domínio (ou testando *Null Session* `-u '' -p ''` e *Guest Logon* `-u 'guest' -p ''`), o `nxc smb` audita permissões de leitura/escrita em todos os compartilhamentos de rede (`--shares`), sessões de usuários conectadas (`--sessions`), usuários logados (`--loggedon-users`), discos (`--disks`) e a política de bloqueio de senhas do domínio (`--pass-pol`).

## Como funciona
Na saída padrão do NetExec, o marcador **`[+]`** confirma autenticação válida como usuário comum, enquanto **`(Pwn3d!)`** indica que a conta autenticada possui **privilégios de Administrador Local** naquela máquina específica.

## Exemplo
```bash
# Mapear hosts SMB na sub-rede, gerar lista de alvos sem SMB Signing e auditar compartilhamentos e politica de senhas
nxc smb 10.10.20.0/24 --gen-relay-list /cases/pentest/unsigned_smb_hosts.txt
nxc smb 10.10.20.0/24 -u 'sec_auditor' -p 'AuditPass!2026' --shares --pass-pol
```

## Limites e trade-offs
A flag **`--gen-relay-list <arquivo>`** filtra e salva automaticamente apenas os endereços IP cujo `signing:False`, gerando o arquivo de entrada pronto para auditoria com `impacket-ntlmrelayx -tf <arquivo>`.

## Como verificar
Sempre execute **`nxc smb <DC_IP> -u <user> -p <pass> --pass-pol`** antes de qualquer teste de credenciais para verificar o `Account Lockout Threshold` e a janela de `Reset Account Lockout Counter` do domínio.

## Conexões
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Veja também: NetExec (`nxc` & `nxcdb`): Arquitetura do Sucessor Open-Source do CrackMapExec, Protocolos Suportados e Isolamento por *Workspaces*.
- [[netexec-auditoria-credenciais-password-spraying-pass-the-hash-lockout]] — Veja também: NetExec: Auditoria de Reutilização de Credenciais Locais (*LAPS Audit*), *Pass-the-Hash* (`-H`) e *Password Spraying* Seguro (`--no-bruteforce` / `--continue-on-success`).
- [[responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay]] — Referência cruzada direta com responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
