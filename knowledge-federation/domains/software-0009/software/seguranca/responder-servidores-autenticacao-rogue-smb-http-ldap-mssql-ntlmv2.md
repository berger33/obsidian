---
id: software.seguranca.tranche06.000572
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

# Responder: Servidores de Autenticação *Rogue* Integrados (SMB, HTTP/HTTPS, LDAP, MSSQL, SMTP/IMAP, WinRM, RDP) e Captura **NetNTLMv1/v2**

## Em uma frase
Quando executado em modo ativo (em um pentest autorizado e dentro de um escopo controlado em `Responder.conf`), o Responder responde às consultas LLMNR/NBT-NS/mDNS direcionando o cliente para si mesmo e sobe simultaneamente **mais de 17 servidores de autenticação integrados** para capturar o desafio-resposta (`Challenge/Response`) da conexão subsequente.

## Por que importa
Quando uma estação Windows resolve um nome via LLMNR apontando para o IP do Responder e tenta abrir um compartilhamento (`SMB` porta 445), uma página web/WebDAV (`HTTP/HTTPS` 80/443), um banco (`MSSQL` 1433) ou diretório (`LDAP` 389), o Windows tenta autenticar automaticamente enviando o hash **NetNTLMv2** (ou NetNTLMv1) do usuário logado usando o `Challenge` de 8 bytes definido em `Responder.conf`.

## Como funciona
Todos os hashes capturados são salvos no banco SQLite **`Responder.db`** e em arquivos de texto dedicados dentro de `logs/` já no formato exato de entrada do **Hashcat** (`-m 5600` para NetNTLMv2 e `-m 5500` para NetNTLMv1) e do John the Ripper, evitando recapturas repetidas da mesma conta na mesma sessão.

## Exemplo
```bash
# Inspecionar os hashes NetNTLMv2 capturados em uma sessao autorizada de pentest para auditoria de forca de senha
sqlite3 /opt/Responder/Responder.db "SELECT timestamp, client, module, type, user FROM responder;"
```

## Limites e trade-offs
O hash **NetNTLMv2** capturado pelo Responder **não** pode ser usado diretamente para *Pass-the-Hash* (pois inclui um HMAC-MD5 salgado com o `Challenge` aleatório e dados da sessão), mas permite **1)** quebra offline de senhas fracas em GPU (`hashcat -m 5600`) ou **2)** *NTLM Relay* em tempo real caso o alvo não exija *SMB/LDAP Signing*.

## Como verificar
Cruze as contas capturadas em `Responder.db` com a política de complexidade de senhas do Active Directory para demonstrar o impacto de senhas fracas combinadas com LLMNR ativo.

## Conexões
- [[responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva]] — Veja também: Responder: Arquitetura de Resolução de Nomes Multicast/Broadcast (**LLMNR** UDP 5355, **NBT-NS** UDP 137 e **mDNS** UDP 5353) e Modo Passivo (`-A`).
- [[responder-captura-kerberos-asrep-roasting-force-ntlm-downgrade]] — Veja também: Responder: Servidor Kerberos Integrado (`KerberosMode = CAPTURE` vs `FORCE_NTLM` via `KDC_ERR_ETYPE_NOSUPP`).
- [[responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing]] — Referência cruzada direta com responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
