---
id: software.seguranca.tranche08.000781
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

# **RustScan (`bee-san/RustScan`)**: Arquitetura Assíncrona em **Rust (`Tokio`)**, Varredura das 65.535 Portas e **Handoff Automático para o Nmap (`--`)**

## Em uma frase
**RustScan** (`bee-san/RustScan` / `rustscan/rustscan`, licença GPLv3, escrito em Rust sobre o runtime assíncrono **`tokio`** e `FuturesUnordered`) é um scanner de portas moderno projetado com uma filosofia direta: **descobrir todas as portas TCP abertas (`1–65535`) de um alvo em poucos segundos usando I/O assíncrono em Rust e invocar automaticamente o Nmap apenas nas portas abertas descobertas**!

## Por que importa
Diferente do Masscan (que exige `root` para injetar pacotes Ethernet brutos e pode ter conflito de `RST` com o kernel), o RustScan utiliza conexões assíncronas não-bloqueantes **`tokio::net::TcpStream`** através da pilha do sistema operacional: isso permite rodá-lo mesmo como usuário comum sem privilégios de `root` e sobre interfaces de **VPN (`tun0`), túneis SSH / `proxychains` e redes IPv6** onde raw sockets Ethernet falham!

## Como funciona
Qualquer argumento colocado após o separador **`--`** no final da linha de comando do RustScan (por exemplo, **`rustscan -a 10.10.10.50 -- -sV -sC -oA scan_detalhado`**) é repassado diretamente para o comando `nmap` gerado automaticamente pelo RustScan junto com `-vvv -p <portas_abertas>`!

## Exemplo
```bash
# Verificar a versao do RustScan e varrer todas as 65.535 portas de um host passando as portas abertas automaticamente para o Nmap (-sV -sC)
rustscan --version
rustscan -a 10.10.10.50 -- -sV -sC -oA /cases/pentest/rustscan_nmap_host50
```

## Limites e trade-offs
Por que o RustScan funciona perfeitamente sobreinterfaces **`tun0` (OpenVPN / WireGuard)** onde ferramentas baseadas em Ethernet L2 às vezes exigem configuração manual de MAC? Porque o `tokio::net::TcpStream` delega o roteamento L3/L2 ao kernel do sistema operacional!

## Como verificar
Se quiser apenas descobrir as portas abertas em segundos **sem** iniciar o Nmap ao final, basta passar a flag **`--scripts none`** (ou **`-g` / `--greppable`**).

## Conexões
- [[rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile]] — Veja também: RustScan: Engenharia de Performance e Confiabilidade — **Batch Size (`-b`)**, **Timeout (`-t`)**, Tries (`--tries`) e Limite de Descritores (**`--ulimit`**).
- [[rustscan-modos-saida-greppable-accessible-automacao-pipelines]] — Referência cruzada direta com rustscan-modos-saida-greppable-accessible-automacao-pipelines.
- [[masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo]] — Referência cruzada direta com masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
