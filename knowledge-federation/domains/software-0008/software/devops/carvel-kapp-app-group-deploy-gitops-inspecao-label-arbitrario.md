---
id: software.devops.tranche16.001520
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

# Carvel kapp: implantação em lote via `app-group` e inspeção de recursos existentes por seletor `label:`

## Em uma frase
O subcomando `kapp app-group deploy` reconcilia múltiplos diretórios de aplicações de forma coordenada para fluxos GitOps, enquanto a sintaxe `-a label:chave=valor` permite usar o `kapp` para inspecionar, monitorar logs e deletar recursos que nem sequer foram criados pelo `kapp`.

## Por que importa
Repositórios GitOps de cluster frequentemente organizam dezenas de aplicações em subdiretórios independentes (`apps/logging`, `apps/monitoring`, `apps/ingress`), e operadores de plantão também precisam inspecionar árvores de recursos e logs de aplicações legadas implantadas via Helm ou `kubectl`.

## Como funciona
Com `kapp app-group deploy -g cluster-core --directory ./apps`, cada subdiretório torna-se uma aplicação `kapp` nomeada `<grupo>-<subdiretorio>`. Já ao executar `kapp inspect -a label:app.kubernetes.io/instance=prometheus --tree`, o `kapp` consulta qualquer conjunto de objetos que compartilhem aquele label padrão do Kubernetes, montando a árvore de status e permitindo rodar `kapp logs -a label:... -f`.

## Exemplo
```bash
kapp app-group deploy -g platform-addons --directory ./cluster-apps --yes
kapp inspect -a label:app.kubernetes.io/name=coredns -n kube-system --tree
```

## Limites e trade-offs
Executar `kapp delete -a label:chave=valor` apagará todos os recursos do cluster (ou namespace) que possuam aquele label, mesmo que tenham sido criados manualmente ou por outra ferramenta; revise sempre a tabela de diff antes de confirmar.

## Como verificar
Execute `kapp inspect -a label:k8s-app=kube-dns -n kube-system --tree` em qualquer cluster Kubernetes para verificar a árvore de `Deployment`, `ReplicaSet`, `Pod` e `Endpoints` sem instalar nada no cluster.

## Conexões
- [[carvel-kapp-operacao-sem-privilegios-admin-single-namespace-rbac]] — Veja também: Carvel kapp: operação sem privilégios de cluster-admin e escopo de namespace único (`-n`).

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
