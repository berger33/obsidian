---
id: software.devops.tranche10.000998
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

# Stern: acompanhamento automático de initContainers, ephemeralContainers (kubectl debug) e rollouts dinâmicos

## Em uma frase
Por padrão (`--init-containers=true` e `--ephemeral-containers=true`), o Stern acompanha automaticamente os logs de containers de inicialização, containers principais e containers efêmeros de debug na medida em que são criados ou substituídos durante rollouts do Kubernetes.

## Por que importa
Quando um pod fica travado em `Init:0/2` ou `Init:CrashLoopBackOff`, o comando `kubectl logs <pod>` padrão falha ou tenta ler o container principal que ainda nem iniciou, exigindo que o operador descubra o nome do `initContainer` e rode `kubectl logs <pod> -c <init-container>`. No Stern, todos os `initContainers` e containers de aplicação já aparecem automaticamente no mesmo fluxo cronológico colorido.

## Como funciona
Quando o Stern detecta um pod que corresponde à consulta: (1) ele inspeciona `spec.initContainers`, `spec.containers` e `spec.ephemeralContainers` (criados via `kubectl debug`); (2) abre um stream de log separado para cada container (diferenciável visualmente ativando `--diff-container` / `-d`); (3) durante um `kubectl rollout restart` de um Deployment, à medida que os pods da revisão antiga recebem `SIGTERM` e emitem seus logs de desligamento gracioso (*graceful shutdown*), os novos pods da revisão nova entram em `Init` -> `Running` e têm seus logs intercalados na mesma janela do terminal sem perder nenhuma linha da transição; e (4) caso você queira ocultar os logs de inicialização, basta passar `--init-containers=false`.

## Exemplo
```bash
# Observar em uma única janela um rollout completo diferenciando cores por container (-d), incluindo initContainers
stern deployment/payment-service -d --tail 0
```

## Limites e trade-offs
Usar `stern deployment/<nome> -d --tail 0` (onde `--tail 0` ignora todas as linhas passadas e mostra apenas linhas geradas a partir do momento em que o comando foi iniciado) em um terminal ao lado de `kubectl rollout restart deployment/<nome>` é a forma mais limpa de validar que os pods antigos encerram conexões sem erros HTTP 500 e que os pods novos passam pelos `initContainers` sem falhas.

## Como verificar
Inicie `stern deployment/<nome> -d --tail 0`, anexe um container efêmero de teste com `kubectl debug` (ou reinicie o deployment) e confirme que o Stern passa a imprimir os logs do novo container automaticamente sem reiniciar o comando.

## Conexões
- [[stern-configuracao-persistente-config-yaml-cores-prompt]] — Veja também: Stern: arquivo de configuração persistente (~/.config/stern/config.yaml), customização de cores SGR e modo --prompt.
- [[stern-pipeline-jq-only-log-lines-raw-color-control]] — Veja também: Stern: integração em pipelines Unix com jq (--only-log-lines / -o raw, --color) e funções de tempo (toUTC, toTimestamp).
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.
- [[stern-selecao-alvos-regex-recursos-labels-containers-estados]] — Referência cruzada direta com stern-selecao-alvos-regex-recursos-labels-containers-estados.
- [[ko-cicd-github-actions-assinatura-cosign-slsa-seguranca]] — Referência cruzada direta com ko-cicd-github-actions-assinatura-cosign-slsa-seguranca.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
