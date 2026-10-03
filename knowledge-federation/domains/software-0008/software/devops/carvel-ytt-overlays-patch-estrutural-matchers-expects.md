---
id: software.devops.tranche16.001503
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
fontes: ["https://carvel.dev/ytt/docs/v0.52.x/", "https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md", "https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel ytt: aplicação de patches estruturais declarativos com o módulo `@ytt:overlay`

## Em uma frase
O módulo `@ytt:overlay` do `ytt` permite modificar documentos YAML existentes (como manifestos upstream de terceiros ou saídas de Helm) por meio de regras declarativas de correspondência (`matcher`) e verificação explícita de cardinalidade (`expects`).

## Por que importa
Diferentemente do `StrategicMergePatch` do Kustomize — que depende de metadados específicos da API do Kubernetes — ou de `JSONPatch` posicional frágil por índice numérico (`containers/0`), os overlays do `ytt` funcionam em qualquer documento YAML (Kubernetes, Concourse, Docker Compose, GitHub Actions) e localizam elementos de lista por predicados semânticos.

## Como funciona
Um documento anotado com `#@overlay/match by=overlay.subset({"kind": "Deployment"})` localiza os documentos alvo. Dentro dele, anotações como `#@overlay/match missing_ok=True`, `#@overlay/replace`, `#@overlay/remove` e `#@overlay/merge` especificam a operação exata sobre cada chave ou item de array, falhando por padrão se o seletor não encontrar exatamente 1 alvo (`expects=1`).

## Exemplo
```yaml
#@ load("@ytt:overlay", "overlay")

#@overlay/match by=overlay.subset({"kind": "Deployment", "metadata": {"name": "coredns"}})
---
spec:
  template:
    spec:
      containers:
        #@overlay/match by="name"
        - name: coredns
          #@overlay/match missing_ok=True
          resources:
            limits:
              memory: 256Mi
```

## Limites e trade-offs
Como o `@ytt:overlay` exige por padrão que cada seletor case com exatamente um nó (`expects=1`), aplicar um overlay genérico a múltiplos Deployments sem declarar `expects="1+"` ou `expects=0` interromperá a execução com erro de cardinalidade.

## Como verificar
Execute `ytt -f base-deployment.yml -f patch-overlay.yml` e verifique que o container `coredns` recebeu o bloco `resources.limits.memory` mantendo os demais campos intocados.

## Conexões
- [[carvel-ytt-data-values-schema-validacao-tipagem-defaults]] — Veja também: Carvel ytt: declaração de `#@data/values-schema` para tipagem forte e valores padrão.
- [[carvel-ytt-validacoes-customizadas-schema-validation-assert]] — Veja também: Carvel ytt: validações customizadas com `#@schema/validation` e módulo `@ytt:assert`.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://carvel.dev/ytt/docs/v0.52.x/) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
