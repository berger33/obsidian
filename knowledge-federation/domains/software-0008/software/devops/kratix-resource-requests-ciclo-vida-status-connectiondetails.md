---
id: software.devops.tranche12.001103
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://docs.kratix.io/main/quick-start", "https://raw.githubusercontent.com/syntasso/kratix/main/README.md", "https://github.com/syntasso/kratix"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kratix: Ciclo de Vida de Resource Requests e Retorno de Status ao Consumidor

## Em uma frase
Resource Requests no Kratix representam instâncias concretas solicitadas pelos consumidores contra a CRD de uma Promise, cujo ciclo de vida inclui execução de workflows `configure` e retorno estruturado de `status.message` e `status.connectionDetails`.

## Por que importa
Quando um desenvolvedor solicita um banco de dados ou fila por autoatendimento, ele precisa saber exatamente quando o recurso terminou de ser provisionado e onde estão o host e o Secret de credenciais, sem precisar vasculhar logs de operadores de infraestrutura.

## Como funciona
Ao submeter o manifesto da Resource Request (por exemplo, `kind: postgresql`), o Kratix dispara um Job de pipeline com o rótulo `kratix.io/promise-name`. Ao concluir o pipeline, o Kratix atualiza `status.conditions` (`ConfigureWorkflowCompleted=True`) e mescla no `status` da requisição qualquer arquivo `status.yaml` gravado pelo workflow em `/kratix/metadata/status.yaml`, expondo endpoints e referências de Secrets ao usuário.

## Exemplo
```yaml
apiVersion: marketplace.kratix.io/v1alpha2
kind: postgresql
metadata:
  name: order-db
  namespace: default
spec:
  teamId: "checkout-squad"
  backupEnabled: true
---
# Verificacao via CLI:
# kubectl get postgresqls.marketplace.kratix.io order-db -o yaml
```

## Limites e trade-offs
Gravar senhas em texto claro dentro de `status.connectionDetails` da Resource Request em vez de gravar apenas o nome do `Secret` Kubernetes expõe credenciais a qualquer usuário com permissão de leitura (`get`/`list`) na CRD.

## Como verificar
Inspecione `status.conditions`, `status.observedGeneration` e `status.connectionDetails` na Resource Request para validar que o workflow preencheu os metadados esperados sem vazar segredos.

## Conexões
- [[kratix-promise-crd-api-contrato-produtor-consumidor]] — Veja também: Kratix: Definição de Promise e Contrato de API entre Produtor e Consumidor.
- [[kratix-workflows-pipelines-containers-input-output-metadata]] — Veja também: Kratix: Workflows Imperativos-Declarativos com Containers (/kratix/input, /kratix/output e /kratix/metadata).

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
