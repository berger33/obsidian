---
id: software.seguranca.tranche09.000892
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

# Feroxbuster: Adaptação Inteligente de Taxa (**`--auto-tune`**), Aborto Automático de Erros (**`--auto-bail`**) e Limite Explícito (**`--rate-limit`**)

## Em uma frase
Em uma varredura recursiva onde 4 diretórios são descobertos ao mesmo tempo, o volume de requisições pode acionar o *Rate Limiting* (`HTTP 429 Too Many Requests` / `403 Forbidden`) do WAF ou sobrecarregar o servidor web.

## Por que importa
O Feroxbuster resolve esse problema em tempo real com duas políticas autônomas documentadas em `ferox-config.toml.example`: **(1) `--auto-tune`** (monitora a taxa de erros HTTP `429`/`403` e timeouts e **reduz ou aumenta dinamicamente a taxa de requisições em tempo de execução** para manter a velocidade máxima suportada pelo alvo sem ser bloqueado!) e **(2) `--auto-bail`** (aborta automaticamente a varredura de um diretório ou host se detectar uma enxurrada contínua de erros de conexão/5xx/403)!

## Como funciona
Quando o ROE exige um teto rígido e determinístico de requisições por segundo (por exemplo, no máximo 100 requisições/s por scan), passe **`--rate-limit 100`** combinado com **`--scan-limit 2`** (`-L 2`).

## Exemplo
```bash
# Executar o Feroxbuster com ajuste dinamico de velocidade (--auto-tune) ou teto fixo de taxa (--rate-limit)
feroxbuster -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt \
  --auto-tune \
  --scan-limit 2 \
  --timeout 7 \
  -o /cases/pentest/ferox_autotuned.txt
```

## Limites e trade-offs
Mesmo durante uma varredura em andamento no terminal, você não precisa matar o Feroxbuster com `Ctrl+C` se quiser alterar filtros ou pausar um subdiretório ruidoso: pressione **`Enter`** durante a execução para abrir o **Menu Interativo em Tempo Real**, onde você pode cancelar diretórios específicos, adicionar novos filtros de tamanho ou ajustar o limite de taxa ao vivo!

## Como verificar
Monitore na barra de progresso de cada diretório a taxa efetiva `req/sec` ajustada pelo `--auto-tune`.

## Conexões
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Veja também: **Feroxbuster (`epi052/feroxbuster`)**: Arquitetura de **Descoberta Recursiva de Conteúdo Web (*Forced Browsing*)** em Rust (`tokio`).
- [[feroxbuster-filtragem-precisa-status-size-words-lines-regex-similar]] — Veja também: Feroxbuster: Filtros Multi-Dimensionais (`-C`, `-S`, `-W`, `-N`, `-X`) e **Filtro de Similaridade Fuzzy (`--filter-similar-to`)** contra *Soft-404 Dinâmicos*.
- [[gobuster-controle-taxa-delay-timeout-user-agent-evasao-waf-deteccao]] — Referência cruzada direta com gobuster-controle-taxa-delay-timeout-user-agent-evasao-waf-deteccao.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
