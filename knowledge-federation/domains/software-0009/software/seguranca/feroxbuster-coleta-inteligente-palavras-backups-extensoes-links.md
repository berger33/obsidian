---
id: software.seguranca.tranche09.000894
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

# Feroxbuster: Geração Dinâmica de Wordlist a partir do Alvo (**`--collect-words` (`-g`)**, **`--collect-backups` (`-B`)**, **`--collect-extensions` (`-E`)** e `--extract-links`)

## Em uma frase
Três flags do Feroxbuster transformam o scanner de um testador de dicionário estático em um motor adaptativo que aprende o vocabulário do próprio site alvo em tempo de execução: **`-g` / `--collect-words`**, **`-B` / `--collect-backups`** e **`-E` / `--collect-extensions`**!

## Por que importa
Com **`-g` (`--collect-words`)**, o Feroxbuster extrai substantivos, identificadores e jargões específicos do negócio encontrados dentro do texto e metadados das páginas respondidas pelo servidor e **os adiciona dinamicamente à wordlist em memória**! Com **`-B` (`--collect-backups`)**, toda vez que o Feroxbuster encontra um arquivo real (ex.: `config.php` ou `login.jsp`), ele testa automaticamente variações de backup daquele arquivo exato (`config.php.bak`, `config.php~`, `config.php.old`, `.config.php.swp`, `config.bak`)!

## Como funciona
E com **`-E` (`--collect-extensions`)**, o Feroxbuster descobre quais extensões de arquivo o servidor realmente utiliza na prática (ignorando imagens/fontes listadas em `--dont-collect png,jpg,gif,css,woff2`) e passa a anexá-las automaticamente!

## Exemplo
```bash
# Executar o Feroxbuster aprendendo palavras do proprio alvo (-g), testando backups de cada arquivo achado (-B) e coletando extensoes (-E)
feroxbuster -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt \
  --collect-words \
  --collect-backups \
  --collect-extensions \
  --dont-collect png,jpg,jpeg,gif,svg,css,woff,woff2,ico \
  -o /cases/pentest/ferox_smart_collection.txt
```

## Limites e trade-offs
Por que **`-B` (`--collect-backups`)** é muito mais eficiente do que passar `-x bak,old,swp,orig` para toda a wordlist? Porque `-x bak,old,swp` multiplica a wordlist inteira de 30.000 palavras por 4 (`120.000` requisições), enquanto `-B` testa `.bak`/`.old`/`.swp` **apenas para os 15 arquivos que realmente foram encontrados** (`60` requisições cirúrgicas)!

## Como verificar
Verifique na saída do Feroxbuster os arquivos de backup (`.bak`, `~`, `.swp`) descobertos automaticamente pelo `-B`.

## Conexões
- [[feroxbuster-filtragem-precisa-status-size-words-lines-regex-similar]] — Veja também: Feroxbuster: Filtros Multi-Dimensionais (`-C`, `-S`, `-W`, `-N`, `-X`) e **Filtro de Similaridade Fuzzy (`--filter-similar-to`)** contra *Soft-404 Dinâmicos*.
- [[feroxbuster-gerenciamento-estado-state-file-resume-from-time-limit]] — Veja também: Feroxbuster: Persistência de Estado (**`ferox-*.state`**), Retomada Exata (**`--resume-from`**) e Orçamento de Tempo (**`--time-limit`**).
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.
- [[gobuster-padroes-arquivos-patterns-p-wordlists-dinamicas-backups]] — Referência cruzada direta com gobuster-padroes-arquivos-patterns-p-wordlists-dinamicas-backups.
- [[wpscan-descoberta-backups-config-exports-db-timthumbs-medias]] — Referência cruzada direta com wpscan-descoberta-backups-config-exports-db-timthumbs-medias.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
