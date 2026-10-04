---
id: software.seguranca.tranche09.000891
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

# **Feroxbuster (`epi052/feroxbuster`)**: Arquitetura de **Descoberta Recursiva de Conteúdo Web (*Forced Browsing*)** em Rust (`tokio`)

## Em uma frase
**Feroxbuster** (`epi052/feroxbuster`, licença MIT, escrito em Rust assíncrono por Ben Risher / `@epi052`) é uma ferramenta de alta performance projetada especificamente para **Forced Browsing (Enumeração Recursiva de Diretórios e Arquivos Web)**.

## Por que importa
Enquanto enumeradores tradicionais exigem que você rode um novo comando manualmente para cada subdiretório encontrado (ou têm recursão sequencial lenta), o Feroxbuster gerencia uma fila concorrente de diretórios controlando simultaneamente **quantos diretórios são varridos em paralelo (`--scan-limit` / `-L`)** e **quantas threads assíncronas operam dentro de cada diretório (`--threads` / `-t`, padrão `50`)**, até a profundidade máxima **`--depth` (`-d`, padrão `4`)**!

## Como funciona
Além disso, durante a própria varredura de wordlist, o Feroxbuster faz **Parsing Ativo do Corpo das Respostas (`--extract-links`, ativo por padrão!)** procurando novos caminhos referenciados no HTML, JavaScript e `robots.txt` para adicioná-los automaticamente à árvore de recursão!

## Exemplo
```bash
# Verificar a versao do Feroxbuster e executar descoberta recursiva com multiplas extensoes (-x) e limite de 4 scans simultaneos (-L 4)
feroxbuster --version
feroxbuster -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt \
  -x php,json,txt,bak \
  -t 30 -L 4 -d 3 \
  -o /cases/pentest/ferox_recursive.txt
```

## Limites e trade-offs
Atenção ao alerta oficial de segurança no topo do `README.md` do projeto: o domínio `feroxbuster.com` **não** pertence aos autores do projeto; baixe o Feroxbuster **exclusivamente** do repositório oficial no GitHub (`https://github.com/epi052/feroxbuster/releases`), `crates.io` ou repositórios oficiais da distribuição!

## Como verificar
Use `-n` (`--no-recursion`) quando quiser desativar a recursão e enumerar apenas o nível atual da URL informada.

## Conexões
- [[feroxbuster-protecao-inteligente-auto-tune-auto-bail-rate-limit]] — Veja também: Feroxbuster: Adaptação Inteligente de Taxa (**`--auto-tune`**), Aborto Automático de Erros (**`--auto-bail`**) e Limite Explícito (**`--rate-limit`**).
- [[feroxbuster-filtragem-precisa-status-size-words-lines-regex-similar]] — Referência cruzada direta com feroxbuster-filtragem-precisa-status-size-words-lines-regex-similar.
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Referência cruzada direta com gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
