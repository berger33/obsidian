---
id: software.seguranca.tranche06.000576
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

# Responder & `ntlmrelayx.py`: Desativação dos Servidores `SMB` e `HTTP` no `Responder.conf` para **NTLM Relay** em Tempo Real

## Em uma frase
Quando o objetivo de um exercício de Red Team não é apenas capturar hashes NetNTLMv2 para quebra offline, mas sim **retransmitir (*Relay*) a autenticação NTLM em tempo real** para outra máquina que não exige assinatura SMB/LDAP (usando `impacket-ntlmrelayx` ou a ferramenta `MultiRelay.py` do próprio Responder), os servidores **`SMB`** e **`HTTP`** do `Responder.conf` devem ser mudados para **`Off`**.

## Por que importa
O Responder atua apenas como o **envenenador de nomes** (respondendo às consultas LLMNR/NBT-NS/mDNS apontando para o IP do operador), enquanto as portas `445/TCP` (SMB) e `80/TCP` (HTTP) ficam livres na máquina do operador para que o `impacket-ntlmrelayx` receba a conexão da vítima e encaminhe o handshake NTLMSSP para o servidor alvo.

## Como funciona
Para descobrir previamente quais hosts da sub-rede possuem **SMB Signing desabilitado** (`Signing: False`, logo vulneráveis a SMB Relay), o Responder inclui a ferramenta auxiliar **`tools/RunFinger.py -i 10.10.20.0/24`**, que varre rapidamente a faixa reportando a versão do OS, status do `SMB Signing`, `Null Session`, `RDP` e `MSSQL`.

## Exemplo
```bash
# 1. Identificar hosts na sub-rede que nao exigem SMB Signing (Signing: False) com RunFinger.py
python3 /opt/Responder/tools/RunFinger.py -i 10.10.20.0/24 -g

# 2. Desabilitar SMB e HTTP no Responder.conf antes de iniciar o Responder junto com o ntlmrelayx
sed -i 's/^SMB = On/SMB = Off/; s/^HTTP = On/HTTP = Off/' /opt/Responder/Responder.conf
```

## Limites e trade-offs
Tentar iniciar o `impacket-ntlmrelayx` enquanto `SMB = On` e `HTTP = On` estiverem ativos no `Responder.conf` causará erro `Address already in use` nas portas `445` e `80`.

## Como verificar
Execute `RunFinger.py -i <SUBNET>` após aplicar uma GPO de *SMB Signing Required* e confirme que 100% dos hosts Windows reportam `Signing:'True'`.

## Conexões
- [[responder-escopo-responder-conf-respondto-dontrespondto-autoignore]] — Veja também: Responder: Controle Estrito de Escopo em `Responder.conf` (`RespondTo`, `DontRespondTo`, `RespondToName`, `DontRespondToTLD` e `AutoIgnoreAfterSuccess`).
- [[responder-utilitarios-runfinger-findsqlsrv-icmp-redirect-multirelay]] — Veja também: Ferramentas Auxiliares da Suíte Responder (`tools/RunFinger.py`, `tools/FindSQLSrv.py` e `tools/MultiRelay.py`).
- [[responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2]] — Referência cruzada direta com responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2.
- [[impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials]] — Referência cruzada direta com impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials.
- [[netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks]] — Referência cruzada direta com netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
