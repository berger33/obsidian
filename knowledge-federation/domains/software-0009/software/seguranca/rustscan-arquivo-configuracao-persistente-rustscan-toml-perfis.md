---
id: software.seguranca.tranche08.000786
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

# RustScan: Padronização de Equipe com o Arquivo de Configuração **`~/.rustscan.toml`** (`--config-path`)

## Em uma frase
Digitar repetidamente `--ulimit 5000 -b 1500 -t 2000 --Accessible --exclude-ports 9100` em todas as invocações manuais do dia a dia é propenso a esquecimentos; por isso, o RustScan lê automaticamente na inicialização um arquivo de configuração no formato **TOML** localizado em **`~/.rustscan.toml`** (ou em um caminho customizado passado via **`-c` / `--config-path /caminho/perfil.toml`**)!

## Por que importa
Dentro do `.rustscan.toml`, você pode definir padrões permanentes para `batch_size`, `timeout`, `tries`, `ulimit`, `greppable`, `accessible`, `scan_order`, `exclude_ports` e até as `flags` padrão que serão passadas para o Nmap quando você não especificar `--` na linha de comando.

## Como funciona
Criar perfis `.toml` separados para diferentes ambientes (ex.: `lan_fast.toml` com `batch_size = 4500` e `timeout = 1000`, vs `vpn_safe.toml` com `batch_size = 800` e `timeout = 2500`) padroniza a operação de toda a equipe de pentest.

## Exemplo
```toml
# /cases/pentest/vpn_safe.toml — Perfil de configuracao TOML do RustScan otimizado para conexoes de VPN
batch_size = 1000
timeout = 2500
tries = 2
ulimit = 5000
scan_order = "Random"
exclude_ports = [9100]
scripts = "default"
```

## Limites e trade-offs
Qualquer argumento passado explicitamente na linha de comando ao invocar `rustscan -c /cases/pentest/vpn_safe.toml` tem precedência sobre o valor definido no arquivo TOML.

## Como verificar
Valide o carregamento do perfil executando `rustscan -c /cases/pentest/vpn_safe.toml -a 127.0.0.1 -p 22,80,443 --scripts none`.

## Conexões
- [[rustscan-modos-saida-greppable-accessible-automacao-pipelines]] — Veja também: RustScan: Modo **`--greppable` (`-g`)** para Automação em Shell/Python e Modo **`--accessible`** para Acessibilidade e Logs Limpos.
- [[rustscan-motor-scripts-customizados-rustscan-scripts-toml-python-lua]] — Veja também: RustScan **Scripting Engine (`--scripts custom`)**: Automação Pós-Descoberta em Python, Shell, Lua ou Binários via **`.rustscan_scripts.toml`**.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile]] — Referência cruzada direta com rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
