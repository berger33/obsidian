---
id: software.seguranca.tranche15.001482
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

# A Família de Funções de Envio e Recebimento no Scapy: **`send()` vs. `sendp()`** e Pareamento Estímulo-Resposta com **`sr()`, `sr1()` e `srp()`**

## Em uma frase
Qual é a diferença exata no Scapy entre as funções que terminam sem `p` (**`send()`, `sr()`, `sr1()`**) e as funções que terminam com `p` (**`sendp()`, `srp()`, `srp1()`**), e como o Scapy sabe qual pacote recebido da rede é a resposta correspondente ao pacote que ele acabou de enviar?

## Por que importa
A regra é cristalina: **(1) As funções SEM `p` (`send`, `sr`, `sr1`) operam na Camada 3 (Rede: `IP(...) / TCP(...)`)** — o próprio Scapy consulta a tabela de roteamento do sistema operacional e monta o cabeçalho de Camada 2 automaticamente; já **(2) As funções COM `p` (`sendp`, `srp`, `srp1`) operam na Camada 2 (Enlace: `Ether(...) / ...` ou `Dot11(...)`)**, exigindo que você construa o quadro Ethernet/802.11 explicitamente e escolha a interface `iface="eth0"`!

## Como funciona
E o grande diferencial do **`sr(pacotes)` (*Send and Receive*)** é o paradigma **Estímulo -> Resposta (`ans, unans`)**: o Scapy envia todos os estímulos, pareia matematicamente cada pacote de resposta com o pacote que o provocou (mesmo que uma requisição `TCP` volte como um erro `ICMP Time Exceeded` de um roteador no meio do caminho!) e retorna duas listas: **`ans` (pares `(estímulo, resposta)` respondidos)** e **`unans` (estímulos sem resposta)**!

## Exemplo
```python
# Enviar um probe TCP SYN na Camada 3 aguardando apenas a primeira resposta (sr1) com timeout e inspecionar as flags TCP retornadas
from scapy.all import IP, TCP, sr1

resp = sr1(IP(dst="192.0.2.10") / TCP(dport=443, flags="S"), timeout=2, verbose=0)
if resp and resp.haslayer(TCP):
    print(f"Flags TCP recebidas: {resp[TCP].flags}")
```

## Limites e trade-offs
Veja na verificação `resp[TCP].flags` acima como funciona um scanner TCP SYN em 4 linhas de Scapy: se o servidor alvo responder com **`SA` (`SYN+ACK`, `0x12`)**, a porta está aberta; se responder com **`RA` (`RST+ACK`, `0x14`)**, a porta está fechada; e se `resp` for `None` (ou voltar um `ICMP` tipo 3 código 13 *Communication Administratively Prohibited*), há um firewall filtrando o pacote!

## Como verificar
Atenção ao testar handshakes TCP manuais com o Scapy no Linux: quando o servidor remoto responde `SYN+ACK` para o seu pacote `SYN` forjado pelo Scapy, **o Kernel Linux local vê um `SYN+ACK` para um socket que o Kernel não abriu e envia automaticamente um `RST` que derruba a conexão**! Para impedir isso em laboratórios de teste TCP com Scapy, bloqueie o envio de `RST` do kernel para o IP de teste no `nftables`/`iptables` (`tcp flags rst drop`).

## Conexões
- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Veja também: Arquitetura do **Scapy (`secdev/scapy`)**: Construção e Dissecação de Pacotes de Rede em **Python**, Operador de Composição **`/`** e Sobrecarga Inteligente de Campos.
- [[scapy-geracao-conjuntos-pacotes-produto-cartesiano-packetlist]] — Veja também: Geração Declarativa de Conjuntos de Pacotes (**Produto Cartesiano de Campos**) e Manipulação de **`PacketList`** no Scapy.

## Fontes
- [Scapy Official GitHub Repository (`secdev/scapy`)](https://raw.githubusercontent.com/secdev/scapy/master/README.md) — repositório oficial da biblioteca e shell interativo Scapy em Python para manipulação, síntese, decodificação e auditoria de protocolos de rede das camadas 2 a 7; consultado em 2026-10-03.
- [Scapy Official Usage & Design Documentation (`doc/scapy/usage.rst`)](https://raw.githubusercontent.com/secdev/scapy/master/doc/scapy/usage.rst) — documentação oficial de uso do Scapy detalhando composição de camadas com `/`, pareamento estímulo-resposta (`sr`/`sr1`/`srp`), geração de conjuntos de pacotes e `fuzz()`; consultado em 2026-10-03.
