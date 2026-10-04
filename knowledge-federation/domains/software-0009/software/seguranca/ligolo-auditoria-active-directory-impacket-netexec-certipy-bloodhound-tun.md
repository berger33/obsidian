---
id: software.seguranca.tranche16.001569
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md", "https://docs.ligolo.ng/Quickstart/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Executando Ferramentas de Auditoria **Active Directory (`NetExec`, `Impacket`, `Certipy`, `BloodHound CE`, `Responder`)** Nativamente sobre a Interface `TUN` do Ligolo-ng

## Em uma frase
Quem já tentou rodar o **BloodHound Python (`bloodhound-python`)**, o **Certipy (`certipy find`)** ou o **Impacket (`secretsdump.py` / `GetUserSPNs.py`)** através de um proxy SOCKS lento com `proxychains4` sabe como consultas LDAP/LDAPS, Kerberos (`88/tcp` e `88/udp`), DNS (`53/udp`) e RPC/SMB (`135`, `445` e portas altas dinâmicas) frequentemente sofrem timeout ou falham na resolução DNS no `proxychains`!

## Por que importa
Como configurar o `/etc/resolv.conf` (ou `--dns-ip`) junto com a interface **`TUN` do Ligolo-ng** para que 100% do arsenal de auditoria de Active Directory rode como se a sua máquina Linux estivesse fisicamente plugada no switch da rede interna do Domain Controller?

## Como funciona
Com a rota da sub-rede do Domain Controller adicionada na interface `TUN` do Ligolo-ng (ex.: `10.100.10.0/24 dev ligolo`), tanto os pacotes **TCP** quanto os pacotes **UDP (incluindo DNS `53/udp` e Kerberos `88/udp`!)** chegam diretamente ao Domain Controller! Basta apontar o `nameserver 10.100.10.5` (IP do DC) no `/etc/resolv.conf` e sincronizar o relógio Kerberos (`ntpdate` / `rdate`)!

## Exemplo
```bash
# Executar coleta do BloodHound CE e auditoria AD CS com Certipy diretamente sobre a rota TUN do Ligolo-ng (sem proxychains!)
certipy find -u 'auditor@corp.interno' -p "${AD_PASS}" -dc-ip 10.100.10.5 -vulnerable -stdout
nxc ldap 10.100.10.5 -u 'auditor' -p "${AD_PASS}" --bloodhound --collection All --dns-server 10.100.10.5
```

## Limites e trade-offs
Olhe os dois comandos acima rodando **sem `proxychains4`**: como o tráfego para `10.100.10.5` passa direto pela interface `TUN` do kernel roteada pelo Ligolo-ng (`> 100 Mbits/s`), a coleta completa `--bloodhound --collection All` do **NetExec** e a enumeração de templates AD CS do **Certipy** terminam em poucos segundos sem perder nenhuma conexão RPC ou consulta DNS UDP!

## Como verificar
Lembre-se sempre de restaurar o seu `/etc/resolv.conf` e remover as rotas e a interface `TUN` (`interface_delete` / `ip link delete ligolo`) ao concluir o teste.

## Conexões
- [[ligolo-multiplos-tuneis-simultaneos-segmentacao-interfaces-tun-paralelas]] — Veja também: Operando **Múltiplos Túneis Simultâneos** para Diferentes Sub-Redes no Ligolo-ng: Uma Interface **`TUN`** Dedicada por Agente.
- [[ligolo-deteccao-defesa-blue-team-certificado-padrao-yamux-gvisor-edr]] — Veja também: Engenharia de Detecção (**Blue Team / SOC / NSM / EDR**) Contra o **Ligolo-ng**: Certificado TLS Default (`ligolo`), Multiplexador **`hashicorp/yamux`** e Telemetria de Processo.
- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Referência cruzada direta com ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks.

## Fontes
- [Ligolo-ng Official GitHub Repository (`nicocha30/ligolo-ng`)](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/README.md) — repositório oficial do túnel de Camada 3 Ligolo-ng cobrindo arquitetura `TUN` + `gVisor` sem privilégios no agente, performance e recomendações `--unprivileged` para Nmap; consultado em 2026-10-03.
- [Ligolo-ng Official Quickstart & Setup Documentation (`docs.ligolo.ng/Quickstart`)](https://docs.ligolo.ng/Quickstart/) — documentação oficial do Ligolo-ng detalhando criação de interfaces `interface_create`, `certificate_fingerprint`/`-accept-fingerprint`, `session`, `ifconfig`, `interface_add_route` e `tunnel_start`; consultado em 2026-10-03.
