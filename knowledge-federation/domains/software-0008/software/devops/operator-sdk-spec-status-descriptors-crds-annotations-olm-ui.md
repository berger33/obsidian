---
id: software.devops.tranche18.001760
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
fontes: ["https://sdk.operatorframework.io/docs/overview/", "https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md", "https://github.com/operator-framework/operator-sdk"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operator SDK: marcadores de `specDescriptors` e `statusDescriptors` (`+operator-sdk:csv:customresourcedefinitions`)

## Em uma frase
Em operadores Go gerenciados pelo Operator SDK, os marcadores de comentário `+operator-sdk:csv:customresourcedefinitions` aplicados nas structs e campos de `api/<version>/*_types.go` geram automaticamente os `specDescriptors`, `statusDescriptors` e recursos associados dentro do `ClusterServiceVersion` (CSV).

## Por que importa
Sem descritores semânticos no CSV, consoles visuais compatíveis com OLM (como o console web do OpenShift ou painéis de plataforma) exibem apenas um editor YAML bruto em vez de formulários tipados (controles numéricos de réplicas, seletores booleanos, badges de condição de saúde e links para Pods).

## Como funciona
Ao anotar um campo da struct `Spec` com `// +operator-sdk:csv:customresourcedefinitions:type=spec,displayName="Size",xDescriptors={"urn:alm:descriptor:com.tectonic.ui:podCount"}` e anotar a struct do CRD com os recursos Kubernetes gerenciados (`resources={{Deployment,v1,memcached-deployment}}`), o comando `make bundle` preenche automaticamente todas as seções do CSV exigidas pelos testes `olm-spec-descriptors-test` e `olm-status-descriptors-test` do `scorecard`.

## Exemplo
```go
// +kubebuilder:object:root=true
// +kubebuilder:subresource:status
// +operator-sdk:csv:customresourcedefinitions:resources={{Deployment,v1,memcached-deployment},{Pod,v1,}}
type Memcached struct {
    metav1.TypeMeta   `json:",inline"`
    metav1.ObjectMeta `json:"metadata,omitempty"`
    Spec              MemcachedSpec   `json:"spec,omitempty"`
    Status            MemcachedStatus `json:"status,omitempty"`
}
```

## Limites e trade-offs
Manter as anotações `+operator-sdk:csv:...` diretamente no código-fonte Go evita que regenerações de `make bundle` apaguem descritores editados manualmente no arquivo CSV.

## Como verificar
Adicione os marcadores `+operator-sdk:csv:customresourcedefinitions` nos campos de `Spec` e `Status`, execute `make bundle` e confirme a presença de `specDescriptors` e `statusDescriptors` no CSV gerado.

## Conexões
- [[operator-sdk-matriz-compatibilidade-kubernetes-client-go-lookup]] — Veja também: Operator SDK: auditoria de compatibilidade de versões com Kubernetes e `client-go` por tipo de projeto.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
