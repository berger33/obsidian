---
id: software.seguranca.tranche06.000595
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

# NetExec: Operação 100% Kerberos (`-k`, `--use-kcache`, `--aesKey` e `--kdcHost`) em Redes com NTLM Restrito

## Em uma frase
Todos os protocolos Windows do NetExec (`smb`, `ldap`, `winrm`, `wmi`, `mssql`, `rdp`) suportam autenticação **100% Kerberos** através das flags **`-k`**, **`--use-kcache`** (que reutiliza o ticket TGT/TGS armazenado no arquivo apontado por `KRB5CCNAME`), **`--aesKey <chave_aes>`** e **`--kdcHost <fqdn_do_dc>`**.

## Por que importa
Em ambientes corporativos modernos que desabilitaram NTLM via GPO (*Restrict NTLM*) ou onde o SOC monitora qualquer autenticação NTLM na rede, operar com `--use-kcache` ou `--aesKey` garante compatibilidade total com Kerberos AES-256.

## Como funciona
Lembre-se de que o protocolo Kerberos constrói o *Service Principal Name* (ex.: `cifs/filesrv01.corp.internal`) a partir do alvo informado na linha de comando: portanto, ao usar `-k` no NetExec, **passe sempre o FQDN (hostname completo) do servidor alvo** (e não o endereço IP numérico) e aponte `--kdcHost` para o FQDN do Domain Controller.

## Exemplo
```bash
# Solicitar TGT com getTGT ou usar --use-kcache diretamente no NetExec contra o FQDN do servidor alvo
export KRB5CCNAME=/cases/pentest/sec_auditor.ccache
nxc smb filesrv01.corp.internal -k --use-kcache --kdcHost dc01.corp.internal --shares
```

## Limites e trade-offs
Se a máquina de auditoria Linux não estiver usando o DNS interno do Active Directory em `/etc/resolv.conf`, adicione os FQDNs do Domain Controller e dos servidores alvo em `/etc/hosts` ou use `--dns-server <DC_IP>` quando suportado.

## Como verificar
Verifique no Wireshark (`kerberos && !ntlmssp`) durante a execução de `nxc smb ... -k --use-kcache` que toda a negociação SPNEGO ocorre via tickets Kerberos AP-REQ sem fallback para NTLM.

## Conexões
- [[netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao]] — Veja também: NetExec (`nxc ldap`): Auditoria de Active Directory via LDAP/LDAPS (`--kerberoasting`, `--asreproast`, `--trusted-for-delegation`, `--gmsa` e `--bloodhound`).
- [[netexec-protocolos-winrm-wmi-execucao-remota-powershell-dpapi]] — Veja também: NetExec (`nxc winrm` & `nxc wmi`): Auditoria de Gerenciamento Remoto Windows (WS-Management Portas `5985`/`5986` e WMI) e Execução (`-x` / `-X`).
- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — Referência cruzada direta com netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces.
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc]] — Referência cruzada direta com wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc.

## Fontes
- [NetExec Official GitHub — The Network Execution Tool (nxc & nxcdb)](https://raw.githubusercontent.com/Pennyw0rth/NetExec/main/README.md) — documentação oficial do NetExec cobrindo protocolos suportados, instalação via pipx e banco nxcdb; consultado em 2026-10-03.
- [NetExec Official Wiki — Getting Started & Protocol Usage](https://www.netexec.wiki/getting-started/installation) — wiki oficial do NetExec cobrindo instalação, autenticação Kerberos/NTLM, módulos e operação; consultado em 2026-10-03.
- [NetExec Official Repository](https://github.com/Pennyw0rth/NetExec) — repositório oficial do projeto NetExec; consultado em 2026-10-03.
