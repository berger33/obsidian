---
id: software.seguranca.tranche08.000790
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

# RustScan em Redes **IPv6 e Dual-Stack**: Varredura de Endereços IPv6, Resolução Assíncrona (`hickory-resolver`) e Mitigação de Exaustão de *Conntrack* Local

## Em uma frase
Enquanto scanners baseados em permutação de inteiros de 32 bits ou pilhas IPv4 legadas têm suporte limitado ou separado para IPv6, o RustScan utiliza o tipo nativo `std::net::IpAddr` (`Ipv4Addr` e `Ipv6Addr`) do Rust e a biblioteca `tokio`, permitindo varrer todas as 65.535 portas TCP de um **endereço IPv6 (`2001:db8::1`) ou hostname Dual-Stack** exatamente com a mesma sintaxe!

## Por que importa
Ao passar um nome de domínio em `-a app.exemplo.com.br`, o resolvedor assíncrono do RustScan consulta os registros DNS e inicia a varredura sobre os endereços resolvidos.

## Como funciona
Entretanto, existe um cuidado importante na própria máquina Linux do analista ao rodar o RustScan com `-b 4500` em múltiplos hosts seguidos: como o RustScan usa `connect()` do kernel, se o firewall local da sua própria estação (`ufw` / `firewalld` / `nftables`) estiver rastreando conexões de saída (`OUTPUT conntrack`), abrir 65.535 conexões TCP em 3 segundos pode encher a tabela **`nf_conntrack` da sua própria máquina de pentest**!

## Exemplo
```bash
# Varrer as 65.535 portas TCP de um servidor IPv6 com o RustScan e repassar as portas abertas para o Nmap em modo IPv6 (-6)
rustscan -a 2001:db8:10::50 \
  -b 1500 -t 2000 --ulimit 5000 \
  -- -6 -sV -sC
```

## Limites e trade-offs
Observe a flag **`-6`** passada após o **`--`**: quando o alvo é um endereço **IPv6**, o Nmap exige a flag `-6` para habilitar o modo IPv6, portanto sempre inclua `-- -6 -sV` ao final do comando do RustScan!

## Como verificar
Se notar erro `Too many open files` ou `Resource temporarily unavailable` na sua estação de pentest durante varreduras intensas, aumente `net.netfilter.nf_conntrack_max` na sua máquina (`sudo sysctl -w net.netfilter.nf_conntrack_max=524288`) e use `--ulimit 10000`.

## Conexões
- [[rustscan-comparacao-arquitetural-rustscan-vs-masscan-vs-nmap-vs-zmap]] — Veja também: Decisão Arquitetural de Scanners de Portas: Quando Usar **RustScan** vs **Masscan** vs **ZMap** vs **Nmap** em Engajamentos Reais.
- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — Referência cruzada direta com rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap.
- [[rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile]] — Referência cruzada direta com rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile.
- [[masscan-deteccao-defensiva-syn-cookies-suricata-zeek-conntrack-tuning]] — Referência cruzada direta com masscan-deteccao-defensiva-syn-cookies-suricata-zeek-conntrack-tuning.

## Fontes
- [RustScan Official GitHub — The Modern Port Scanner & Automatic Nmap Integration](https://raw.githubusercontent.com/bee-san/RustScan/master/README.md) — documentação oficial do RustScan cobrindo varredura assíncrona de 65.535 portas, handoff para o Nmap, batch-size, ulimit, accessible e Docker; consultado em 2026-10-03.
- [RustScan Official Cargo Manifest — Tokio Async Runtime & Hickory DNS Dependencies](https://raw.githubusercontent.com/bee-san/RustScan/master/Cargo.toml) — especificação oficial de dependências e crates do RustScan (tokio, futures, rlimit, cidr-utils, hickory-resolver); consultado em 2026-10-03.
- [RustScan Official Wiki — Configuration File & Custom Scripting Engine](https://github.com/bee-san/RustScan/wiki) — wiki oficial do RustScan cobrindo o arquivo .rustscan.toml e o motor de scripts customizados .rustscan_scripts.toml; consultado em 2026-10-03.
