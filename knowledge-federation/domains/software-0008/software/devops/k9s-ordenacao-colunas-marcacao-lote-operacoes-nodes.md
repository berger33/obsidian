---
id: software.devops.tranche10.000987
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
fontes: ["https://raw.githubusercontent.com/derailed/k9s/master/README.md", "https://k9scli.io/topics/commands/", "https://github.com/derailed/k9s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K9s: ordenação de colunas (SHIFT-N/A/S/O), seleção múltipla em lote (SPACE / CTRL-SPACE) e operações de Node (cordon/drain)

## Em uma frase
Nas tabelas de recursos do K9s, o operador pode ordenar linhas instantaneamente por coluna (`Shift-n` nome, `Shift-a` idade, `Shift-s` status, `Shift-o` coluna selecionada), marcar múltiplos recursos (`Space` e `Ctrl-Space`) para operações em lote e gerenciar nós (`u` cordon/uncordon e `r` drain).

## Por que importa
Durante uma manutenção de cluster ou limpeza de pods com falha, precisar deletar 15 pods em estado `Evicted` um por um ou lembrar a sintaxe de flags do `kubectl drain` / `kubectl sort-by` atrasa a operação; a marcação em lote e a ordenação por teclado do K9s executam isso em segundos.

## Como funciona
Conforme lista a tabela completa de `Key Bindings` no README oficial: (1) **Ordenação e Colunas**: `Shift-n` ordena por `Name`, `Shift-a` ordena por `Age` (idade do recurso, ideal para ver os pods recém-criados no topo), `Shift-s` ordena por `Status`, `Shift-p` ordena por `Namespace`, e usar `Shift-Left` / `Shift-Right` move o cursor de coluna permitindo ordenar por qualquer coluna selecionada com **`Shift-o`** (além de `Ctrl-w` para alternar colunas *wide*); (2) **Marcação em lote (*Marks*)**: **`Space`** marca/desmarca a linha atual, **`Ctrl-Space`** marca um intervalo inteiro de linhas e **`Ctrl-\`** limpa todas as marcas, permitindo aplicar `Ctrl-d` (delete) ou `Ctrl-s` (save) em todos os itens marcados de uma só vez; e (3) **Node View (`:node`)**: selecionar um nó e pressionar **`u`** alterna *Cordon/Uncordon*, enquanto **`r`** executa *Drain node*.

## Exemplo
```text
# Atalhos na visão :pod para ordenar pelos pods mais recentes, selecionar um intervalo de pods e deletá-los em lote
1. Pressione Shift-a (ordena os pods por Age)
2. Selecione o primeiro pod alvo e pressione Space
3. Mova até o último pod do bloco e pressione Ctrl-Space (marca o intervalo)
4. Pressione Ctrl-d para deletar todos os pods marcados (ou Ctrl-\ para limpar a seleção)
```

## Limites e trade-offs
Na visão de **Nodes (`:node`)**, a tecla **`r`** executa **`Drain node`** (evacuando os pods do nó), enquanto na visão de **Deployments / DaemonSets / StatefulSets** a mesma tecla **`r`** executa **`Restart resource`** (`rollout restart`); verifique sempre no cabeçalho superior da tela em qual visão você está antes de pressionar `r` ou `u`.

## Como verificar
Na visão `:pod` do K9s, pressione `Ctrl-w` para expandir as colunas detalhadas (`wide`, mostrando IP e Node), use `Shift-Right` para navegar até a coluna `RESTARTS` e pressione `Shift-o` para ordenar os pods pelo número de reinicializações.

## Conexões
- [[k9s-extensibilidade-plugins-hotkeys-aliases-views-skins]] — Veja também: K9s: extensibilidade com plugins customizados (plugins.yaml), atalhos (hotkeys.yaml), colunas (views.yaml) e temas (skins).
- [[k9s-execucao-container-docker-build-multiplataforma-compatibilidade]] — Veja também: K9s: execução via container Docker (derailed/k9s), compilação com KUBECTL_VERSION e matriz de compatibilidade Kubernetes.
- [[k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes]] — Referência cruzada direta com k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes.
- [[k9s-navegacao-modo-comando-filtros-regex-labels-contextos]] — Referência cruzada direta com k9s-navegacao-modo-comando-filtros-regex-labels-contextos.
- [[k9s-atalhos-operacao-logs-shell-port-forward-benchmark]] — Referência cruzada direta com k9s-atalhos-operacao-logs-shell-port-forward-benchmark.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
