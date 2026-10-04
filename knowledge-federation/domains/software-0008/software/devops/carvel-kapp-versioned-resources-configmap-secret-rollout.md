---
id: software.devops.tranche16.001513
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
fontes: ["https://carvel.dev/kapp/docs/v0.63.x/diff/", "https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md", "https://github.com/carvel-dev/kapp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kapp: recursos versionados (`kapp.k14s.io/versioned`) para rollout automático de ConfigMaps e Secrets

## Em uma frase
A anotação `kapp.k14s.io/versioned: ""` instrui o `kapp` a criar recursos imutáveis sufixados com `-ver-{n}` a cada alteração de conteúdo de um `ConfigMap` ou `Secret`, atualizando automaticamente todas as referências em `Deployment`, `StatefulSet`, `DaemonSet` e `Job`.

## Por que importa
No Kubernetes nativo, alterar os dados de um `ConfigMap` ou `Secret` não reinicia os Pods de um `Deployment` que o consomem via variáveis de ambiente (`envFrom` / `configMapKeyRef`), fazendo com que os containers continuem rodando com configurações obsoletas.

## Como funciona
Quando um `ConfigMap` ou `Secret` possui `kapp.k14s.io/versioned: ""`, qualquer mudança em seu conteúdo faz o `kapp` criar um novo objeto (por exemplo `special-config-ver-2` após `special-config-ver-1`) e reescrever os campos `configMapRef`, `secretRef` e `volumes` nos workloads dependentes através de `templateRules` embutidas. Opcionalmente, `kapp.k14s.io/num-versions: "5"` controla quantas versões históricas são retidas antes da coleta de lixo.

## Exemplo
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-settings
  annotations:
    kapp.k14s.io/versioned: ""
    kapp.k14s.io/num-versions: "3"
data:
  LOG_LEVEL: "info"
```

## Limites e trade-offs
Se outro recurso externo que não faz parte do mesmo deploy do `kapp` precisar referenciar o nome original sem o sufixo `-ver-{n}`, é necessário adicionar também a anotação `kapp.k14s.io/versioned-keep-original: ""` para manter uma cópia com o nome fixo.

## Como verificar
Modifique um valor no `ConfigMap` anotado, execute `kapp deploy -a payments-api -f manifestos.yml --diff-changes --diff-run` e confirme a criação de `app-settings-ver-2` e o update automático no `Deployment`.

## Conexões
- [[carvel-kapp-diff-stage-estrategias-last-applied-vs-live]] — Veja também: Carvel kapp: estágio de diff e estratégias de comparação contra `last-applied` versus recurso ativo.
- [[carvel-kapp-ordenacao-mudancas-change-group-change-rule]] — Veja também: Carvel kapp: ordenação determinística de mudanças com `change-group` e `change-rule`.

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
