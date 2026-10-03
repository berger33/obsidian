---
id: software.devops.tranche18.001789
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
fontes: ["https://www.spinkube.dev/docs/overview/", "https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md", "https://raw.githubusercontent.com/spinframework/spin/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SpinKube: auto-escalonamento horizontal (HPA) e *scale-to-zero* orientado a eventos com KEDA para `SpinApp`

## Em uma frase
Como o Spin Operator integra o CRD `SpinApp` às primitivas padrão do Kubernetes (incluindo o sub-recurso `/scale` e métricas de CPU/memória/requisições), aplicações WebAssembly no SpinKube suportam nativamente **HorizontalPodAutoscaler (HPA)** e escalonamento para zero (**scale-to-zero**) via **KEDA**.

## Por que importa
Em microsserviços com tráfego intermitente ou picos repentinos, containers tradicionais sofrem ao escalar de `0` para `1` réplica porque o pull e a inicialização da imagem levam vários segundos; como artefatos Spin pesam poucos megabytes e iniciam rapidamente no `containerd-shim-spin`, o scale-to-zero com KEDA torna-se prático.

## Como funciona
Configurando `spec.enableAutoscaling: true` na `SpinApp`, o operador delega o controle de `replicas` para um `HorizontalPodAutoscaler` ou `ScaledObject` do KEDA apontando para `scaleTargetRef: {apiVersion: core.spinkube.dev/v1alpha1, kind: SpinApp, name: ...}`.

## Exemplo
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: simple-spinapp-hpa
spec:
  scaleTargetRef:
    apiVersion: core.spinkube.dev/v1alpha1
    kind: SpinApp
    name: simple-spinapp
  minReplicas: 1
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

## Limites e trade-offs
Quando `enableAutoscaling: true` está ativo na `SpinApp`, não defina um valor fixo conflitante em `spec.replicas` no manifesto GitOps para que o controlador não reverta o número de réplicas ajustado pelo HPA/KEDA.

## Como verificar
Aplique o HPA apontando para a `SpinApp` e verifique com `kubectl get hpa` a vinculação ao `scaleTargetRef` do recurso.

## Conexões
- [[spin-registry-push-pull-distribuicao-artefatos-oci-wasm]] — Veja também: Spin OCI Distribution: empacotamento e distribuição de aplicações Wasm em Registries OCI (`spin registry push` / `pull`).
- [[spin-plugins-templates-extensibilidade-custom-triggers-wasi]] — Veja também: Spin: sistema de Plugins (`spin plugins`), Templates (`spin templates`) e criação de Custom Triggers.

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://www.spinkube.dev/docs/overview/) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
