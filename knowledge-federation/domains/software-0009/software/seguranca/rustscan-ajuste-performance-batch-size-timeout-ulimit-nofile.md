---
id: software.seguranca.tranche08.000782
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

# RustScan: Engenharia de Performance e Confiabilidade — **Batch Size (`-b`)**, **Timeout (`-t`)**, Tries (`--tries`) e Limite de Descritores (**`--ulimit`**)

## Em uma frase
Como o RustScan abre conexões assíncronas via sockets do sistema operacional em lotes concorrentes (`FuturesUnordered`), no Linux cada tentativa de conexão simultânea consome um **File Descriptor (`fd`)**: se o limite de arquivos abertos do seu shell (`ulimit -n`, frequentemente apenas `1024` por padrão) for menor que o **`--batch-size` (`-b`, padrão `4500`)**, o sistema operacional recusará a abertura de novos sockets ou o RustScan reduzirá automaticamente o lote!

## Por que importa
Conforme documentado no `README.md` oficial do RustScan, três parâmetros controlam o equilíbrio entre velocidade extrema e zero falsos negativos: **(1) `--ulimit <valor>`** (ex.: `--ulimit 5000`, que usa a crate `rlimit` para elevar automaticamente o `RLIMIT_NOFILE` da sessão antes do scan!), **(2) `-b` / `--batch-size`** (quantas portas são sondadas simultaneamente por lote) e **(3) `-t` / `--timeout`** (tempo máximo de espera em milissegundos por porta, padrão `1500` ms = 1,5s).

## Como funciona
Em redes remotas com alta latência (VPNs transcontinentais ou links lentos) ou contra firewalls com controle de taxa, usar um `-b` muito alto (ex.: `10000`) causa perda de pacotes e falsos negativos; nesses cenários, reduza para **`-b 1000 -t 2500 --tries 2`** para precisão total!

## Exemplo
```bash
# Ajustar ulimit (5000 descritores), tamanho de lote (-b 1500), timeout (-t 2000ms) e tentativas (--tries 2) para links de VPN
rustscan -a 10.10.10.50 \
  --ulimit 5000 \
  -b 1500 \
  -t 2000 \
  --tries 2 \
  -- -sV -Pn
```

## Limites e trade-offs
Atenção ao diagnóstico clássico: se o RustScan reportar zero portas abertas em um host que você sabe que está ativo (ou encontrar menos portas em uma segunda execução), o problema é quase sempre **saturação do link/firewall pelo `--batch-size` alto demais ou `ulimit -n` baixo**; reduza `-b` para `500–1500` e aumente `-t` para `2000`.

## Como verificar
Verifique o limite atual de descritores do seu usuário Linux com `ulimit -n` e `ulimit -Hn` (hard limit).

## Conexões
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Veja também: **RustScan (`bee-san/RustScan`)**: Arquitetura Assíncrona em **Rust (`Tokio`)**, Varredura das 65.535 Portas e **Handoff Automático para o Nmap (`--`)**.
- [[rustscan-selecao-alvos-enderecos-cidr-hosts-file-ranges-portas]] — Veja também: RustScan: Especificação de Alvos (**`-a` IPs, Hostnames, Blocos CIDR e Arquivos de Hosts**), Faixas de Portas (`-r` / `-p`) e **`--exclude-ports`**.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
