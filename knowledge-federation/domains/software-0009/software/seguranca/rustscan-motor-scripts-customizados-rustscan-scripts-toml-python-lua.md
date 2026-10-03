---
id: software.seguranca.tranche08.000787
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

# RustScan **Scripting Engine (`--scripts custom`)**: Automação Pós-Descoberta em Python, Shell, Lua ou Binários via **`.rustscan_scripts.toml`**

## Em uma frase
Embora o comportamento padrão do RustScan (`--scripts default`) seja chamar o `nmap`, a arquitetura do RustScan na verdade possui um **Motor de Scripts Genérico (*RustScan Scripting Engine*)** controlado pela flag **`--scripts <none|default|custom>`**!

## Por que importa
Quando executado com **`--scripts custom`**, o RustScan lê o arquivo **`~/.rustscan_scripts.toml`** e os scripts contidos no diretório configurado: cada script inclui cabeçalhos de metadados (**`tags`**, **`developer`**, **`ports_separator`**, **`call_format`**) e recebe do RustScan as variáveis **`{{ip}}`** e **`{{port}}`** das portas abertas recém-descobertas.

## Como funciona
Se um script tiver `ports = ["80", "443", "8080", "8443"]` no seu cabeçalho, o RustScan **só disparará aquele script automaticamente quando encontrar pelo menos uma daquelas portas HTTP abertas no alvo** — permitindo acionar automaticamente `nuclei`, `gobuster dir`, `nikto` ou `testssl.sh` conforme as portas descobertas!

## Exemplo
```python
#!/usr/bin/env python3
# tags = ["core_approved", "http_audit"]
# developer = [ "SecOps Team", "https://internal.corp" ]
# trigger_port = ["80", "443", "8080", "8443"]
# call_format = "python3 {{script}} {{ip}} {{port}}"
# ports_separator = ","

import sys
ip, ports = sys.argv[1], sys.argv[2]
print(f"[+] RustScan Custom Trigger: Host {ip} abriu portas web [{ports}] -> pronto para httpx/nuclei!")
```

## Limites e trade-offs
No arquivo `~/.rustscan_scripts.toml`, o filtro **`tags = ["core_approved", "http_audit"]`** define que apenas os scripts que possuam **todas** as tags listadas serão executados, impedindo a execução acidental de scripts experimentais ou intrusivos.

## Como verificar
Teste o motor sem executar os comandos reais ou listando a configuração antes de rodar em produção.

## Conexões
- [[rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis]] — Veja também: RustScan: Padronização de Equipe com o Arquivo de Configuração **`~/.rustscan.toml`** (`--config-path`).
- [[rustscan-execucao-container-docker-ulimit-rede-host-alias]] — Veja também: RustScan em Containers **Docker (`rustscan/rustscan`)**: Configuração de `--network host`, `ulimit` do Container e Montagem de Volumes para o Nmap.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[rustscan-modos-saida-greppable-accessible-automacao-pipelines]] — Referência cruzada direta com rustscan-modos-saida-greppable-accessible-automacao-pipelines.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
