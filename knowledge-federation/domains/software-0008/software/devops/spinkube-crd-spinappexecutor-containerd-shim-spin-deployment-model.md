---
id: software.devops.tranche18.001786
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
fontes: ["https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md", "https://www.spinkube.dev/docs/overview/", "https://raw.githubusercontent.com/spinframework/spin/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SpinKube CRD `SpinAppExecutor`: configuração do modelo de execução (`containerd-shim-spin`) e `RuntimeClass`

## Em uma frase
O Custom Resource **`SpinAppExecutor`** (`core.spinkube.dev/v1alpha1`) instrui o Spin Operator sobre **como** uma `SpinApp` deve ser executada no cluster — seja delegando a execução diretamente ao shim `containerd-shim-spin` via `RuntimeClass` do Kubernetes, seja rodando através de uma imagem de container runner.

## Por que importa
Em clusters gerenciados onde o administrador tem controle dos nós (ou usa o `runtime-class-manager`), usar `runtimeClassName: wasmtime-spin-v2` oferece a maior densidade e velocidade; já em clusters restritos onde não é possível instalar shims customizados no `containerd` do nó, o `SpinAppExecutor` permite alternar a estratégia sem alterar os manifestos `SpinApp`.

## Como funciona
No manifesto do `SpinAppExecutor`, o campo `spec.createDeployment: true` e `spec.deploymentConfig.runtimeClassName: wasmtime-spin-v2` vinculam o operador à `RuntimeClass` associada ao handler `spin` no `containerd`.

## Exemplo
```yaml
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: wasmtime-spin-v2
handler: spin
---
apiVersion: core.spinkube.dev/v1alpha1
kind: SpinAppExecutor
metadata:
  name: containerd-shim-spin
spec:
  createDeployment: true
  deploymentConfig:
    runtimeClassName: wasmtime-spin-v2
    installDefaultCACerts: true
```

## Limites e trade-offs
A opção `installDefaultCACerts: true` em `deploymentConfig` garante que o ambiente minimalista do shim Wasm tenha o bundle de autoridades certificadoras raiz montado para validar chamadas HTTPS de saída (`allowed_outbound_hosts`).

## Como verificar
Execute `kubectl get runtimeclass` e `kubectl get spinappexecutors` para confirmar que o executor e a `RuntimeClass` estão prontos antes de criar uma `SpinApp`.

## Conexões
- [[spinkube-crd-spinapp-deploy-oci-replicas-variables-secrets]] — Veja também: SpinKube CRD `SpinApp`: implantação declarativa de artefatos OCI WebAssembly com réplicas, variáveis e recursos no Kubernetes.
- [[spinkube-runtime-class-manager-kwasm-instalacao-shims-nos-kubernetes]] — Veja também: SpinKube Runtime Class Manager (`Shim` CRD): instalação declarativa de shims Wasm (`containerd-shim-spin`) nos worker nodes.

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://www.spinkube.dev/docs/overview/) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
