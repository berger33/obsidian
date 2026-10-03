---
id: software.seguranca.tranche06.000575
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

# Responder: Controle Estrito de Escopo em `Responder.conf` (`RespondTo`, `DontRespondTo`, `RespondToName`, `DontRespondToTLD` e `AutoIgnoreAfterSuccess`)

## Em uma frase
O arquivo de configuração **`Responder.conf`** contém diretivas fundamentais de segurança operacional para restringir exatamente **a quais IPs** e **a quais nomes consultados** o Responder tem permissão para responder durante um exercício autorizado.

## Por que importa
Rodar o Responder em modo ativo sem preencher `RespondTo` em uma rede de produção grande pode responder acidentalmente a sistemas industriais, servidores de banco de dados ou causar bloqueio de contas (*Account Lockout*) se um serviço automatizado tentar autenticar repetidamente e falhar.

## Como funciona
As diretivas de escopo incluem: **`RespondTo = 10.10.20.55`** (responde exclusivamente aos IPs/faixas listados), **`DontRespondTo`** (nunca responde aos IPs listados, como gateways e DCs), **`RespondToName`** / **`DontRespondToName = ISATAP, WPAD`** (filtra pelos prefixos de hostname consultados), **`DontRespondToTLD = _dosvc, local`** (ignora sufixos barulhentos como *Windows Delivery Optimization* `_dosvc`) e **`AutoIgnoreAfterSuccess = On`** (assim que captura um hash de um cliente IP, adiciona o IP automaticamente à lista de ignorados para que o cliente siga trabalhando normalmente sem interrupção).

## Exemplo
```ini
# Configuracao de seguranca operacional (OPSEC) no Responder.conf para testar apenas hosts especificos sem causar impacto
[Responder Core]
RespondTo = 10.10.20.50-10.10.20.55
DontRespondTo = 10.10.20.1, 10.10.20.10
DontRespondToName = ISATAP
DontRespondToTLD = _dosvc
AutoIgnoreAfterSuccess = On
CaptureMultipleCredentials = Off
```

## Limites e trade-offs
Habilitar **`AutoIgnoreAfterSuccess = On`** com **`CaptureMultipleCredentials = Off`** é uma excelente prática em pentests internos: na primeira tentativa de conexão o Responder captura 1 hash de evidência e imediatamente para de responder àquele cliente, permitindo que a segunda tentativa do Windows conecte de forma transparente ao recurso real.

## Como verificar
Verifique no console do Responder a mensagem `[*] Adding client <IP> to auto-ignore list` imediatamente após a primeira captura bem-sucedida.

## Conexões
- [[responder-envenenamento-ipv6-dhcpv6-dns-takeover-wpad-mitigacao]] — Veja também: Responder: Auditoria de **DHCPv6 DNS Takeover** (`--dhcpv6`, `SendRA`) e Descoberta Automática de Proxy **WPAD** (`-w` / `-P`).
- [[responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay]] — Veja também: Responder & `ntlmrelayx.py`: Desativação dos Servidores `SMB` e `HTTP` no `Responder.conf` para **NTLM Relay** em Tempo Real.
- [[responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva]] — Referência cruzada direta com responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva.
- [[responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2]] — Referência cruzada direta com responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2.
- [[bettercap-automacao-caplets-api-rest-tls-seguranca-operacional]] — Referência cruzada direta com bettercap-automacao-caplets-api-rest-tls-seguranca-operacional.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
