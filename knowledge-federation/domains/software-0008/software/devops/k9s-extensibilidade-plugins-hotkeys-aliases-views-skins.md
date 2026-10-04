---
id: software.devops.tranche10.000986
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

# K9s: extensibilidade com plugins customizados (plugins.yaml), atalhos (hotkeys.yaml), colunas (views.yaml) e temas (skins)

## Em uma frase
O K9s pode ser estendido sem recompilar o código por meio dos arquivos YAML listados em `k9s info`: **`plugins.yaml`** (para acionar ferramentas externas como `stern`, `kubectl debug`, `dive` ou `helm` com variáveis de contexto), **`views.yaml`** (colunas customizadas), **`hotkeys.yaml`**, **`aliases.yaml`** e **`skins`**.

## Por que importa
Cada equipe de engenharia de plataforma possui suas próprias ferramentas e fluxos operacionais — como abrir os logs de um Deployment no `stern`, iniciar um container efêmero `kubectl debug`, disparar uma sincronização do Argo CD ou exibir uma coluna customizada mostrando uma label específica do pod.

## Como funciona
Nos arquivos localizados nos diretórios exibidos por `k9s info`: (1) **`plugins.yaml`**: permite definir novos atalhos de teclado vinculados a `scopes` específicos (ex.: `pods`, `deployments`, `containers`) que executam qualquer comando binário externo (`command` e `args`), injetando variáveis de ambiente automáticas do item atualmente selecionado na tela do K9s (`$NAME`, `$NAMESPACE`, `$CONTEXT`, `$CONTAINER`, `$POD`, `$COL-<NOME>`); (2) **`views.yaml`**: customiza quais colunas (incluindo expressões JSONPath) são exibidas em cada tipo de recurso; (3) **`hotkeys.yaml`** e **`aliases.yaml`**: criam teclas de salto rápido (ex.: `Shift-0` para ir direto a `:pods`) e apelidos curtos para CRDs longos; e (4) **`skins`**: personaliza a paleta de cores da interface (podendo associar uma cor de topo diferente para cada cluster de produção vs desenvolvimento!).

## Exemplo
```yaml
# Exemplo de plugin em ~/.local/share/k9s/plugins.yaml para abrir os logs do pod selecionado usando o stern (Shift-T)
plugins:
  stern-logs:
    shortCut: Shift-T
    confirm: false
    description: "Tail logs with Stern"
    scopes:
      - pods
    command: stern
    background: false
    args:
      - --tail=100
      - $NAME
      - -n
      - $NAMESPACE
      - --context
      - $CONTEXT
```

## Limites e trade-offs
Configurar um tema visual (**skin**) específico por contexto de cluster (por exemplo, fundo de cabeçalho vermelho para clusters de produção e verde/azul para clusters de desenvolvimento/kind) é uma das melhores práticas operacionais no K9s para evitar que o engenheiro execute comandos destrutivos achando que está conectado ao cluster de testes.

## Como verificar
Execute `k9s info` para localizar o caminho exato de `Plugins file` e `Custom views file` no seu sistema e adicione um atalho em `hotkeys.yaml` ou `plugins.yaml` verificando sua exibição no menu `?`.

## Conexões
- [[k9s-configuracao-xdg-diretorios-logs-debug-screendumps]] — Veja também: K9s: estrutura de diretórios XDG (config.yaml, clusters, screendumps), logs de debug (-l debug) e variável K9S_CONFIG_DIR.
- [[k9s-ordenacao-colunas-marcacao-lote-operacoes-nodes]] — Veja também: K9s: ordenação de colunas (SHIFT-N/A/S/O), seleção múltipla em lote (SPACE / CTRL-SPACE) e operações de Node (cordon/drain).
- [[k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes]] — Referência cruzada direta com k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes.
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
