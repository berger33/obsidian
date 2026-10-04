---
id: software.seguranca.tranche15.001485
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

# Fuzzing Inteligente de Protocolos de Rede com **`fuzz()`** e `VolatileValue` no Scapy: Testando a Robustez de Parsers, Firewalls e Regras IDS/IPS

## Em uma frase
Se você gerar bytes 100% aleatórios com `/dev/urandom` e enviá-los na placa de rede para testar um servidor DNS, um parser industrial Modbus ou uma regra do **Snort 3 / Suricata**, o pacote será descartado logo na primeira linha do kernel porque o comprimento do cabeçalho IP ou o checksum estará inválido!

## Por que importa
Como fazer **Fuzzing Estruturado de Camada (`Layer-Aware Protocol Fuzzing`)** onde todos os valores dos campos da camada alvo mudam aleatoriamente a cada pacote enviado, mas **os comprimentos calculados, tipos de protocolo e checksums permanecem matematicamente válidos** para que o pacote atravesse a pilha TCP/IP e atinja em cheio o parser da aplicação?

## Como funciona
Com a função mágica **`fuzz()`** do Scapy! Quando você envolve uma camada com **`fuzz(DNS())`** (por exemplo: `IP(dst="10.0.0.50") / UDP(dport=53) / fuzz(DNS(qd=fuzz(DNSQR())))`), o Scapy transforma todos os campos daquela camada (exceto os campos que você fixou explicitamente e os campos de cálculo automático de comprimento/checksum!) em objetos **`VolatileValue` (`RandByte`, `RandShort`, `RandString`, `RandIP`)** que sorteiam um valor novo e válido para o tipo de dado daquele campo a cada pacote emitido!

## Exemplo
```python
# Criar um gerador de Fuzzing de protocolo DNS sobre UDP onde IP e UDP permanecem integros e todos os campos DNS variam aleatoriamente
from scapy.all import DNS, DNSQR, IP, UDP, fuzz

pacote_fuzz = IP(dst="192.0.2.53") / UDP(dport=53) / fuzz(DNS(qd=fuzz(DNSQR())))
for _ in range(3):
    amostra = IP( bytes(pacote_fuzz) )
    print(amostra.summary(), "id=", amostra[DNS].id, "opcode=", amostra[DNS].opcode)
```

## Limites e trade-offs
Veja no loop acima o que acontece a cada vez que `bytes(pacote_fuzz)` (ou `send(pacote_fuzz, count=100)`) é avaliado: o mesmo objeto `pacote_fuzz` produz um pacote DNS estruturalmente diferente a cada iteração (testando `opcode`, `rcode`, flags truncadas, contagens de registros e strings malformadas), com o checksum UDP recalculado perfeitamente!

## Como verificar
Para testar se uma nova regra do **Snort 3** ou **Suricata** realmente dispara ou se pode ser burlada por variações de cabeçalho, gere um arquivo `.pcap` de teste com `wrpcap("teste_ids.pcap", [bytes(pacote_fuzz) for _ in range(500)])` e passe para `snort -r teste_ids.pcap`!

## Conexões
- [[scapy-captura-sniff-filtros-bpf-lfilter-prn-offline-rdpcap-wrpcap]] — Veja também: Captura Programática (**`sniff()`** com `filter` BPF, `lfilter` Python e Callback `prn`) e Processamento de PCAPs em Streaming (**`PcapReader` vs. `rdpcap`**) no Scapy.
- [[scapy-auditoria-camada-2-arp-vlan-8021q-dhcp-dai-port-security]] — Veja também: Testes de Segurança de **Camada 2 (Data Link)** com Scapy: Auditoria de **Dynamic ARP Inspection (DAI)**, **802.1Q VLAN Hopping (Double Tagging)** e **DHCP Snooping**.
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Referência cruzada direta com scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas.
- [[snort-inspetores-http-inspect-js-norm-dce-smb-scada-ics]] — Referência cruzada direta com snort-inspetores-http-inspect-js-norm-dce-smb-scada-ics.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
