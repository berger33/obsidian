---
id: software.seguranca.tranche06.000571
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

# Responder: Arquitetura de Resolução de Nomes Multicast/Broadcast (**LLMNR** UDP 5355, **NBT-NS** UDP 137 e **mDNS** UDP 5353) e Modo Passivo (`-A`)

## Em uma frase
**Responder** (`lgandx/Responder`, GPLv3, mantido pela SpiderLabs / Laurent Gaffie) é a ferramenta padrão para auditar a exposição de redes corporativas Windows/Active Directory a protocolos de resolução de nomes local baseados em multicast/broadcast (**LLMNR**, **NBT-NS** e **mDNS**) e descoberta automática de proxy (**WPAD**).

## Por que importa
Por padrão em instalações Windows não endurecidas, quando um host ou serviço tenta acessar um nome de servidor que não existe no DNS corporativo (ex.: um erro de digitação `\\filesrv01\public` em vez de `\\filesrv02\public`, ou um atalho antigo mapeado em GPO), o Windows faz *fallback* perguntando em multicast/broadcast para toda a VLAN local via **LLMNR** (`224.0.0.252` / `ff02::1:3` UDP 5355), **NBT-NS** (broadcast UDP 137) e **mDNS** (`224.0.0.251` / `ff02::fb` UDP 5353).

## Como funciona
Antes de realizar qualquer teste ativo, a flag **`-A` (*Analyze Mode*)** executa o Responder em modo **100% passivo**: ele apenas escuta na interface (`-I eth0`) e registra todas as consultas LLMNR, NBT-NS, mDNS e solicitações de navegador/WPAD vistas no segmento de rede sem enviar absolutamente nenhum pacote de resposta.

## Exemplo
```bash
# Executar o Responder em modo 100% passivo (-A Analyze Mode) para inventariar consultas LLMNR/NBT-NS/mDNS na VLAN
sudo python3 Responder.py -I eth0 -A -v
```

## Limites e trade-offs
O modo **`-A`** é totalmente seguro para diagnósticos de *Blue Team* e auditorias de conformidade: qualquer consulta LLMNR ou NBT-NS observada em `-A` comprova que as políticas de GPO de desativação de protocolos legados ainda não foram aplicadas àquelas estações.

## Como verificar
Inspecione os logs em `logs/Analyzer-Session.log` após rodar `Responder.py -I eth0 -A` por 15 minutos para listar todos os hosts que ainda emitem broadcasts de resolução de nomes.

## Conexões
- [[responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2]] — Veja também: Responder: Servidores de Autenticação *Rogue* Integrados (SMB, HTTP/HTTPS, LDAP, MSSQL, SMTP/IMAP, WinRM, RDP) e Captura **NetNTLMv1/v2**.
- [[responder-escopo-responder-conf-respondto-dontrespondto-autoignore]] — Referência cruzada direta com responder-escopo-responder-conf-respondto-dontrespondto-autoignore.
- [[responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing]] — Referência cruzada direta com responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
