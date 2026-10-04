---
id: software.seguranca.tranche09.000895
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

# Feroxbuster: Persistência de Estado (**`ferox-*.state`**), Retomada Exata (**`--resume-from`**) e Orçamento de Tempo (**`--time-limit`**)

## Em uma frase
Varreduras recursivas profundas sobre grandes portais corporativos podem descobrir dezenas de subdiretórios: se a conexão VPN cair ou se a janela de manutenção autorizada do cliente encerrar às 06:00 da manhã, perder horas de enumeração recursiva seria frustrante.

## Por que importa
Por padrão, sempre que uma varredura do Feroxbuster é interrompida com `Ctrl+C` ou atinge o limite de tempo configurado por **`--time-limit` (ex.: `--time-limit 30m`)**, o Feroxbuster serializa em disco um arquivo **`ferox-<slug>-<timestamp>.state`** contendo todas as árvores de diretórios já concluídas, os filtros calibrados, as palavras coletadas e a posição exata em cada diretório em andamento!

## Como funciona
Para retomar a varredura exatamente de onde ela parou, basta executar **`feroxbuster --resume-from ferox-https_app_internal_corp-*.state`**!

## Exemplo
```bash
# Executar varredura com orcamento estrito de tempo de 15 minutos (--time-limit 15m) e retomar depois a partir do arquivo .state
feroxbuster -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt \
  --time-limit 15m \
  -o /cases/pentest/ferox_window1.txt
```

## Limites e trade-offs
Se você estiver rodando o Feroxbuster em scripts efêmeros rápidos onde não deseja que arquivos `.state` sejam criados em caso de interrupção, você pode desabilitar esse comportamento definindo `save_state = false` no `ferox-config.toml`.

## Como verificar
Inspecione um arquivo `.state` gerado (que é um documento JSON estruturado!) com `jq . ferox-*.state | head -n 40`.

## Conexões
- [[feroxbuster-coleta-inteligente-palavras-backups-extensoes-links]] — Veja também: Feroxbuster: Geração Dinâmica de Wordlist a partir do Alvo (**`--collect-words` (`-g`)**, **`--collect-backups` (`-B`)**, **`--collect-extensions` (`-E`)** e `--extract-links`).
- [[feroxbuster-encaminhamento-seletivo-replay-proxy-replay-codes-burp-mitmproxy]] — Veja também: Feroxbuster: **`--replay-proxy`** e **`--replay-codes`** — Como Enviar Apenas os Achados Válidos (`200`, `301`, `403`) para o **`mitmproxy` / ZAP / Burp**.
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.
- [[feroxbuster-configuracao-persistente-ferox-config-toml-escopo]] — Referência cruzada direta com feroxbuster-configuracao-persistente-ferox-config-toml-escopo.
- [[masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo]] — Referência cruzada direta com masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
