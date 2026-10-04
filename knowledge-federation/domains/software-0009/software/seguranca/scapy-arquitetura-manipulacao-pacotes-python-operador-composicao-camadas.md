---
id: software.seguranca.tranche15.001481
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

# Arquitetura do **Scapy (`secdev/scapy`)**: Construção e Dissecação de Pacotes de Rede em **Python**, Operador de Composição **`/`** e Sobrecarga Inteligente de Campos

## Em uma frase
Por que o **Scapy (`secdev/scapy`)** é a biblioteca e shell interativo em **Python** preferido por pesquisadores de vulnerabilidades de protocolo, engenheiros de NIDS (**Snort 3 / Suricata / Zeek**) e desenvolvedores de segurança de rede no mundo inteiro?

## Por que importa
Como resume a documentação oficial (`usage.rst`), enquanto ferramentas de linha de comando tradicionais fazem apenas uma tarefa fixa e escondem a estrutura interna dos pacotes, o **Scapy** modela cada protocolo de rede (`Ether`, `Dot1Q`, `ARP`, `IP`, `IPv6`, `ICMP`, `TCP`, `UDP`, `DNS`, `TLS`, `Dot11`) como uma **Classe Python composicional unida pelo operador `/` (*Stacking Layers*)**!

## Como funciona
Quando você escreve **`pkt = Ether() / IP(dst="10.0.0.1") / TCP(dport=443, flags="S")`**, a camada inferior (`Ether` e `IP`) **sobrecarrega automaticamente seus campos padrão de acordo com a camada superior** (por exemplo: `Ether.type` vira `0x0800 IPv4`, `IP.proto` vira `6 TCP`, `IP.src` é preenchido automaticamente consultando a tabela de roteamento do sistema operacional para `10.0.0.1`, e todos os *checksums* e comprimentos `len` são calculados na hora de serializar com `raw(pkt)`)!

## Exemplo
```python
# Construir, inspecionar os campos resolvidos (show2) e dissecar um pacote TCP/IP com payload HTTP usando a biblioteca Scapy em Python 3
from scapy.all import Ether, IP, TCP, Raw, hexdump, raw

pkt = Ether() / IP(dst="192.0.2.10", ttl=64) / TCP(dport=80, flags="S") / Raw(b"TEST")
pkt.show2()
hexdump(raw(pkt))
```

## Limites e trade-offs
Qual é a diferença fundamental entre chamar **`pkt.show()`** e **`pkt.show2()`** no Scapy documentada na tabela oficial de comandos? **`pkt.show()`** mostra o pacote antes da montagem (onde campos calculados automaticamente como `len` e `chksum` ainda aparecem como `None`), enquanto **`pkt.show2()`** monta os bytes brutos (`raw(pkt)`) e disseca o pacote montado — exibindo os **valores reais calculados de `len`, `ihl`, `dataofs` e `chksum`** exatamente como sairão na placa de rede!

## Como verificar
Use **`ls(TCP)`** (ou `ls(IP)`, `ls(DNS)`) no shell do Scapy para listar instantaneamente todos os nomes de campos, tipos e valores default de qualquer protocolo suportado.

## Conexões
- [[scapy-envio-recebimento-send-sendp-sr-sr1-srp-matching-respostas]] — Veja também: A Família de Funções de Envio e Recebimento no Scapy: **`send()` vs. `sendp()`** e Pareamento Estímulo-Resposta com **`sr()`, `sr1()` e `srp()`**.
- [[scapy-geracao-conjuntos-pacotes-produto-cartesiano-packetlist]] — Referência cruzada direta com scapy-geracao-conjuntos-pacotes-produto-cartesiano-packetlist.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
