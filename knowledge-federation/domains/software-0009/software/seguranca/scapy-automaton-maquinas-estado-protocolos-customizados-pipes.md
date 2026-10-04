---
id: software.seguranca.tranche15.001489
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

# Máquinas de Estado de Protocolo (**`Automaton` — `@ATMT.state`, `@ATMT.receive_condition`**) e **`Pipetool`** no Scapy: Implementando Clientes, Servidores e Honeypots

## Em uma frase
Quando você precisa implementar um protocolo que exige **múltiplos passos com estado e temporizadores** (por exemplo: um cliente/servidor de handshake customizado, um emulador de protocolo industrial para um Honeypot ou um testador de máquina de estados TLS/DHCP/EAPOL), usar apenas `sr1()` sequencial fica complexo se pacotes chegarem fora de ordem ou sofrerem timeout!

## Por que importa
Como o **Scapy** permite programar **Máquinas de Estado Finitas Orientadas a Eventos de Rede e Timeouts** de forma limpa e declarativa em Python?

## Como funciona
Através da classe nativa **`Automaton` (`from scapy.automaton import Automaton, ATMT`)**! Em uma subclasse de `Automaton`, você decora métodos com **`@ATMT.state(initial=1)`** (estados da máquina), **`@ATMT.receive_condition(ESTADO)`** (transições disparadas quando um pacote específico chega da rede!), **`@ATMT.timeout(ESTADO, segundos)`** (transições automáticas se o par remoto demorar a responder!) e **`@ATMT.action(...)`** (ações executadas durante a transição)!

## Exemplo
```python
# Definir a estrutura declarativa de uma Maquina de Estados de Protocolo (Automaton) no Scapy com estados, condicao de recebimento e timeout
from scapy.automaton import Automaton, ATMT

class MonitorHandshake(Automaton):
    @ATMT.state(initial=1)
    def AGUARDANDO(self):
        pass

    @ATMT.timeout(AGUARDANDO, 5)
    def expirar_espera(self):
        raise self.FIM()

    @ATMT.state(final=1)
    def FIM(self):
        return "Ciclo concluido"
```

## Limites e trade-offs
Além de rodar diretamente na placa de rede, toda subclasse de **`Automaton`** do Scapy pode gerar automaticamente o **Grafo Visual Graphviz da sua Máquina de Estados** chamando ` MonitorHandshake.graph()` — desenhando todas as bolhas de estados e as setas de transição de pacotes e timeouts para a documentação da sua equipe!

## Como verificar
Para fluxos contínuos de transformação de pacotes (como ler de um PCAP, filtrar, modificar um cabeçalho IP e injetar em uma interface TAP ou Wireshark ao vivo), o Scapy também inclui o motor **`PipeEngine` (`Scapy Pipetool`)**!

## Conexões
- [[scapy-camadas-avancadas-tls-http2-80211-dot11-iot-scada-modbus]] — Veja também: Submódulos Avançados do Scapy (`load_layer` / `load_contrib`): Dissecando **TLS 1.3 (`scapy.layers.tls`)**, **HTTP/2**, **Wi-Fi `Dot11`/`RadioTap`** e **Protocolos Industriais (`modbus`, `s7comm`)**.
- [[scapy-definicao-protocolos-customizados-packet-fieldsdesc-dissector]] — Veja também: Criando Dissecadores de **Protocolos Proprietários ou Binários Customizados** em 10 Linhas no Scapy: Subclasse **`Packet`**, **`fields_desc`** e **`bind_layers()`**.
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Referência cruzada direta com scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
