---
id: software.devops.tranche10.000999
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

# Stern: integração em pipelines Unix com jq (--only-log-lines / -o raw, --color) e funções de tempo (toUTC, toTimestamp)

## Em uma frase
Para integrar o Stern com processadores de linha de comando como `jq`, `awk` ou `grep`, as opções **`--only-log-lines`** (ou **`-o raw`**) e **`--color=never|auto|always`** controlam os prefixos e códigos de escape ANSI, enquanto as funções de template `toUTC`, `toRFC3339Nano` e `toTimestamp` normalizam datas internas do JSON.

## Por que importa
Se você tentar fazer `stern meu-app | jq .`, o `jq` falhará imediatamente com erro de parsing porque a saída padrão do Stern precede cada linha JSON com o nome colorido do pod e do container (`meu-app-7b9f-xk2 api {"level":"info",...}`). Saber emitir apenas a linha bruta (`-o raw` / `--only-log-lines`) ou enriquecer o JSON com o nome do pod (`-o json`) permite compor pipelines Unix perfeitos.

## Como funciona
Conforme a documentação oficial do Stern: (1) **`-o raw`** ou **`--only-log-lines`**: suprime o prefixo de namespace/pod/container e imprime exclusivamente a mensagem de log original, permitindo canalizar logs JSON de 10 pods diferentes diretamente para `| jq .`; (2) **`-o json`**: envolve a linha de log em um envelope JSON do Stern (`{"nodeName":...,"namespace":...,"podName":...,"containerName":...,"message":...}`), ideal quando você quer filtrar no `jq` tanto pelo nome do pod quanto pelo conteúdo da mensagem (`jq 'select(.podName | contains("canary")) | .message | fromjson'`); e (3) **`--color`**: por padrão é `auto` (desativa cores automaticamente quando a saída é redirecionada para um pipe `|` ou arquivo `>`), podendo ser forçado para `always` (ex.: `stern app --color=always | less -R`) ou `never`.

## Exemplo
```bash
# Canalizar logs JSON de múltiplos pods diretamente para o jq usando -o raw ou paginar com cores no less -R
stern deployment/api -o raw --tail 50 | jq 'select(.status >= 500)'
stern deployment/api --color=always --no-follow --tail 200 | less -R
```

## Limites e trade-offs
Quando você usa `-o raw` (ou `--only-log-lines`) agregando logs de 10 pods diferentes no `jq`, se o JSON original emitido pela aplicação não contiver um campo identificando o `hostname` ou `pod_name`, você não saberá de qual pod veio aquela linha filtrada pelo `jq`; nesse caso, prefira usar `-o json` ou um `--template` customizado que injete `.PodName` no JSON.

## Como verificar
Execute `stern . -n kube-system --tail 5 --no-follow --only-log-lines` e confirme que os prefixos de pod e container foram removidos da saída.

## Conexões
- [[stern-containers-efemeros-init-containers-ciclo-vida-pods]] — Veja também: Stern: acompanhamento automático de initContainers, ephemeralContainers (kubectl debug) e rollouts dinâmicos.
- [[stern-instalacao-krew-homebrew-autocompletar-shells-kubeconfig]] — Veja também: Stern: instalação via Krew/Homebrew/asdf/WinGet, precedência de KUBECONFIG e autocompletar de shell (--completion).
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.
- [[stern-formatos-saida-output-templates-go-funcoes-json]] — Referência cruzada direta com stern-formatos-saida-output-templates-go-funcoes-json.
- [[stern-processamento-logs-locais-stdin-no-follow-condition]] — Referência cruzada direta com stern-processamento-logs-locais-stdin-no-follow-condition.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
