---
id: software.seguranca.tranche09.000899
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

# Feroxbuster em Pipelines Unix: Leitura de Alvos via **`--stdin`**, Modo **`--silent` (`-q`)**, Saída **JSON Lines (`--json`)** e `--parallel`

## Em uma frase
O Feroxbuster foi projetado para se comportar como um cidadão de primeira classe em pipelines Unix: passando a flag **`--stdin`**, ele lê uma lista de URLs diretamente da entrada padrão (por exemplo, vinda do **`httpx`** ou **`katana`**) e com **`--parallel <N>`** controla quantos hosts da entrada `stdin` são varridos simultaneamente!

## Por que importa
Quando você adiciona a flag **`--silent` (`-q`)**, o Feroxbuster desativa barras de progresso e banners e imprime em `stdout` **exclusivamente as URLs descobertas (uma URL limpa por linha)** — permitindo canalizar a saída diretamente via pipe para outra ferramenta (`| nuclei`, `| arjun`, `| dalfox`)!

## Como funciona
E para armazenamento estruturado e análise com `jq`, adicionar **`--json`** junto com **`-o resultados.jsonl`** grava cada resposta descoberta como um objeto JSON rico contendo `url`, `path`, `status`, `content_length`, `line_count`, `word_count`, `headers` e `extension`!

## Exemplo
```bash
# Pipeline Unix: ler URLs vivas do httpx via --stdin, rodar ate 4 hosts em paralelo (--parallel 4) e gravar JSONL estruturado
cat /cases/easm/live_web_assets.txt \
  | feroxbuster --stdin \
    --parallel 4 \
    --scan-limit 2 \
    --threads 20 \
    --depth 2 \
    --silent \
    --json -o /cases/easm/ferox_all_hosts.jsonl
```

## Limites e trade-offs
Veja como combinar `--parallel 4` + `--scan-limit 2` + `--threads 20` dá controle matemático total da concorrência máxima de rede: no máximo `4 hosts × 2 diretórios × 20 threads = 160` requisições em voo simultaneamente.

## Como verificar
Filtre no arquivo `ferox_all_hosts.jsonl` rotas administrativas ou arquivos de configuração expostos com `jq -r 'select(.status == 200) | .url' /cases/easm/ferox_all_hosts.jsonl`.

## Conexões
- [[feroxbuster-configuracao-persistente-ferox-config-toml-escopo]] — Veja também: Feroxbuster: Padronização Corporativa com **`ferox-config.toml`**, Controle de Fronteira (**`--scope`**) e Bloqueio (**`--dont-scan`**).
- [[feroxbuster-comparacao-feroxbuster-vs-ffuf-vs-gobuster-vs-katana]] — Veja também: Decisão Arquitetural de Descoberta Web: Quando Usar **Feroxbuster** vs **`ffuf`** vs **Gobuster** vs **Katana** em Pentests e EASM.
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.
- [[arjun-integracao-pipeline-katana-arjun-dalfox-sqlmap-nuclei]] — Referência cruzada direta com arjun-integracao-pipeline-katana-arjun-dalfox-sqlmap-nuclei.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
