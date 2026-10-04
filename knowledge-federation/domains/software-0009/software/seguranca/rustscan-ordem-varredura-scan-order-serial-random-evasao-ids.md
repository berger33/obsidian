---
id: software.seguranca.tranche08.000784
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

# RustScan: Ordem de Sondagem (**`--scan-order serial` vs `--scan-order random`**) e Comportamento Frente a Sistemas de Detecção de Intrusão (IDS)

## Em uma frase
Por padrão, o RustScan sonda as portas em ordem sequencial crescente (**`--scan-order serial`**: `1, 2, 3, ..., 65535`), o que tem a vantagem prática de mostrar primeiro as portas baixas mais conhecidas (`22`, `80`, `443`, `445`) logo nos primeiros milissegundos da execução.

## Por que importa
Contudo, muitos sistemas de detecção de intrusão (IDS/IPS) e firewalls locais possuem heurísticas simples que bloqueiam imediatamente qualquer IP que tente conectar em 10 portas sequenciais consecutivas (`1, 2, 3, 4, 5...`).

## Como funciona
Passar a flag **`--scan-order random`** instrui o RustScan a embaralhar pseudo-aleatoriamente (usando a crate `rand`) o vetor de todas as portas antes de dividi-lo nos lotes de `--batch-size`, evitando padrões sequenciais previsíveis e distribuindo a carga ao longo do espectro de 65.535 portas.

## Exemplo
```bash
# Executar o RustScan embaralhando aleatoriamente a ordem das portas (--scan-order random) com lote moderado
rustscan -a 10.10.10.50 \
  --scan-order random \
  -b 500 -t 2000 \
  -- -sV -T3
```

## Limites e trade-offs
Tenha em mente os limites reais de `--scan-order random`: embaralhar a ordem das portas evita heurísticas ingênuas de portas sequenciais, mas **qualquer IDS moderno (como Suricata ou Zeek) que contabilize o volume total de conexões `SYN` recusadas (`RST`) por segundo continuará detectando uma varredura de 65.535 portas em 3 segundos**!

## Como verificar
Para testes furtivos onde o ROE exige discrição contra o SOC, o RustScan de alta velocidade não é a ferramenta indicada; nesses casos, prefira o Nmap em portas pontuais selecionadas com `-T2` / `--scan-delay`.

## Conexões
- [[rustscan-selecao-alvos-enderecos-cidr-hosts-file-ranges-portas]] — Veja também: RustScan: Especificação de Alvos (**`-a` IPs, Hostnames, Blocos CIDR e Arquivos de Hosts**), Faixas de Portas (`-r` / `-p`) e **`--exclude-ports`**.
- [[rustscan-modos-saida-greppable-accessible-automacao-pipelines]] — Veja também: RustScan: Modo **`--greppable` (`-g`)** para Automação em Shell/Python e Modo **`--accessible`** para Acessibilidade e Logs Limpos.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile]] — Referência cruzada direta com rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
