---
id: software.seguranca.tranche08.000783
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
fontes: ["https://raw.githubusercontent.com/bee-san/RustScan/master/README.md", "https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml", "https://github.com/bee-san/RustScan/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# RustScan: Especificação de Alvos (**`-a` IPs, Hostnames, Blocos CIDR e Arquivos de Hosts**), Faixas de Portas (`-r` / `-p`) e **`--exclude-ports`**

## Em uma frase
A flag **`-a` / `--addresses`** do RustScan é polimórfica e aceita na mesma opção: **(1)** uma lista de IPs ou domínios separados por vírgula (`-a 10.10.10.1,10.10.10.2,app.internal.corp`), **(2)** notação de sub-rede **CIDR** (`-a 10.10.10.0/24`, expandida pela crate `cidr-utils`), e **(3)** o caminho para um **arquivo texto contendo um host/IP por linha** (`-a /cases/pentest/targets.txt`)!

## Por que importa
Quanto à seleção de portas, por padrão o RustScan varre o intervalo **`1–65535`** (ou você pode restringir um intervalo com **`-r` / `--range 1-10000`**, passar uma lista específica com **`-p` / `--ports 22,80,443,8080,8443`** e excluir portas problemáticas com **`-e` / `--exclude-ports 9100`**).

## Como funciona
Para resolução de nomes DNS, conforme mostra o `Cargo.toml` oficial, o RustScan integra a biblioteca moderna **`hickory-resolver`** (com suporte a DNS-over-Rustls) para resolver assincronamente múltiplos hostnames antes de iniciar a varredura de portas.

## Exemplo
```bash
# Varrer as primeiras 10.000 portas de uma lista de ativos (-a arquivo.txt) excluindo a porta 9100 de impressoras JetDirect
rustscan -a /cases/pentest/scope_hosts.txt \
  -r 1-10000 \
  --exclude-ports 9100 \
  -b 1500 --ulimit 5000 \
  --scripts none
```

## Limites e trade-offs
Sempre inclua **`--exclude-ports 9100`** ao varrer sub-redes de escritórios corporativos: a porta `9100/TCP` (*HP JetDirect / Raw Print*) de impressoras de rede imprime fisicamente em papel qualquer byte recebido se um scanner conectar ou se o Nmap `-sV` enviar probes de detecção de serviço!

## Como verificar
Confirme que a lista de alvos em `scope_hosts.txt` não contém linhas em branco malformadas ou IPs fora do escopo autorizado.

## Conexões
- [[rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile]] — Veja também: RustScan: Engenharia de Performance e Confiabilidade — **Batch Size (`-b`)**, **Timeout (`-t`)**, Tries (`--tries`) e Limite de Descritores (**`--ulimit`**).
- [[rustscan-ordem-varredura-scan-order-serial-random-evasao-ids]] — Veja também: RustScan: Ordem de Sondagem (**`--scan-order serial` vs `--scan-order random`**) e Comportamento Frente a Sistemas de Detecção de Intrusão (IDS).
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Referência cruzada direta com masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
