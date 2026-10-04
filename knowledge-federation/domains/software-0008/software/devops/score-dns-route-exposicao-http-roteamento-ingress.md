---
id: software.devops.tranche12.001118
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
fontes: ["https://raw.githubusercontent.com/score-spec/spec/main/README.md", "https://raw.githubusercontent.com/score-spec/score-compose/main/README.md", "https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Score: Exposição de Tráfego Externo com Recursos dns e route

## Em uma frase
No Score, a exposição de rotas HTTP externas para um workload é modelada combinando um recurso `type: dns` (que provisiona ou aloca um hostname) com um recurso `type: route` que vincula `host`, `path` e a `port` do serviço.

## Por que importa
Configurar roteamento HTTP em Docker Compose (via proxy reverso local) e no Kubernetes (via `Ingress` ou Gateway API `HTTPRoute`) exige sintaxes radicalmente diferentes se o desenvolvedor tiver que escrever os manifestos diretamente.

## Como funciona
No `score.yaml`, o recurso `dns` expõe `${resources.dns.host}`, que é referenciado nos parâmetros do recurso `route` (`host: ${resources.dns.host}`, `path: /`, `port: 8080`). No `score-compose`, isso provisiona roteamento local acessível no navegador; no `score-k8s`, gera os objetos de roteamento Kubernetes correspondentes ao controlador do cluster.

## Exemplo
```yaml
service:
  ports:
    web:
      port: 8080
resources:
  dns:
    type: dns
  route:
    type: route
    params:
      host: ${resources.dns.host}
      path: /api
      port: 8080
```

## Limites e trade-offs
Apontar `params.port` no recurso `route` para uma porta numérica que não foi declarada na seção `service.ports` do workload causa falha de validação ou cria regras de roteamento apontando para um Service inexistente.

## Como verificar
Verifique se o valor de `params.port` em `route` coincide exatamente com uma porta declarada em `service.ports` e teste o roteamento HTTP após o deploy.

## Conexões
- [[score-shared-resources-id-multi-workload-communication]] — Veja também: Score: Recursos Compartilhados entre Múltiplos Workloads (id e service-port).
- [[score-k8s-patch-templates-post-processing-customizacao]] — Veja também: Score: Pós-Processamento de Manifestos no score-k8s com --patch-templates.

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/score-compose/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
