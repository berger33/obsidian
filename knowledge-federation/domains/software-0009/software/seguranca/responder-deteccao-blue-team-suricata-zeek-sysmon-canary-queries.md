---
id: software.seguranca.tranche06.000579
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

# Detecção de Envenenamento LLMNR/NBT-NS/mDNS/DHCPv6 pelo **Blue Team** (Suricata, Zeek, Windows Event Logs e *Canary Name Queries*)

## Em uma frase
Equipes de SOC e Engenharia de Detecção podem detectar o uso do Responder na rede em segundos através de três camadas complementares: **monitoramento passivo NSM (Zeek/Suricata)**, **telemetria de endpoint Windows** e **Sondas Canário de Resolução de Nomes (*LLMNR/NBT-NS Canary Queries*)**.

## Por que importa
Um envenenador ativo na VLAN se revela imediatamente quando uma estação (ou um sensor do SOC) envia uma consulta LLMNR/NBT-NS para um hostname inexistente gerado aleatoriamente (ex.: `\\HONEY-CHECK-9821A`): em uma rede limpa, **nenhum host jamais deve responder** a um nome inexistente; se qualquer IP responder dizendo *"sou eu"*, há um Responder ativo naquele segundo na VLAN.

## Como funciona
Além das sondas canário, regras do **Suricata** detectam o certificado TLS padrão ou challenges conhecidos do Responder, e logs do **Zeek** (`dns.log` nas portas UDP `5355`/`137`/`5353` e `ntlm.log` / `smb_files.log`) mostram um único IP de estação de trabalho respondendo a dezenas de nomes distintos e recebendo conexões SMB de entrada de múltiplos colegas da mesma VLAN.

## Exemplo
```zeek
# Logica de caca no Zeek (dns.log): identificar um unico IP respondendo a multiplos nomes distintos via LLMNR (5355/udp)
# Consulta via zeek-cut sobre dns.log filtrando porta 5355 onde rcode_name == NOERROR
```

## Limites e trade-offs
Implemente um script leve ou agente EDR em uma máquina por VLAN que envie periodicamente uma consulta LLMNR/NBT-NS para um hostname aleatório inexistente e dispare um alerta de severidade crítica no SIEM/TheHive caso receba qualquer pacote UDP de resposta.

## Como verificar
Teste a regra de detecção em uma VLAN de laboratório confirmando que o alerta no SIEM identifica o endereço IP e o endereço MAC exatos da máquina que respondeu à sonda canário.

## Conexões
- [[responder-auditoria-offline-senhas-hashcat-netntlmv2-netntlmv1-regras]] — Veja também: Auditoria de Força de Senhas sobre Hashes Capturados pelo Responder (`NetNTLMv2` Hashcat `-m 5600` vs `NetNTLMv1` `-m 5500`).
- [[responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing]] — Veja também: Hardening Definitivo do Windows e Active Directory contra o Responder (Desativar **LLMNR**, **NBT-NS**, **mDNS**, **WPAD** e Exigir **SMB/LDAP Signing**).
- [[responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva]] — Referência cruzada direta com responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
