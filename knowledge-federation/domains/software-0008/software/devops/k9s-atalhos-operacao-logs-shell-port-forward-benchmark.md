---
id: software.devops.tranche10.000983
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

# K9s: atalhos de operação em recursos (YAML y, Describe d, Edit e, Logs l/p, Shell s, Port-Forward SHIFT-F e Benchmark b)

## Em uma frase
Sobre qualquer recurso selecionado na lista do K9s, teclas de uma única letra acionam operações imediatas: `y` (ver YAML), `d` (describe), `e` (editar), `l` (logs atuais), `p` (logs anteriores de container reiniciado), `s` (abrir shell no container), `Shift-f` (port-forward) e `b` (benchmark HTTP embutido).

## Por que importa
Além de observar recursos, o operador precisa inspecionar por que um container acabou de reiniciar (`p`), abrir um túnel de porta local para testar um endpoint HTTP (`Shift-f`) e até medir a taxa de requisições por segundo e latência daquele endpoint (`b`) sem precisar sair da TUI.

## Como funciona
Conforme lista a tabela `Key Bindings` do README oficial: (1) **Inspeção e Edição**: `y` exibe o manifesto YAML completo (com `f` para tela cheia e `c` para copiar), `d` executa o equivalente ao `kubectl describe`, e `e` abre o recurso no `$KUBE_EDITOR` (desabilitado em `--readonly`); (2) **Logs e Containers**: `l` abre o streaming de logs do pod/deployment (onde `w` alterna quebra de linha *text wrap* e `t` alterna timestamps), `p` exibe os logs da instância anterior (`--previous`), `s` abre um shell interativo dentro do container e `a` faz attach; (3) **Ciclo de vida e Rollout**: `r` faz restart de Deployments/DaemonSets/StatefulSets (ou `drain` na visão de Nodes), `z` lista os ReplicaSets de um Deployment e `ctrl-l` faz rollback; e (4) **Port-Forward e Benchmark**: `Shift-f` cria um port-forward (listado em `f` ou `:pf`), e pressionar **`b`** sobre o port-forward ou Service dispara um gerador de carga HTTP de benchmark (gravando o relatório no diretório `Benchmarks dir` exibido em `k9s info`).

## Exemplo
```text
# Sequência de teclas no K9s para criar um Port-Forward em um Pod, listar os túneis ativos e rodar um Benchmark HTTP
1. Selecione o Pod e pressione: Shift-f (confirme a porta local:container)
2. Navegue para a visão de Port-Forwards digitando: :pf
3. Selecione o túnel ativo e pressione: b (para iniciar/parar o benchmark HTTP)
```

## Limites e trade-offs
Atenção redobrada à diferença entre **`ctrl-d`** e **`ctrl-k`** ao remover recursos no K9s: enquanto **`ctrl-d`** abre uma caixa de diálogo pedindo confirmação explícita (`TAB` e `ENTER`, permitindo escolher propagation policy), pressionar **`ctrl-k`** (*Kill*) executa o equivalente imediato a `kubectl delete --now` **sem nenhuma caixa de diálogo de confirmação**!

## Como verificar
Em um cluster de desenvolvimento, selecione um Pod no K9s, pressione `y` para ver o YAML, `Esc` para voltar, `l` para ver os logs e `w` para alternar o word-wrap dos logs.

## Conexões
- [[k9s-navegacao-modo-comando-filtros-regex-labels-contextos]] — Veja também: K9s: modo de comando (:pod, :ctx, :ns) e filtragem avançada por Regex (/), inversa (/!), Labels (/-l) e Fuzzy (/-f).
- [[k9s-visoes-diagnostico-pulses-xray-popeye-usedby]] — Veja também: K9s: visões integradas de diagnóstico de saúde e topologia (:pulses, :xray, :popeye, UsedBy u e Jump to Owner SHIFT-J).
- [[k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes]] — Referência cruzada direta com k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
