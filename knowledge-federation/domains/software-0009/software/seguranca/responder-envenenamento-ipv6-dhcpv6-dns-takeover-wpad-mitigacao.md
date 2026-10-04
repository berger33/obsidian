---
id: software.seguranca.tranche06.000574
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

# Responder: Auditoria de **DHCPv6 DNS Takeover** (`--dhcpv6`, `SendRA`) e Descoberta Automática de Proxy **WPAD** (`-w` / `-P`)

## Em uma frase
Mesmo em redes corporativas que operam oficialmente apenas em IPv4, todas as versões modernas do Windows têm a pilha **IPv6 habilitada e preferencial sobre o IPv4 por padrão**; o módulo **`--dhcpv6`** do Responder audita se os switches permitem que um host na VLAN responda a solicitações `DHCPv6 Solicit` / `Router Advertisement` (`SendRA = On`) se declarando como o servidor DNS IPv6 da sub-rede.

## Por que importa
Quando o Windows recebe uma configuração de DNS via DHCPv6 na VLAN local, ele passa a enviar consultas DNS legítimas primeiro para o DNS IPv6 recém-anunciado. Combinado com o protocolo **WPAD** (*Web Proxy Auto-Discovery*, onde o Windows e navegadores procuram automaticamente por `http://wpad.<dominio>/wpad.dat`), um servidor WPAD rogue pode servir um arquivo `wpad.dat` e exigir autenticação HTTP/Proxy (`-P`), capturando credenciais sem que o usuário digite nada errado.

## Como funciona
A opção `-w` inicia o servidor WPAD rogue, `-d` habilita respostas a consultas DHCP de domínio e `-P` força autenticação NTLM/Basic na recuperação do script `wpad.dat`.

## Exemplo
```ini
# Configuracao da secao [DHCPv6] no Responder.conf para auditoria de RA Guard e DHCPv6 Shield
[DHCPv6]
DHCPv6_Domain = internal.corp
SendRA = On
ROUTER_LIFETIME = 300
RDNSS_LIFETIME = 300
DNS_TTL = 60
RespondToRequests = True
```

## Limites e trade-offs
O teste com `--dhcpv6` e `SendRA = On` afeta o roteamento/DNS IPv6 da VLAN se os switches não tiverem **IPv6 RA Guard** e **DHCPv6 Shield / Guard** configurados; execute **sempre** com filtro estrito de IP/MAC em `RespondTo` de uma única máquina de teste.

## Como verificar
Confirme nos switches de acesso que portas de estações têm `ipv6 nd raguard` e `ipv6 dhcp guard` ativos e que o serviço Windows `WinHttpAutoProxySvc` (WPAD) está desabilitado via GPO.

## Conexões
- [[responder-captura-kerberos-asrep-roasting-force-ntlm-downgrade]] — Veja também: Responder: Servidor Kerberos Integrado (`KerberosMode = CAPTURE` vs `FORCE_NTLM` via `KDC_ERR_ETYPE_NOSUPP`).
- [[responder-escopo-responder-conf-respondto-dontrespondto-autoignore]] — Veja também: Responder: Controle Estrito de Escopo em `Responder.conf` (`RespondTo`, `DontRespondTo`, `RespondToName`, `DontRespondToTLD` e `AutoIgnoreAfterSuccess`).
- [[responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva]] — Referência cruzada direta com responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva.
- [[responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing]] — Referência cruzada direta com responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
