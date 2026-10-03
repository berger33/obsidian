---
id: software.seguranca.tranche06.000580
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

# Hardening Definitivo do Windows e Active Directory contra o Responder (Desativar **LLMNR**, **NBT-NS**, **mDNS**, **WPAD** e Exigir **SMB/LDAP Signing**)

## Em uma frase
A erradicação definitiva da superfície de ataque explorada pelo Responder em ambientes corporativos Windows exige aplicar um conjunto coordenado de configurações via **Group Policy (GPO)**, **DHCP** e **Switches de Camada 2**.

## Por que importa
Desativar apenas o LLMNR deixando o **NBT-NS** ou o **mDNS** ativos ainda permite o envenenamento pelo próximo protocolo na cadeia de *fallback* do Windows; da mesma forma, desativar a resolução multicast sem exigir **SMB Signing** e **LDAP Signing / Channel Binding** deixa a rede exposta a coerção de autenticação (`PetitPotam`, `PrinterBug`) e *NTLM Relay*.

## Como funciona
O checklist completo de Hardening compreende: **(1) Desativar LLMNR** via GPO (*Computer Configuration -> Administrative Templates -> Network -> DNS Client -> Turn off multicast name resolution = Enabled*, chave `EnableMulticast = 0`), **(2) Desativar NetBIOS over TCP/IP (NBT-NS)** via opção DHCP Microsoft `001 Disable NetBIOS over TCP/IP = 0x2` ou script de GPO (`SetTcpipNetbios(2)`), **(3) Desativar mDNS** no Windows (`HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters\EnableMDNS = 0`), **(4) Desativar o serviço WPAD** (`WinHttpAutoProxySvc` = `Disabled`), **(5) Exigir `SMB Signing` e `LDAP Signing / Channel Binding`** em todos os clientes e servidores e **(6) Habilitar `RA Guard` e `DHCPv6 Guard`** nos switches.

## Exemplo
```powershell
# Script PowerShell de auditoria e hardening local para verificar desativacao de LLMNR, mDNS, NBT-NS e exigencia de SMB Signing
Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient" -Name "EnableMulticast" -Value 0 -Type DWord -Force
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" -Name "EnableMDNS" -Value 0 -Type DWord -Force
Set-SmbClientConfiguration -RequireSecuritySignature $true -Force
Set-SmbServerConfiguration -RequireSecuritySignature $true -Force

Get-SmbServerConfiguration | Select-Object EnableSecuritySignature, RequireSecuritySignature
```

## Limites e trade-offs
No Windows 11 e Windows Server 2025, a Microsoft passou a exigir *SMB Signing* por padrão nas edições mais recentes, mas em domínios legados atualizados a partir de versões anteriores a GPO explícita (`Microsoft network server: Digitally sign communications (always) = Enabled`) continua obrigatória.

## Como verificar
Após aplicar as GPOs de hardening, execute `Responder.py -I eth0 -A` na VLAN e `RunFinger.py -i <SUBNET>` para comprovar zero tráfego LLMNR/NBT-NS e 100% de `Signing:'True'`.

## Conexões
- [[responder-deteccao-blue-team-suricata-zeek-sysmon-canary-queries]] — Veja também: Detecção de Envenenamento LLMNR/NBT-NS/mDNS/DHCPv6 pelo **Blue Team** (Suricata, Zeek, Windows Event Logs e *Canary Name Queries*).
- [[responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva]] — Referência cruzada direta com responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva.
- [[responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay]] — Referência cruzada direta com responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay.
- [[impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials]] — Referência cruzada direta com impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials.

## Fontes
- [Responder Official GitHub — LLMNR/NBT-NS/mDNS/DHCPv6 Poisoner & Rogue Servers](https://raw.githubusercontent.com/lgandx/Responder/master/README.md) — documentação oficial do Responder cobrindo modo passivo -A, servidores rogue, DHCPv6, Kerberos e ferramentas auxiliares; consultado em 2026-10-03.
- [Responder Official Configuration — Responder.conf Reference](https://raw.githubusercontent.com/lgandx/Responder/master/Responder.conf) — configuração oficial do Responder detalhando KerberosMode, RespondTo, DontRespondTo, AutoIgnoreAfterSuccess e DHCPv6; consultado em 2026-10-03.
- [Responder Repository & Tools Suite](https://github.com/lgandx/Responder) — repositório oficial da suíte Responder (RunFinger, MultiRelay, FindSQLSrv); consultado em 2026-10-03.
