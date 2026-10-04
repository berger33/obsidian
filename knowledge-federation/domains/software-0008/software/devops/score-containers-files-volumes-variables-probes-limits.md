---
id: software.devops.tranche12.001116
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

# Score: Configuração de Containers (Variables, Files, Volumes, Probes e Resources)

## Em uma frase
Dentro da seção `containers` do `score.yaml`, a especificação Score suporta definição detalhada de imagem, comando/argumentos, variáveis de ambiente, montagem de arquivos de configuração com interpolação, volumes persistentes, `livenessProbe`/`readinessProbe` HTTP e requests/limits de CPU e memória.

## Por que importa
Aplicações reais frequentemente precisam montar arquivos de configuração estruturados (JSON/YAML/INI) ou definir healthchecks HTTP e limites de recursos que funcionem de maneira coerente sem reescrever `ConfigMaps` manualmente.

## Como funciona
Enquanto o `score-k8s` traduz integralmente `resources.requests`, `resources.limits`, `livenessProbe.httpGet` e `readinessProbe.httpGet` em campos nativos do Pod Kubernetes, o `score-compose` valida esses campos contra o schema mas ignora limites e probes HTTP que não possuem equivalência confiável no Docker Compose local, preservando a execução do workload sem erro.

## Exemplo
```yaml
apiVersion: score.dev/v1b1
metadata:
  name: billing-service
containers:
  app:
    image: ghcr.io/org/billing:3.0.1
    resources:
      requests:
        cpu: "250m"
        memory: "256Mi"
      limits:
        cpu: "1000m"
        memory: "512Mi"
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
```

## Limites e trade-offs
Assumir que `livenessProbe.httpGet` e `resources.limits` declarados no `score.yaml` serão aplicados pelo Docker Compose local durante testes com `score-compose` leva a falsas suposições sobre comportamento de OOM ou reinício automático no laptop.

## Como verificar
Teste os limites de memória e as probes HTTP geradas pelo `score-k8s` em um cluster efêmero (KinD/k3d) além do teste funcional em `score-compose`.

## Conexões
- [[score-custom-provisioners-template-cmd-extensibilidade-plataforma]] — Veja também: Score: Provisionadores Customizados (template:// e cmd://) em score-compose e score-k8s.
- [[score-shared-resources-id-multi-workload-communication]] — Veja também: Score: Recursos Compartilhados entre Múltiplos Workloads (id e service-port).

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/score-compose/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
