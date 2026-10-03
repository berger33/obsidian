---
id: software.seguranca.tranche09.000900
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md", "https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example", "https://epi052.github.io/feroxbuster-docs/overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Decisão Arquitetural de Descoberta Web: Quando Usar **Feroxbuster** vs **`ffuf`** vs **Gobuster** vs **Katana** em Pentests e EASM

## Em uma frase
Como o nosso lote de segurança cobre **Feroxbuster**, **`ffuf`**, **Gobuster** e **Katana**, saber escolher a ferramenta exata (ou a combinação delas) para cada tarefa de descoberta web é uma competência essencial de engenharia de AppSec e Red Team.

## Por que importa
Compare a especialidade arquitetural de cada uma: **(1) Katana (`projectdiscovery/katana`)**: é um **Crawler / Spider** (navega por links existentes e faz parsing profundo de arquivos JavaScript/DOM Headless, sem fazer força bruta de dicionário); **(2) Feroxbuster (`epi052/feroxbuster`)**: é o especialista em **Descoberta Recursiva Forçada de Diretórios/Arquivos** (combina wordlist + extração de links + `--collect-words`/`--collect-backups` + `--filter-similar-to` + `--replay-proxy`); **(3) `ffuf` (`ffuf/ffuf`)**: é o **Fuzzer HTTP Paramétrico Mais Flexível** (suporta múltiplas wordlists em modos `sniper`/`pitchfork`/`clusterbomb` em qualquer posição da requisição crua); e **(4) Gobuster (`OJ/gobuster`)**: é o enumerador multi-protocolo em Go com modos dedicados para **`dns`, `vhost`, `s3`, `gcs` e `tftp`**!

## Como funciona
Em um pentest web completo, o fluxo de ouro começa com **`katana`** (mapeia tudo que está linkado no HTML/JS), segue com **`feroxbuster`** (descobre recursivamente diretórios e backups não-linkados e os envia via `--replay-proxy` para o `mitmproxy`), usa **`arjun`** (descobre parâmetros ocultos nas rotas) e usa **`ffuf`** para fuzzing combinatório de parâmetros!

## Exemplo
```bash
# Fluxo integrado: Feroxbuster descobre rotas ocultas recursivamente e alimenta o Arjun para descobrir parametros ocultos nelas!
feroxbuster -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/quickhits.txt \
  --collect-backups \
  --silent -o /cases/pentest/ferox_discovered_urls.txt

arjun -i /cases/pentest/ferox_discovered_urls.txt -w small -oJ /cases/pentest/ferox_arjun_params.json
```

## Limites e trade-offs
Adote também a flag **`--unique`** do Feroxbuster (`unique = true` no `ferox-config.toml`) quando auditar aplicações que possuem dezenas de subpastas espelhadas retornando páginas idênticas: o `--unique` deduplica respostas idênticas para manter o relatório enxuto.

## Como verificar
Verifique os resultados consolidados no `mitmproxy` e no relatório JSON do Arjun.

## Conexões
- [[feroxbuster-pipelines-stdin-silent-json-encadeamento-httpx-nuclei]] — Veja também: Feroxbuster em Pipelines Unix: Leitura de Alvos via **`--stdin`**, Modo **`--silent` (`-q`)**, Saída **JSON Lines (`--json`)** e `--parallel`.
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Referência cruzada direta com gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
