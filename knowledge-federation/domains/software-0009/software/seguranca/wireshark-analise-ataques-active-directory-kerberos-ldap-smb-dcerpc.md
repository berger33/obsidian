---
id: software.seguranca.tranche06.000557
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
fontes: ["https://raw.githubusercontent.com/wireshark/wireshark/master/README.md", "https://www.wireshark.org/docs/man-pages/tshark.html", "https://www.wireshark.org/docs/wsug_html_chunked/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Wireshark & `tshark`: Filtros de Detecção de Ataques em Active Directory (Kerberos Roasting, `DCSync` `DRSUAPI`, NTLM Relay e `psexec`)

## Em uma frase
O conjunto profundo de dissecadores Microsoft do Wireshark (`kerberos`, `ntlmssp`, `smb2`, `dcerpc`, `drsuapi`, `samr`, `lsarpc`, `svcctl`, `ldap`) permite identificar ataques contra Active Directory no nível exato da chamada de procedimento remoto.

## Por que importa
Permite distinguir na rede uma replicação legítima entre dois Domain Controllers de um ataque **`DCSync`** (`secretsdump.py` / Mimikatz) originado de uma estação de trabalho usando a operação `DsGetNCChanges` (`drsuapi.opnum == 3`), ou detectar *Kerberoasting* filtrando pedidos `TGS-REQ` com downgrade para cifra `RC4-HMAC` (`etype == 23`).

## Como funciona
Da mesma forma, movimentação lateral estilo `psexec` / `smbexec` deixa uma assinatura cristalina na rede: conexão `SMB2 Tree Connect` ao compartilhamento `IPC$` e `ADMIN$`, abertura do named pipe `\pipe\svcctl` e chamadas `DCERPC` para `CreateServiceW` (`svcctl.opnum == 12`) e `StartServiceW` (`svcctl.opnum == 19`).

## Exemplo
```bash
# Detectar chamadas DCSync (DRSUAPI DsGetNCChanges opnum 3), criacao remota de servicos (svcctl) e Kerberoasting RC4
tshark -r /cases/pcaps/ad_incident.pcapng -n \
  -Y '(drsuapi.opnum == 3) || (svcctl.opnum == 12) || (kerberos.msg_type == 12 && kerberos.etype == 23)' \
  -T fields -e frame.time_utc -e ip.src -e ip.dst -e _ws.col.Protocol -e _ws.col.Info
```

## Limites e trade-offs
Se os clientes de domínio utilizarem *LDAP Signing / Sealing* (`SASL GSS-SPNEGO`) ou *SMB3 Encryption*, os payloads internos de LDAP/SMB2 aparecerão cifrados (`smb2.transform.signature`); porém, metadados de Kerberos (`etype`, `cname`, `sname`) e conexões de transporte permanecem visíveis.

## Como verificar
Audite capturas de sub-redes de servidores filtrando `drsuapi` e confirme que os únicos endereços `ip.src` legítimos são exclusivamente Domain Controllers oficiais.

## Conexões
- [[wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark]] — Veja também: Wireshark & `tshark`: Extração Forense de Arquivos e Payloads Transferidos via Rede (`--export-objects http,smb,tftp,imf`).
- [[wireshark-manipulacao-pcaps-editcap-mergecap-capinfos-reordercap]] — Veja também: Utilitários de Manipulação Forense de PCAPs do Wireshark: `capinfos`, `editcap`, `mergecap` e `reordercap`.
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — Referência cruzada direta com wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens.
- [[impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa]] — Referência cruzada direta com impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa.
- [[responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva]] — Referência cruzada direta com responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva.

## Fontes
- [Wireshark Official GitHub — Architecture & Security Privilege Separation](https://raw.githubusercontent.com/wireshark/wireshark/master/README.md) — documentação oficial do Wireshark cobrindo arquitetura, formato pcapng e isolamento de privilégios no dumpcap; consultado em 2026-10-03.
- [Wireshark Official Manual Page — tshark CLI Reference](https://www.wireshark.org/docs/man-pages/tshark.html) — manual oficial do tshark cobrindo filtros -f vs -Y, análise em duas passagens -2, estatísticas -z e extração -T; consultado em 2026-10-03.
- [Wireshark User's Guide — Official HTML Documentation](https://www.wireshark.org/docs/wsug_html_chunked/) — guia oficial do usuário do Wireshark; consultado em 2026-10-03.
