---
id: software.seguranca.tranche15.001487
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

# Testando Motores de Reassemblagem de **NIDS/NIPS (Snort 3 / Suricata / Firewalls)** com **`fragment()`** e Fragmentação IP/TCP Customizada no Scapy

## Em uma frase
Na Tranche 14 vimos que o inspetor `stream_tcp` e o motor de desfragmentação IP do **Snort 3** e do **Suricata** remontam pacotes fragmentados antes de aplicar as regras de assinatura. Como um engenheiro de detecção usa o **Scapy** para gerar arquivos `.pcap` de teste com **Fragmentação IP (`fragment()`), Fragmentos Fora de Ordem e Segmentos TCP Pequenos** e provar que o NIDS não sofre bypass?

## Por que importa
O Scapy inclui a função nativa **`fragment(pkt, fragsize=...)`**, que divide qualquer pacote IP grande em uma lista de fragmentos IPv4 ajustando automaticamente a flag **`MF` (*More Fragments*)** e o campo **`frag` (*Fragment Offset* em múltiplos de 8 bytes)** de cada pedaço!

## Como funciona
Além disso, como os fragmentos retornados por `fragment()` são objetos `Packet` normais em uma lista Python, você pode **inverter a ordem da lista (`frags[::-1]`)** ou construir fragmentos sobrepostos manualmente para verificar se a política de reassemblagem de SO (`linux` vs. `windows` vs. `bsd`) do seu NIDS/Firewall reconstrói exatamente o mesmo payload que o servidor de destino!

## Exemplo
```python
# Fragmentar um pacote IP/ICMP grande em pedacos de 16 bytes com fragment(), inverter a ordem de envio e salvar em PCAP para testar o Snort 3 / Suricata
from scapy.all import ICMP, IP, Raw, fragment, wrpcap

pkt_original = IP(dst="192.0.2.10") / ICMP() / Raw(b"A" * 64)
lista_fragmentos = fragment(pkt_original, fragsize=16)
wrpcap("./teste_fragmentos_fora_de_ordem.pcap", lista_fragmentos[::-1])
for f in lista_fragmentos:
    print(f.summary(), "flags=", f.flags, "offset=", f.frag)
```

## Limites e trade-offs
Por que o campo `frag` (*Fragment Offset*) impresso pelo loop acima avança de `0`, `2`, `4`, `6` quando o `fragsize=16`? Porque no cabeçalho IPv4 (`RFC 791`), o campo *Fragment Offset* tem 13 bits e é expresso em **unidades de 8 octetos (8 bytes)**: portanto, `offset = 2` significa `2 x 8 = 16 bytes`!

## Como verificar
Execute o seu sensor **Snort 3** ou **Suricata** contra o arquivo `./teste_fragmentos_fora_de_ordem.pcap` gerado acima para validar que as regras de detecção disparam normalmente mesmo quando os fragmentos chegam em ordem reversa!

## Conexões
- [[scapy-auditoria-camada-2-arp-vlan-8021q-dhcp-dai-port-security]] — Veja também: Testes de Segurança de **Camada 2 (Data Link)** com Scapy: Auditoria de **Dynamic ARP Inspection (DAI)**, **802.1Q VLAN Hopping (Double Tagging)** e **DHCP Snooping**.
- [[scapy-camadas-avancadas-tls-http2-80211-dot11-iot-scada-modbus]] — Veja também: Submódulos Avançados do Scapy (`load_layer` / `load_contrib`): Dissecando **TLS 1.3 (`scapy.layers.tls`)**, **HTTP/2**, **Wi-Fi `Dot11`/`RadioTap`** e **Protocolos Industriais (`modbus`, `s7comm`)**.
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Referência cruzada direta com scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas.
- [[snort-inspetores-http-inspect-js-norm-dce-smb-scada-ics]] — Referência cruzada direta com snort-inspetores-http-inspect-js-norm-dce-smb-scada-ics.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
