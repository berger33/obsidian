---
id: software.devops.tranche16.001514
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

# Carvel kapp: ordenação determinística de mudanças com `change-group` e `change-rule`

## Em uma frase
O `kapp` ordena automaticamente a criação de `Namespace` e `CustomResourceDefinition` antes dos demais recursos e permite definir dependências arbitrárias de deploy e deleção por meio das anotações `kapp.k14s.io/change-group` e `kapp.k14s.io/change-rule`.

## Por que importa
Em muitas aplicações, um `Job` de migração de esquema de banco de dados precisa concluir com sucesso (`Succeeded`) antes que o novo `Deployment` da API seja atualizado, ou um operador CRD precisa estar rodando e com webhook ativo antes de aplicar os Custom Resources correspondentes.

## Como funciona
O autor atribui um grupo ao recurso produtor (por exemplo `kapp.k14s.io/change-group: "db-migrations"`) e adiciona ao `Deployment` consumidor a regra `kapp.k14s.io/change-rule: "upsert after upserting db-migrations"`. Durante o `apply stage`, o `kapp` constrói um grafo acíclico direcionado (DAG), aplica primeiro o grupo `db-migrations`, aguarda sua reconciliação completa e só então inicia o rollout do `Deployment`.

## Exemplo
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: schema-migrate
  annotations:
    kapp.k14s.io/change-group: "db-migration"
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: migrate
          image: ghcr.io/org/migrate:v2.0
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
  annotations:
    kapp.k14s.io/change-rule.0: "upsert after upserting db-migration"
    kapp.k14s.io/change-rule.1: "delete before deleting db-migration"
```

## Limites e trade-offs
Criar dependências circulares entre anotações `change-group` e `change-rule` fará o `kapp` abortar o deploy antes de tocar no cluster, reportando o ciclo detectado no grafo de mudanças.

## Como verificar
Execute `kapp deploy -a api -f manifestos.yml --diff-run` e verifique a ordem planejada de execução e espera dos recursos.

## Conexões
- [[carvel-kapp-versioned-resources-configmap-secret-rollout]] — Veja também: Carvel kapp: recursos versionados (`kapp.k14s.io/versioned`) para rollout automático de ConfigMaps e Secrets.
- [[carvel-kapp-apply-waiting-reconciliacao-wait-rules-streaming-logs]] — Veja também: Carvel kapp: espera ativa de convergência (`apply waiting`), `waitRules` e streaming de logs (`--logs`).

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
