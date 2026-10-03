---
id: software.devops.tranche16.001511
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md", "https://carvel.dev/kapp/docs/v0.63.x/diff/", "https://github.com/carvel-dev/kapp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kapp: gerenciamento declarativo de aplicações Kubernetes por agrupamento de labels client-side

## Em uma frase
O Carvel `kapp` (CNCF Carvel, escrito em Go) é uma CLI de implantação para Kubernetes que agrupa conjuntos de recursos sob um rótulo de aplicação gerenciado client-side, separando rigorosamente o cálculo de diferenças (`diff stage`) da aplicação e espera de convergência (`apply stage`).

## Por que importa
O `kubectl apply -f dir/` nativo aplica manifestos individualmente sem noção nativa de conjunto de aplicação (a menos que se use `--prune` com seletores manuais arriscados) e retorna assim que a API aceita o YAML, sem aguardar que os Pods, Services e CRDs realmente convirjam para o estado saudável.

## Como funciona
Ao executar `kapp deploy -a minha-app -f manifestos.yml`, o `kapp` injeta automaticamente um label identificador único em todos os objetos do lote, cria um `ConfigMap` de metadados de histórico de mudanças no cluster (sem exigir componentes server-side nem CRDs próprios) e calcula exatamente quais recursos devem ser criados, atualizados ou removidos em relação ao último deploy.

## Exemplo
```bash
kapp deploy -a payments-api -f rendered-manifests.yml --yes
kapp list -n default
kapp inspect -a payments-api --tree
```

## Limites e trade-offs
Diferentemente do Helm, o `kapp` exclui deliberadamente templating e empacotamento de seu escopo, esperando receber manifestos Kubernetes YAML já renderizados (por exemplo via `ytt`, `helm template` ou `kustomize build`).

## Como verificar
Execute `kapp inspect -a payments-api --tree` após o deploy para visualizar a árvore hierárquica (`Deployment -> ReplicaSet -> Pod`) e o estado de reconciliação de cada objeto.

## Conexões
- [[carvel-kapp-diff-stage-estrategias-last-applied-vs-live]] — Veja também: Carvel kapp: estágio de diff e estratégias de comparação contra `last-applied` versus recurso ativo.

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
