---
id: software.devops.tranche12.001117
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
fontes: ["https://raw.githubusercontent.com/score-spec/score-compose/main/README.md", "https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md", "https://raw.githubusercontent.com/score-spec/spec/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Score: Recursos Compartilhados entre Múltiplos Workloads (id e service-port)

## Em uma frase
A especificação Score permite que múltiplos workloads compartilhem a mesma instância de um recurso (como um banco de dados ou tópico Kafka) definindo um identificador comum `id` no bloco `resources`, ou descubram portas de outros workloads via recurso `type: service-port`.

## Por que importa
Em arquiteturas com uma API web e um worker assíncrono em serviços separados, ambos precisam acessar a mesma fila AMQP ou o mesmo banco de dados sem que os provisionadores criem duas instâncias isoladas.

## Como funciona
Ao atribuir o mesmo campo `id` (por exemplo, `id: shared-orders-db`) em dois arquivos `score.yaml` processados no mesmo projeto `score-compose` ou `score-k8s`, o motor de estado resolve o recurso uma única vez e injeta os mesmos dados de conexão em ambos os workloads. Para chamadas diretas entre serviços, o recurso `type: service-port` recebe `params: { workload: target-svc, port: http }` e expõe `hostname` e `port`.

## Exemplo
```yaml
resources:
  orders-queue:
    type: amqp
    id: shared-orders-rabbitmq
  catalog-endpoint:
    type: service-port
    params:
      workload: catalog-api
      port: http
```

## Limites e trade-offs
Omitir o campo `id` esperando que dois recursos com o mesmo nome de chave (`db`) em arquivos `score.yaml` distintos sejam compartilhados faz o Score provisionar instâncias separadas por escopo de workload.

## Como verificar
Passe ambos os arquivos `score.yaml` para `score-compose generate` ou `score-k8s generate` e confirme no manifesto final que apenas uma instância do recurso com `id` compartilhado foi criada.

## Conexões
- [[score-containers-files-volumes-variables-probes-limits]] — Veja também: Score: Configuração de Containers (Variables, Files, Volumes, Probes e Resources).
- [[score-dns-route-exposicao-http-roteamento-ingress]] — Veja também: Score: Exposição de Tráfego Externo com Recursos dns e route.

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/score-compose/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
