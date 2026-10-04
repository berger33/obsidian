---
id: software.seguranca.tranche15.001488
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/secdev/scapy/master/README.md", "https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Submódulos Avançados do Scapy (`load_layer` / `load_contrib`): Dissecando **TLS 1.3 (`scapy.layers.tls`)**, **HTTP/2**, **Wi-Fi `Dot11`/`RadioTap`** e **Protocolos Industriais (`modbus`, `s7comm`)**

## Em uma frase
Você sabia que além de TCP/IP básico, o repositório oficial do **Scapy** traz implementações completas de **TLS 1.2/1.3 (incluindo handshakes, certificados X.509 e descriptografia com `NSS Key Log`!)**, **HTTP/2 (`scapy.contrib.http2`)**, **Quadros Sem Fio 802.11 (`Dot11`, `RadioTap`, `Dot11Beacon`, `Dot11Deauth`, `EAPOL`)** e dezenas de protocolos industriais **OT/SCADA (`modbus`, `pnio`, `opcua`, `can`, `isotp`)**?

## Por que importa
Para manter a inicialização do Scapy rápida, as camadas especializadas e contribuições ficam organizadas sob **`load_layer("tls")`** (ou `load_layer("http")`) e **`load_contrib("modbus")`** (ou `load_contrib("http2")`, `load_contrib("bgp")`, `load_contrib("gtp")` para redes móveis 4G/5G)!

## Como funciona
Uma vez carregado `load_layer("tls")`, o Scapy disseca nativamente mensagens `TLSClientHello`, extensões `TLS_Ext_ServerName` (`SNI`), `TLS_Ext_SupportedGroups` (incluindo grupos pós-quânticos!), `TLS_Ext_ALPN` e cadeias de certificados `Cert`!

## Exemplo
```python
# Carregar a camada TLS oficial do Scapy (load_layer("tls")) e construir um registro TLSClientHello com extensao SNI para auditoria de servidores
from scapy.all import load_layer

load_layer("tls")
from scapy.layers.tls.all import TLS, TLSClientHello, TLS_Ext_ServerName, ServerName

ch = TLS(msg=[TLSClientHello(ext=[TLS_Ext_ServerName(servernames=[ServerName(servername=b"api.exemplo.br")])])])
ch.show2()
```

## Limites e trade-offs
Veja como é simples usar **`load_layer("tls")`** no Scapy para criar testes automatizados de conformidade TLS ou verificar como um servidor reage a extensões `TLSClientHello` específicas (como `Encrypted Client Hello`, `ALPN` customizado ou *cipher suites* específicas) sem depender de bibliotecas externas rígidas!

## Como verificar
Use **`list_contrib()`** no shell do Scapy para pesquisar os mais de 150 protocolos industriais, automotivos (`CAN bus` / `UDS`), telecom (`GTP` / `PFCP`) e de roteamento (`BGP` / `OSPF` / `MPLS`) disponíveis em `scapy.contrib`!

## Conexões
- [[scapy-teste-evasao-fragmentacao-ip-overlap-idps-snort-suricata]] — Veja também: Testando Motores de Reassemblagem de **NIDS/NIPS (Snort 3 / Suricata / Firewalls)** com **`fragment()`** e Fragmentação IP/TCP Customizada no Scapy.
- [[scapy-automaton-maquinas-estado-protocolos-customizados-pipes]] — Veja também: Máquinas de Estado de Protocolo (**`Automaton` — `@ATMT.state`, `@ATMT.receive_condition`**) e **`Pipetool`** no Scapy: Implementando Clientes, Servidores e Honeypots.
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Referência cruzada direta com scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas.
- [[rustls-privacidade-encrypted-client-hello-ech-rfc9849-sni-alpn]] — Referência cruzada direta com rustls-privacidade-encrypted-client-hello-ech-rfc9849-sni-alpn.
- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Referência cruzada direta com aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
