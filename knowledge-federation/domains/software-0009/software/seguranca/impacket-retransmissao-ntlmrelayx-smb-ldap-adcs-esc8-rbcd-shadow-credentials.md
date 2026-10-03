---
id: software.seguranca.tranche06.000585
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

# Impacket: Retransmissão Multiprocolo com `ntlmrelayx.py` (SMB, LDAP/LDAPS, HTTP **AD CS ESC8**, *RBCD*, *Shadow Credentials* e SOCKS Proxy)

## Em uma frase
O **`ntlmrelayx.py`** é o servidor de retransmissão NTLM multiprocolo do Impacket: ele escuta conexões de entrada (SMB, HTTP/HTTPS, WCF, RAW) e retransmite a autenticação NTLMSSP do cliente vítima em tempo real para servidores alvo (SMB, LDAP/LDAPS, MSSQL, HTTP/HTTPS, IMAP, RPC) ou mantém as sessões autenticadas abertas em um **proxy SOCKS** local (`-socks`).

## Por que importa
Permite demonstrar cadeias completas de escalação de privilégio em Active Directory quando *SMB Signing*, *LDAP Signing*, *LDAP Channel Binding (CBT)* ou *Extended Protection for Authentication (EPA)* estão ausentes:

## Como funciona
**(1) Relay para HTTP de Autoridade Certificadora AD CS (`ESC8`)**: retransmite a autenticação NTLM de uma máquina ou usuário para `http://<ca-server>/certsrv/certfnsh.asp` (`--adcs --template DomainController`), emitindo um certificado X.509 válido para autenticação Kerberos PKINIT; **(2) Relay para LDAP/LDAPS**: adiciona uma conta de computador controlada pelo auditor no atributo `msDS-AllowedToActOnBehalfOfOtherIdentity` do alvo (`--delegate-access`, **RBCD**) ou injeta uma chave pública no atributo `msDS-KeyCredentialLink` (**Shadow Credentials**); e **(3) Modo `-socks`**: mantém a sessão SMB/MSSQL/LDAP viva na porta `1080/TCP` para uso interativo com `proxychains4`.

## Exemplo
```bash
# Iniciar ntlmrelayx em modo SOCKS (-socks) com suporte a SMB2 apontando para lista de hosts sem SMB Signing
impacket-ntlmrelayx -tf /cases/pentest/unsigned_smb_targets.txt -smb2support -socks
```

## Limites e trade-offs
Para mitigar completamente ataques de `ntlmrelayx` contra LDAP/LDAPS e AD CS Web Enrollment (`ESC8`), habilite **LDAP Server Signing Requirements = Require signature**, **LDAP Channel Binding = Always** (`LdapEnforceChannelBinding = 2`) e **Extended Protection for Authentication (EPA) = Required** com HTTPS obrigatório no IIS do AD CS.

## Como verificar
Consulte o comando `socks` dentro do console interativo do `ntlmrelayx` para ver as sessões ativas e confirme que servidores endurecidos com *Signing + EPA/CBT* rejeitam a tentativa de relay.

## Conexões
- [[impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa]] — Veja também: Impacket: Auditoria de Extração de Credenciais com `secretsdump.py` (`SAM` / `LSA Secrets` Remotos, Parsing Offline de `NTDS.dit` e **`DCSync`** `DRSUAPI`).
- [[impacket-enumeracao-msrpc-rpcdump-samrdump-lookupsid-netview-services]] — Veja também: Impacket: Enumeração MSRPC e Controle de Serviços (`rpcdump.py`, `samrdump.py`, `lookupsid.py`, `netview.py`, `reg.py` e `services.py`).
- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Referência cruzada direta com impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos.
- [[responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay]] — Referência cruzada direta com responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay.
- [[responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing]] — Referência cruzada direta com responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing.

## Fontes
- [Fortra Impacket Official GitHub — Network Protocols & Examples Overview](https://raw.githubusercontent.com/fortra/impacket/master/README.md) — documentação oficial do Fortra Impacket cobrindo protocolos SMB1-3, MSRPC, Kerberos, LDAP, TDS e utilitários; consultado em 2026-10-03.
- [Fortra Impacket Official Testing Guide — TESTING.md & AD Lab Setup](https://raw.githubusercontent.com/fortra/impacket/master/TESTING.md) — guia oficial de testes locais/remotos (pytest, tox) e configuração de laboratório Active Directory e LDAPS; consultado em 2026-10-03.
- [Fortra Impacket Official Repository](https://github.com/fortra/impacket) — repositório oficial da biblioteca Impacket; consultado em 2026-10-03.
