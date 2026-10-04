---
id: software.seguranca.tranche15.001490
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

# Criando Dissecadores de **Protocolos Proprietários ou Binários Customizados** em 10 Linhas no Scapy: Subclasse **`Packet`**, **`fields_desc`** e **`bind_layers()`**

## Em uma frase
Durante uma engenharia reversa de firmware IoT, auditoria de jogo online, análise de protocolo industrial ou investigação de um malware de C2 que usa um **protocolo binário proprietário sobre TCP/UDP** (por exemplo: `Magic (4 bytes) + Opcode (1 byte) + Tamanho (2 bytes) + Payload`), no Wireshark ou `tcpdump` o pacote inteiro aparece apenas como uma sopa hexadecimal genérica (`Raw Data`)!

## Por que importa
Como ensinar o **Scapy** a dissecar e construir esse protocolo proprietário em **menos de 15 linhas de Python**?

## Como funciona
Criando uma subclasse de **`Packet`**, declarando a lista **`fields_desc`** com os tipos de campos ricos do Scapy (`XIntField`, `ByteEnumField`, `FieldLenField`, `StrLenField`, `BitField`, `ConditionalField`) e conectando-a à porta TCP/UDP com **`bind_layers(UDP, MeuProtocolo, dport=9999)`**!

## Exemplo
```python
# Definir um dissecador e construtor completo para um protocolo binario customizado (Magic + Opcode + Tamanho auto-calculado + Payload) no Scapy
from scapy.all import ByteEnumField, FieldLenField, Packet, StrLenField, UDP, XIntField, bind_layers

class ProtoCustom(Packet):
    name = "ProtocoloInternoIoT"
    fields_desc = [
        XIntField("magic", 0xCAFEBABE),
        ByteEnumField("opcode", 1, {1: "PING", 2: "AUTH", 3: "DATA"}),
        FieldLenField("tam", None, length_of="dados", fmt="H"),
        StrLenField("dados", b"", length_from=lambda pkt: pkt.tam),
    ]

bind_layers(UDP, ProtoCustom, dport=9999)
pkt = UDP(sport=12345, dport=9999) / ProtoCustom(opcode="AUTH", dados=b"token123")
pkt.show2()
```

## Limites e trade-offs
Olhe a inteligência da dupla **`FieldLenField("tam", None, length_of="dados", fmt="H")`** e **`StrLenField("dados", b"", length_from=lambda pkt: pkt.tam)`** na classe `ProtoCustom` acima: **(1) Na Construção**: quando você passa `dados=b"token123"` (`8 bytes`) deixando `tam=None`, o `FieldLenField` calcula e preenche `tam = 8` automaticamente!; e **(2) Na Dissecação (`UDP(bytes_da_rede)`)**: o `StrLenField` lê o valor de `pkt.tam` que veio da rede e recorta exatamente `tam` bytes para o campo `dados`, deixando o resto do pacote para a próxima camada!

## Como verificar
E como usamos **`bind_layers(UDP, ProtoCustom, dport=9999)`**, qualquer captura aberta com `rdpcap()` ou `sniff()` no Scapy já reconhecerá e decodificará automaticamente todos os pacotes da porta `9999` como `ProtocoloInternoIoT` (`opcode = AUTH`, `tam = 8`)!

## Conexões
- [[scapy-automaton-maquinas-estado-protocolos-customizados-pipes]] — Veja também: Máquinas de Estado de Protocolo (**`Automaton` — `@ATMT.state`, `@ATMT.receive_condition`**) e **`Pipetool`** no Scapy: Implementando Clientes, Servidores e Honeypots.
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Referência cruzada direta com scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas.
- [[scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids]] — Referência cruzada direta com scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
