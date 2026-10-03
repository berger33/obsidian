---
id: software.seguranca.tranche09.000898
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

# Feroxbuster: Padronização Corporativa com **`ferox-config.toml`**, Controle de Fronteira (**`--scope`**) e Bloqueio (**`--dont-scan`**)

## Em uma frase
Conforme detalhado no arquivo oficial `ferox-config.toml.example`, o Feroxbuster procura automaticamente na inicialização um arquivo de configuração chamado **`ferox-config.toml`** (em `/etc/feroxbuster/`, `~/.config/feroxbuster/` ou no mesmo diretório do binário) para aplicar padrões de equipe sem precisar redigitar flags.

## Por que importa
Duas opções de governança de escopo no `ferox-config.toml` e na CLI são fundamentais porque o `--extract-links` analisa links encontrados no HTML/JS: **`--scope <dominios>`** (define quais domínios e seus subdomínios implícitos podem ser seguidos quando o Feroxbuster encontra links ou redirecionamentos `-r`) e **`--dont-scan <urls_ou_regex>`** (`url_denylist` e `regex_denylist` no TOML, que bloqueiam URLs ou padrões regex proibidos pelo ROE)!

## Como funciona
Além disso, você pode passar **múltiplas wordlists** na configuração (`wordlist = ["/caminho/lista1.txt", "/caminho/lista2.txt"]`), e o Feroxbuster mescla e deduplica todas as palavras em memória automaticamente!

## Exemplo
```toml
# ~/.config/feroxbuster/ferox-config.toml — Perfil padrao endurecido para pentests autorizados
threads = 25
scan_limit = 3
timeout = 7
auto_tune = true
collect_backups = true
dont_collect = ["png", "gif", "jpg", "jpeg", "svg", "css", "woff", "woff2", "ico"]
regex_denylist = ["/logout.*", "/signout.*", "/delete.*"]
replay_proxy = "http://127.0.0.1:8080"
replay_codes = [200, 201, 301, 302, 401, 403]
```

## Limites e trade-offs
Note no comentário oficial do `ferox-config.toml.example`: qualquer domínio fornecido em `scope = ["exemplo.com.br"]` autoriza implicitamente também subdomínios dele (`api.exemplo.com.br`), enquanto bloqueia links para domínios externos de terceiros.

## Como verificar
Execute `feroxbuster -u https://app.internal.corp -v` e verifique no cabeçalho de inicialização o carregamento das opções do `ferox-config.toml`.

## Conexões
- [[feroxbuster-autenticacao-mtls-request-file-headers-cookies-queries]] — Veja também: Feroxbuster: Auditoria Autenticada via **`--request-file` (Raw HTTP)**, Certificados **mTLS (`--client-cert`, `--client-key`)**, `-H`, `-b` e `-Q`.
- [[feroxbuster-pipelines-stdin-silent-json-encadeamento-httpx-nuclei]] — Veja também: Feroxbuster em Pipelines Unix: Leitura de Alvos via **`--stdin`**, Modo **`--silent` (`-q`)**, Saída **JSON Lines (`--json`)** e `--parallel`.
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.
- [[feroxbuster-encaminhamento-seletivo-replay-proxy-replay-codes-burp-mitmproxy]] — Referência cruzada direta com feroxbuster-encaminhamento-seletivo-replay-proxy-replay-codes-burp-mitmproxy.
- [[rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis]] — Referência cruzada direta com rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
