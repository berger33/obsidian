---
id: software.devops.tranche10.000993
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/stern/stern/master/README.md", "https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md", "https://github.com/stern/stern"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Stern: filtragem e destaque de conteúdo de logs por Regex (--include, --exclude, --highlight) e formatação de timestamps (-t)

## Em uma frase
Em vez de encadear múltiplos comandos `grep -v` e `grep -E` no shell (que frequentemente sofrem com buffering de pipe), o Stern filtra e destaca o conteúdo das linhas de log nativamente via expressões regulares com **`--include` (`-i`)**, **`--exclude` (`-e`)** e **`--highlight` (`-H`)**, além de formatar datas e fusos com **`--timestamps` (`-t`)** e **`--timezone`**.

## Por que importa
Aplicações web costumam registrar uma linha `GET /healthz 200 OK` a cada 2 segundos por pod devido às probes do `kubelet`, poluindo o terminal. Se você tentar filtrar com `stern app | grep -v healthz | grep ERROR`, perde a capacidade de ver o contexto ao redor de uma linha destacada ou precisa lidar com o buffer do pipe Unix.

## Como funciona
Para cada linha de log recebida dos containers: (1) **`--exclude` (`-e`)**: descarta qualquer linha que case com a expressão regular informada (pode ser repetida para múltiplos padrões, ex.: `-e "/healthz" -e "/metrics"`); (2) **`--include` (`-i`)**: exibe apenas linhas que casem com a expressão regular informada; (3) **`--highlight` (`-H`)**: mantém todas as linhas fluindo na tela, mas colore em destaque qualquer trecho que case com a regex (ex.: `-H "ERROR|WARN|timeout"`); e (4) **`--timestamps` (`-t` / `--timestamps=short|default`) e `--timezone`**: adiciona o timestamp de cada linha convertido para o fuso horário local (`Local`, o padrão) ou para uma timezone específica (ex.: `--timezone UTC` ou `America/Sao_Paulo`).

## Exemplo
```bash
# Excluir logs de healthcheck (-e), destacar erros/timeouts (-H) e exibir timestamps curtos (-t) no fuso UTC
stern deployment/orders-api -e "/healthz|/readyz" -H "ERROR|DEADLINE_EXCEEDED" --timestamps=short --timezone=UTC
```

## Limites e trade-offs
Conforme detalha a tabela de flags do README oficial do Stern, ao especificar um formato para a flag `--timestamps` (como `default` ou `short`), **o sinal de igual `=` não pode ser omitido** (`--timestamps=short` ou apenas `-t` / `--timestamps` sem valor para usar o formato `default`); se você escrever `--timestamps short` com espaço em branco, a palavra `short` será interpretada pelo parser como um argumento posicional de `pod-query`!

## Como verificar
Execute `stern . -n kube-system --tail 10 --timestamps=short -H "kube"` e verifique a exibição do timestamp curto no início de cada linha e o destaque colorido do termo pesquisado.

## Conexões
- [[stern-selecao-alvos-regex-recursos-labels-containers-estados]] — Veja também: Stern: seleção granular de pods e containers (--selector, --field-selector, --node, --container e --container-state).
- [[stern-formatos-saida-output-templates-go-funcoes-json]] — Veja também: Stern: modos de saída (--output default, raw, json, extjson, ppextjson) e templates Go customizados (--template).
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
