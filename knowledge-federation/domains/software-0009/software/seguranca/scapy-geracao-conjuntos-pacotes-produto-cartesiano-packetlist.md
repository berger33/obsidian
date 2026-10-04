---
id: software.seguranca.tranche15.001483
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

# Geração Declarativa de Conjuntos de Pacotes (**Produto Cartesiano de Campos**) e Manipulação de **`PacketList`** no Scapy

## Em uma frase
Como o Scapy permite gerar uma varredura de sub-rede inteira, um *traceroute* paralelo de 30 saltos em 1 segundo ou uma matriz combinatória de portas e flags TCP **sem escrever um único loop `for` explícito**?

## Por que importa
Conforme demonstrado em `usage.rst` (*Generating sets of packets*), **qualquer campo de qualquer camada no Scapy aceita uma Lista, uma Tupla de intervalo `(inicio, fim)` ou uma Sub-rede CIDR `Net("10.0.0.0/24")`**!

## Como funciona
Quando você cria `pacotes = IP(dst="192.0.2.0/30", ttl=(1, 15)) / TCP(dport=[80, 443, 8443])`, o Scapy define implicitamente o **Produto Cartesiano (`4 IPs x 15 TTLs x 3 Portas = 180 pacotes`)**! Ao passar esse objeto para `ans, unans = sr(pacotes)`, o Scapy desenrola o gerador, dispara os 180 pacotes e armazena os resultados em um objeto poderoso chamado **`PacketList`** (que suporta métodos analíticos como `.summary()`, `.nsummary()`, `.filter()`, `.conversations()` e `.plot()`)!

## Exemplo
```python
# Executar um Traceroute TCP paralelo instantaneo (enviando TTLs de 1 a 20 simultaneamente para a porta 443) usando produto cartesiano no Scapy
from scapy.all import IP, TCP, sr

ans, unans = sr(
    IP(dst="198.51.100.10", ttl=(1, 20)) / TCP(dport=443, flags="S"),
    timeout=2,
    verbose=0,
)
for snd, rcv in ans:
    print(f"TTL={snd.ttl:02d} -> Hop={rcv.src} (TCP={rcv.haslayer(TCP)})")
```

## Limites e trade-offs
Compare o **Traceroute TCP Paralelo** de 8 linhas acima com o comando `traceroute` tradicional: enquanto o `traceroute` antigo usa pacotes UDP/ICMP (que quase todos os firewalls corporativos bloqueiam!) e espera um salto responder antes de mandar o próximo, o Scapy envia os 20 pacotes **`TCP SYN` na porta `443`** com `ttl=(1, 20)` de uma só vez — atravessando firewalls de borda e mapeando toda a rota de rede em um único RTT!

## Como verificar
Lembre-se do aviso oficial de `usage.rst`: se você chamar uma função de pacote único como `raw(a)` sobre um conjunto de pacotes sem antes desdobrá-lo com `[p for p in a]` ou `PacketList(a)`, apenas o primeiro elemento do conjunto será serializado.

## Conexões
- [[scapy-envio-recebimento-send-sendp-sr-sr1-srp-matching-respostas]] — Veja também: A Família de Funções de Envio e Recebimento no Scapy: **`send()` vs. `sendp()`** e Pareamento Estímulo-Resposta com **`sr()`, `sr1()` e `srp()`**.
- [[scapy-captura-sniff-filtros-bpf-lfilter-prn-offline-rdpcap-wrpcap]] — Veja também: Captura Programática (**`sniff()`** com `filter` BPF, `lfilter` Python e Callback `prn`) e Processamento de PCAPs em Streaming (**`PcapReader` vs. `rdpcap`**) no Scapy.
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Referência cruzada direta com scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
