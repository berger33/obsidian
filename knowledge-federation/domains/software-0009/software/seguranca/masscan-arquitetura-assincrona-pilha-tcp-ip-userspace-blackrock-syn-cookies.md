---
id: software.seguranca.tranche08.000771
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md", "https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown", "https://github.com/robertdavidgraham/masscan"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **Masscan (`robertdavidgraham/masscan`)**: Arquitetura Assíncrona *Stateless*, Pilha TCP/IP em User-Space, **Cifra BlackRock** e *SYN Cookies*

## Em uma frase
Criado por Robert David Graham, o **Masscan** (`robertdavidgraham/masscan`, licença AGPLv3) é o scanner de portas TCP/UDP mais rápido disponível, projetado para varrer a internet IPv4 inteira (ou redes corporativas Classe A `10.0.0.0/8` inteiras) a taxas de até **10 a 25 milhões de pacotes por segundo** a partir de uma única máquina com driver `PF_RING` DNA / raw sockets.

## Por que importa
Conforme detalhado no manual oficial `doc/masscan.8.markdown`, a velocidade extrema do Masscan vem de três pilares arquiteturais: **(1) Transmissão e Recepção Assíncronas Desacopladas (*Stateless*)** — a thread de envio dispara pacotes `SYN` sem guardar tabela de conexões em memória RAM, enquanto a thread de recepção valida os `SYN-ACK` retornados usando **SYN Cookies criptográficos** no número de sequência TCP; **(2) Pilha TCP/IP Própria em User-Space** que faz bypass da pilha de sockets do kernel; e **(3) Randomização Matemática Total via Cifra Feistel `BlackRock`**!

## Como funciona
Graças à cifra **BlackRock** (uma rede Feistel de alcance arbitrário $N = \text{total de IPs} \times \text{total de portas}$), o Masscan **nunca** varre o IP `10.0.0.1` sequencialmente e **nunca** precisa alocar um array de bilhões de IPs na RAM: ele aplica uma bijeção matemática `BlackRock(i)` sobre o contador $i = 0 \dots N-1$, espalhando os pacotes de forma 100% aleatória por todas as sub-redes e portas!

## Exemplo
```bash
# Verificar a versao do Masscan e testar uma varredura simulada (--offline) para validar a sintaxe e a taxa de pacotes
masscan --version
masscan 10.0.0.0/8 -p80,443 --rate 10000 --offline
```

## Limites e trade-offs
Atenção ao aviso fundamental do `README.md` oficial: a taxa padrão do Masscan é de apenas **`100` pacotes/segundo** (`--rate 100`), mas se você configurar `--rate 1000000` sem entender a capacidade do seu switch, firewall stateful ou roteador de borda, **você esgotará a tabela `conntrack`/NAT do roteador local e derrubará a rede em segundos**!

## Como verificar
Use sempre a flag **`--offline`** primeiro para testar os parâmetros da linha de comando sem transmitir nenhum pacote real na placa de rede.

## Conexões
- [[masscan-captura-banners-pilha-tcp-conflito-kernel-rst-source-ip-iptables]] — Veja também: Masscan **`--banners`**: Como Resolver o Conflito de **Pacotes `RST` do Kernel Linux** usando **`--source-ip` Dedicado** ou **`--adapter-port` + `iptables`/`nftables`**.
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Referência cruzada direta com masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede.
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Referência cruzada direta com zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
