---
id: software.seguranca.tranche06.000573
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
fontes: ["https://raw.githubusercontent.com/lgandx/Responder/master/README.md", "https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf", "https://github.com/lgandx/Responder"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Responder: Servidor Kerberos Integrado (`KerberosMode = CAPTURE` vs `FORCE_NTLM` via `KDC_ERR_ETYPE_NOSUPP`)

## Em uma frase
Versões modernas do Responder incluem um servidor **Kerberos (porta 88 TCP/UDP)** e suporte a autenticação Kerberos dentro de SPNEGO (SMB, HTTP, WinRM, MSSQL), configurável na diretiva **`KerberosMode`** do `Responder.conf` entre três modos: **`CAPTURE`**, **`FORCE_NTLM`** e **`BOTH`**.

## Por que importa
Em ambientes modernos onde clientes tentam usar Kerberos antes de NTLM, um servidor rogue que falhasse na negociação Kerberos perderia a autenticação; o modo `FORCE_NTLM` responde ao cliente com o erro Kerberos **`KDC_ERR_ETYPE_NOSUPP` (`error-code: 14`)**, forçando o cliente Windows a fazer **downgrade imediato para NTLMSSP (NetNTLMv2)** na mesma conexão.

## Como funciona
Já quando configurado em **`KerberosMode = CAPTURE`** (ou `BOTH`), se o cliente enviar uma requisição `AS-REQ` contendo o *pa-enc-timestamp* de pré-autenticação Kerberos na porta 88, o Responder extrai o material cifrado no formato **Hashcat `-m 7500`** (*Kerberos 5, etype 23/17/18, AS-REQ Pre-Auth*).

## Exemplo
```ini
# Trecho do Responder.conf configurando o comportamento do servidor Kerberos integrado
[Responder Core]
Kerberos = On
; CAPTURE = captura hashes AS-REQ Pre-Auth (Hashcat -m 7500)
; FORCE_NTLM = envia KDC_ERR_ETYPE_NOSUPP para forcar downgrade do cliente para NetNTLMv2 (-m 5600)
; BOTH = captura em AS-REQ na porta 88 e faz downgrade em SPNEGO (SMB/HTTP/WinRM)
KerberosMode = BOTH
```

## Limites e trade-offs
Para impedir que clientes Windows façam downgrade silencioso de Kerberos para NTLM ao falar com servidores corporativos, a Microsoft introduziu políticas de **Restrição de NTLM de Saída** (*Restrict NTLM: Outgoing NTLM traffic to remote servers*) e proteção de canal IAKerb/SPNEGO.

## Como verificar
Verifique nos logs de auditoria `Microsoft-Windows-Ntlm/Operational` (Event ID `8001` / `4004`) do Windows Server quais máquinas ainda realizam autenticações NTLM de saída.

## Conexões
- [[responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2]] — Veja também: Responder: Servidores de Autenticação *Rogue* Integrados (SMB, HTTP/HTTPS, LDAP, MSSQL, SMTP/IMAP, WinRM, RDP) e Captura **NetNTLMv1/v2**.
- [[responder-envenenamento-ipv6-dhcpv6-dns-takeover-wpad-mitigacao]] — Veja também: Responder: Auditoria de **DHCPv6 DNS Takeover** (`--dhcpv6`, `SendRA`) e Descoberta Automática de Proxy **WPAD** (`-w` / `-P`).
- [[impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden]] — Referência cruzada direta com impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
