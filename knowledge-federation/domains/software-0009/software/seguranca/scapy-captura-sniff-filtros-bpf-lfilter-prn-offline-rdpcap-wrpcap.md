---
id: software.seguranca.tranche15.001484
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

# Captura Programática (**`sniff()`** com `filter` BPF, `lfilter` Python e Callback `prn`) e Processamento de PCAPs em Streaming (**`PcapReader` vs. `rdpcap`**) no Scapy

## Em uma frase
Como construir em poucas linhas de Python com o **Scapy** um sensor customizado de rede que analisa pacotes ao vivo na placa de rede (`sniff()`) ou processa arquivos `.pcap` gigantescos de vários Gigabytes sem estourar a memória RAM da máquina?

## Por que importa
Para captura ao vivo (ou leitura filtrada), a função **`sniff()`** do Scapy combina: **(1) `filter="tcp port 53 or udp port 53"`** (filtro **BPF compilado no Kernel** para descartar tráfego irrelevante com custo zero de Python!); **(2) `lfilter=lambda pkt: ...`** (função booleana em Python que avalia qualquer condição profunda das camadas dissecadas pelo Scapy!); **(3) `prn=minha_funcao`** (callback executado em tempo real para cada pacote capturado!); e **(4) `store=False`** (fundamental em sensores 24x7 para **não acumular os pacotes capturados na memória RAM**!)!

## Como funciona
E ao analisar arquivos `.pcap` salvos em disco: use **`rdpcap("pequeno.pcap")`** para carregar arquivos pequenos de uma vez na memória (e **`wrpcap("saida.pcap", pkts)`** para salvar), mas para arquivos `.pcap` de **Gigabytes**, use sempre o iterador em streaming **`with PcapReader("gigante.pcap") as pcap_reader:`**!

## Exemplo
```python
# Processar um arquivo PCAP grande em streaming (memoria constante O(1)) usando PcapReader do Scapy para extrair todas as consultas DNS
from scapy.all import DNS, DNSQR, IP, PcapReader

with PcapReader("./captura_rede.pcap") as reader:
    for pkt in reader:
        if pkt.haslayer(DNSQR) and pkt.haslayer(IP):
            qname = pkt[DNSQR].qname.decode("utf-8", errors="ignore")
            print(f"{pkt[IP].src} consultou DNS: {qname}")
```

## Limites e trade-offs
Por que usar **`store=False`** no `sniff(iface="eth0", filter="...", prn=callback, store=False)` e **`PcapReader`** na leitura de arquivos é obrigatório em ferramentas de produção? Porque `rdpcap()` e `sniff(store=True)` guardam cada objeto `Packet` dissecado em uma lista Python na RAM — em poucos milhões de pacotes, o processo consumiria dezenas de Gigabytes de memória! Com `PcapReader` e `sniff(store=False)`, o consumo de memória RAM permanece constante em poucos Megabytes mesmo processando 100 GB de tráfego!

## Como verificar
Você também pode usar **`AsyncSniffer`** do Scapy quando quiser iniciar e parar a captura de pacotes em uma thread de background enquanto o seu script Python executa testes de integração.

## Conexões
- [[scapy-geracao-conjuntos-pacotes-produto-cartesiano-packetlist]] — Veja também: Geração Declarativa de Conjuntos de Pacotes (**Produto Cartesiano de Campos**) e Manipulação de **`PacketList`** no Scapy.
- [[scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids]] — Veja também: Fuzzing Inteligente de Protocolos de Rede com **`fuzz()`** e `VolatileValue` no Scapy: Testando a Robustez de Parsers, Firewalls e Regras IDS/IPS.
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Referência cruzada direta com scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas.
- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Referência cruzada direta com tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
