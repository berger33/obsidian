---
id: software.seguranca.tranche06.000594
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

# NetExec (`nxc ldap`): Auditoria de Active Directory via LDAP/LDAPS (`--kerberoasting`, `--asreproast`, `--trusted-for-delegation`, `--gmsa` e `--bloodhound`)

## Em uma frase
O módulo **`nxc ldap`** concentra as auditorias de configuração do diretório Active Directory em um único comando: detecção de *AS-REP Roasting* (`--asreproast`), *Kerberoasting* (`--kerberoasting`), delegação Kerberos irrestrita/restrita (`--trusted-for-delegation`), leitura de `ms-DS-MachineAccountQuota` (`-M maq`), senhas LAPS/gMSA (`--gmsa`) e coleta completa de grafos para o **BloodHound (`--bloodhound`)**.

## Por que importa
Em vez de instalar coletores pesados em estações Windows, o `nxc ldap` integra o coletor Python do BloodHound diretamente (`--bloodhound -c All --dns-server <DC_IP>`), gerando o arquivo `.zip` com todas as relações de grupos, sessões, trusts, OUs, GPOs e ACLs pronto para importação no BloodHound CE.

## Como funciona
Além disso, `nxc ldap <DC_IP>` sem credenciais verifica imediatamente se o Domain Controller exige **LDAP Signing** e **LDAPS Channel Binding**, duas proteções essenciais contra ataques de `ntlmrelayx`.

## Exemplo
```bash
# Auditar exigencia de LDAP Signing/Channel Binding, extrair contas Kerberoastable e coletar dados para o BloodHound
nxc ldap dc01.corp.internal -k --use-kcache \
  --kerberoasting /cases/pentest/kerberoast_hashes.txt \
  --asreproast /cases/pentest/asrep_hashes.txt \
  --trusted-for-delegation

nxc ldap dc01.corp.internal -k --use-kcache --bloodhound -c All --dns-server 10.10.10.5
```

## Limites e trade-offs
Sempre verifique no cabeçalho de saída de `nxc ldap <DC>` os indicadores **`signing:True`** e **`channel binding:True`**; caso apareça `signing:False` ou `channel binding:Never`, o Domain Controller está vulnerável a *NTLM Relay* para LDAP/LDAPS.

## Como verificar
Importe os arquivos JSON/ZIP gerados por `--bloodhound` no BloodHound Community Edition para auditar os caminhos de ataque até `Domain Admins` / `Tier 0`.

## Conexões
- [[netexec-auditoria-credenciais-password-spraying-pass-the-hash-lockout]] — Veja também: NetExec: Auditoria de Reutilização de Credenciais Locais (*LAPS Audit*), *Pass-the-Hash* (`-H`) e *Password Spraying* Seguro (`--no-bruteforce` / `--continue-on-success`).
- [[netexec-autenticacao-kerberos-ccache-aeskey-kdchost-opsec]] — Veja também: NetExec: Operação 100% Kerberos (`-k`, `--use-kcache`, `--aesKey` e `--kdcHost`) em Redes com NTLM Restrito.
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Referência cruzada direta com netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces.
- [[impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden]] — Referência cruzada direta com impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden.
- [[impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials]] — Referência cruzada direta com impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
