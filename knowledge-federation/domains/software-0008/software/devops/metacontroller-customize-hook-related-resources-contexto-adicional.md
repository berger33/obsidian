---
id: software.devops.tranche18.001776
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://metacontroller.github.io/metacontroller/concepts.html", "https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md", "https://github.com/metacontroller/metacontroller"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Metacontroller `customize` hook: busca declarativa de `relatedResources` para enriquecer o contexto do `sync`

## Em uma frase
O hook **`customize`** (`spec.hooks.customize`) permite que o controlador informe dinamicamente ao Metacontroller quais recursos adicionais do cluster (*related resources* que não são nem o pai nem os filhos criados) devem ser buscados no cache e incluídos sob a chave `related` na chamada do webhook `sync`.

## Por que importa
Imagine que um `CompositeController` para um `WebApp` precise ler um `ConfigMap` global ou um `Secret` referenciado pelo nome em `spec.secretName` do `WebApp`: como o `Secret` não é filho do `WebApp`, ele não viria no dicionário `children`.

## Como funciona
Com o hook `customize`, o Metacontroller primeiro envia o objeto `parent` para o endpoint `/customize`; o hook retorna uma lista de regras `relatedResources` (especificando `apiVersion`, `resource`, `namespace` e `names` ou `labelSelector`). O Metacontroller busca esses objetos no seu cache de Informers (sem bater no `kube-apiserver`) e os entrega na chave `related` da requisição `/sync`.

## Exemplo
```json
{
  "relatedResources": [
    {
      "apiVersion": "v1",
      "resource": "secrets",
      "namespace": "default",
      "names": ["app-tls-secret"]
    }
  ]
}
```

## Limites e trade-offs
Qualquer alteração em um objeto listado em `relatedResources` re-enfileira automaticamente a reconciliação `sync` do objeto pai dependente, mantendo reatividade total sem código de watch manual.

## Como verificar
Configure um hook `customize` retornando um `ConfigMap` relacionado, edite o `ConfigMap` com `kubectl edit` e verifique que o hook `sync` do pai é disparado imediatamente.

## Conexões
- [[metacontroller-finalize-hook-limpeza-ordenada-finalizers]] — Veja também: Metacontroller `finalize` hook: gerenciamento declarativo de Finalizers e limpeza antes da exclusão.
- [[metacontroller-estrategias-atualizacao-filhos-ondelete-recreate-inplace-rolling]] — Veja também: Metacontroller: estratégias de atualização de recursos filhos (`OnDelete`, `Recreate`, `InPlace`, `RollingRecreate`, `RollingInPlace`).

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://metacontroller.github.io/metacontroller/concepts.html) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
