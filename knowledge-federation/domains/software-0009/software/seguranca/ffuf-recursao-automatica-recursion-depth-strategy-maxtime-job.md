---
id: software.seguranca.tranche04.000337
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/ffuf/ffuf/master/README.md", "https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example", "https://github.com/ffuf/ffuf/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ffuf: Varredura Recursiva (`-recursion`, `-recursion-depth`, `-recursion-strategy`) e `-maxtime-job`

## Em uma frase
O modo recursivo do `ffuf` (`-recursion`) enfileira automaticamente novos jobs de fuzzing sempre que descobre um subdiretório válido, respeitando a profundidade máxima (`-recursion-depth`) e o limite de tempo por subdiretório (`-maxtime-job`).

## Por que importa
Automatiza o mapeamento de árvores profundas de APIs (`/api/v1/admin/reports/...`) sem exigir que o analista reinicie manualmente o scanner para cada subdiretório encontrado.

## Como funciona
A flag `-recursion-strategy` oferece dois comportamentos: `default` (que só entra em recursão quando o servidor responde com redirecionamento indicando diretório, ex.: `301 Moved Permanently` de `/admin` para `/admin/`) e `greedy` (que entra em recursão para **qualquer** resultado que der *match*, essencial para APIs REST que não emitem `301` em prefixos de rota).

## Exemplo
```bash
# Descoberta recursiva até profundidade 2 com limite de 60 segundos por subdiretório
ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt \
  -u https://api.staging.corp/FUZZ \
  -recursion -recursion-depth 2 \
  -recursion-strategy default \
  -maxtime-job 60 -ac
```

## Limites e trade-offs
Usar `-recursion-strategy greedy` sem uma calibração rigorosa (`-ac` ou filtros de status/tamanho) causa explosão de jobs na fila porque qualquer falso positivo de página gerará uma nova varredura completa da wordlist.

## Como verificar
Pressione `ENTER` para entrar no console interativo durante a execução e digite `queueshow` para inspecionar os jobs de recursão enfileirados e descartar ramos irrelevantes com `queuedel`.

## Conexões
- [[ffuf-modos-multi-wordlist-clusterbomb-pitchfork-sniper-encoders]] — Veja também: ffuf: Modos Multi-Wordlist (`clusterbomb`, `pitchfork`, `sniper`) e Encoders (`-enc`).
- [[ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo]] — Veja também: ffuf: Controle de Taxa (`-rate`, `-p`, `-t`), Circuit Breakers (`-sf`, `-se`, `-sa`) e Modo Interativo.
- [[ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos]] — Referência cruzada direta com ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos.
- [[ffuf-auto-calibration-ac-acs-acc-ach-eliminacao-soft-404]] — Referência cruzada direta com ffuf-auto-calibration-ac-acs-acc-ach-eliminacao-soft-404.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
