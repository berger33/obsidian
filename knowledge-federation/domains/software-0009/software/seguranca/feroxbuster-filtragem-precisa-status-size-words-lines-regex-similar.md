---
id: software.seguranca.tranche09.000893
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

# Feroxbuster: Filtros Multi-Dimensionais (`-C`, `-S`, `-W`, `-N`, `-X`) e **Filtro de Similaridade Fuzzy (`--filter-similar-to`)** contra *Soft-404 Dinâmicos*

## Em uma frase
Assim como o `ffuf`, o Feroxbuster permite filtrar respostas indesejadas por cinco dimensões clássicas: **`-C` / `--filter-status`** (código HTTP, ex.: `-C 404,400`), **`-S` / `--filter-size`** (tamanho em bytes), **`-W` / `--filter-words`** (contagem de palavras), **`-N` / `--filter-lines`** (contagem de linhas) e **`-X` / `--filter-regex`** (expressão regular no corpo ou cabeçalhos)!

## Por que importa
Mas e quando uma página "Soft 404" muda simultaneamente o tamanho em bytes, o número de palavras e o número de linhas a cada requisição (porque inclui um feed de notícias aleatório ou stack trace dinâmico)?

## Como funciona
O Feroxbuster resolve isso com a flag exclusiva **`--filter-similar-to <URL_EXEMPLO_DE_ERRO>`** (`filter_similar` no `ferox-config.toml`): ele busca a página de erro informada, calcula o **hash de similaridade (*Fuzzy Hash / SimHash*)** da estrutura da página e **descarta automaticamente qualquer resposta cujo conteúdo seja estruturalmente similar àquela página Soft-404**!

## Exemplo
```bash
# Filtrar paginas Soft-404 dinamicas usando comparacao de similaridade fuzzy (--filter-similar-to) e regex (-X)
feroxbuster -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/common.txt \
  --filter-similar-to https://app.internal.corp/caminho-inexistente-padrao-404 \
  --filter-status 404,429 \
  --filter-regex "Rota nao encontrada no gateway" \
  -o /cases/pentest/ferox_clean.txt
```

## Limites e trade-offs
Antes de iniciar cada diretório, o próprio Feroxbuster já realiza testes automáticos de *Wildcard* com UUIDs aleatórios e cria filtros `-S` / `-W` automaticamente; só passe `--dont-filter` (`-D`) se você quiser desativar explicitamente esse filtro automático de wildcard.

## Como verificar
Teste `--filter-similar-to` contra SPAs em React/Vue/Angular ou portais corporativos que renderizam páginas de erro dinâmicas.

## Conexões
- [[feroxbuster-protecao-inteligente-auto-tune-auto-bail-rate-limit]] — Veja também: Feroxbuster: Adaptação Inteligente de Taxa (**`--auto-tune`**), Aborto Automático de Erros (**`--auto-bail`**) e Limite Explícito (**`--rate-limit`**).
- [[feroxbuster-coleta-inteligente-palavras-backups-extensoes-links]] — Veja também: Feroxbuster: Geração Dinâmica de Wordlist a partir do Alvo (**`--collect-words` (`-g`)**, **`--collect-backups` (`-B`)**, **`--collect-extensions` (`-E`)** e `--extract-links`).
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.
- [[nikto-tratamento-soft-404-no404-db-404-strings-falso-positivo]] — Referência cruzada direta com nikto-tratamento-soft-404-no404-db-404-strings-falso-positivo.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
