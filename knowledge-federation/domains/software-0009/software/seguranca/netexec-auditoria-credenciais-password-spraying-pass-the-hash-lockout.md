---
id: software.seguranca.tranche06.000593
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

# NetExec: Auditoria de Reutilização de Credenciais Locais (*LAPS Audit*), *Pass-the-Hash* (`-H`) e *Password Spraying* Seguro (`--no-bruteforce` / `--continue-on-success`)

## Em uma frase
O NetExec permite auditar em segundos um dos problemas mais críticos em redes corporativas Windows: a **reutilização da mesma senha/hash NTLM de Administrador Local** (`RID 500`) em centenas de estações de trabalho e servidores quando o **LAPS** (*Local Administrator Password Solution*) não está implantado.

## Por que importa
Ao passar **`--local-auth`** junto ao hash NTLM da conta local (`-u Administrator -H <NTHASH> --local-auth`), o NetExec testa se o mesmo hash autentica localmente nas demais máquinas da sub-rede, demonstrando o impacto de movimentação lateral caso uma única estação seja comprometida.

## Como funciona
Para auditoria de senhas fracas de domínio (*Password Spraying*), combinar uma lista de usuários (`-u users.txt`) com uma única senha candidata por janela de bloqueio (`-p 'Outono2026!' --no-bruteforce --continue-on-success`) testa 1 tentativa por conta e continua listando todas as contas que utilizam aquela senha padrão.

## Exemplo
```bash
# Auditar reutilizacao do hash de Administrador Local (RID 500) na sub-rede usando Pass-the-Hash (--local-auth)
nxc smb 10.10.20.0/24 -u Administrator -H e19ccf75ee54e06b06a5907af13cef42 --local-auth --continue-on-success
```

## Limites e trade-offs
Ao passar uma lista de usuários e uma lista de senhas (`-u users.txt -p passwords.txt`), inclua `--no-bruteforce` se quiser pareamento `1:1` (linha N do usuário com linha N da senha) ou use apenas **uma única senha por rodada** respeitando o `Lockout Observation Window` retornado por `--pass-pol` para jamais bloquear contas de usuários em produção.

## Como verificar
Confirme que após implantar o **Windows LAPS**, o teste com `--local-auth` usando a credencial local da Máquina A falha em 100% das demais máquinas da sub-rede.

## Conexões
- [[netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks]] — Veja também: NetExec (`nxc smb`): Mapeamento de Sub-Redes SMB, Verificação de `signing:False` / `SMBv1:True`, Compartilhamentos (`--shares`) e Sessões (`--sessions`).
- [[netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao]] — Veja também: NetExec (`nxc ldap`): Auditoria de Active Directory via LDAP/LDAPS (`--kerberoasting`, `--asreproast`, `--trusted-for-delegation`, `--gmsa` e `--bloodhound`).
- [[netexec-autenticacao-kerberos-ccache-aeskey-kdchost-opsec]] — Referência cruzada direta com netexec-autenticacao-kerberos-ccache-aeskey-kdchost-opsec.
- [[impacket-gestao-contas-acl-addcomputer-dacledit-rbcd-laps-dpapi]] — Referência cruzada direta com impacket-gestao-contas-acl-addcomputer-dacledit-rbcd-laps-dpapi.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
