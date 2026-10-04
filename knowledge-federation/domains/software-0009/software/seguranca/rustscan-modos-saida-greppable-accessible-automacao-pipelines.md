---
id: software.seguranca.tranche08.000785
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

# RustScan: Modo **`--greppable` (`-g`)** para Automação em Shell/Python e Modo **`--accessible`** para Acessibilidade e Logs Limpos

## Em uma frase
Quando você integra o RustScan dentro de um script Bash/Python de automação de reconhecimento ou pipeline de CI/CD, o banner ASCII art colorido, os spinners de progresso e a execução automática do Nmap atrapalham o parsing da saída.

## Por que importa
Para uso em scripts e pipelines, a flag **`-g` / `--greppable`** muda completamente o comportamento do RustScan: **(1)** ela desativa automaticamente a chamada ao Nmap e **(2)** imprime na saída padrão (`stdout`) exclusivamente uma linha limpa por host no formato **`IP -> [p1,p2,p3]`** (ex.: `10.10.10.50 -> [22,80,443,8080]`), pronta para ser processada por `awk`, `sed`, `jq` ou `cut`!

## Como funciona
Além disso, o RustScan foi pioneiro em ferramentas de segurança ao incluir a flag **`--accessible`**, que remove toda arte ASCII e formatação visual quebrada para **leitores de tela (*Screen Readers* usados por profissionais de segurança com deficiência visual)** e também gera logs limpos em arquivos de CI/CD!

## Exemplo
```bash
# Executar o RustScan em modo Greppable (-g) e Acessivel (--accessible) para extrair apenas a lista de portas abertas em scripts
rustscan -a 10.10.10.50 -g --accessible
```

## Limites e trade-offs
Veja como é simples transformar a saída de `rustscan -a 10.10.10.50 -g` em uma variável de portas no Bash: `PORTS=$(rustscan -a 10.10.10.50 -g | awk -F'[][]' '{print $2}')`!

## Como verificar
Teste combinar `rustscan -a 10.10.10.0/24 -g` com um loop que alimenta o **`httpx`** ou **`nuclei`** nas portas abertas descobertas.

## Conexões
- [[rustscan-ordem-varredura-scan-order-serial-random-evasao-ids]] — Veja também: RustScan: Ordem de Sondagem (**`--scan-order serial` vs `--scan-order random`**) e Comportamento Frente a Sistemas de Detecção de Intrusão (IDS).
- [[rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis]] — Veja também: RustScan: Padronização de Equipe com o Arquivo de Configuração **`~/.rustscan.toml`** (`--config-path`).
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[rustscan-motor-scripts-customizados-rustscan-scripts-toml-python-lua]] — Referência cruzada direta com rustscan-motor-scripts-customizados-rustscan-scripts-toml-python-lua.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
