---
id: software.devops.tranche20.001913
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://cert-manager.io/docs/trust/trust-manager/", "https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md", "https://github.com/cert-manager/trust-manager"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# trust-manager Fontes Dinâmicas: uso de `selector.matchLabels` e `includeAllKeys: true` em `ConfigMaps` e `Secrets`

## Em uma frase
Nas fontes `configMap` e `secret` de um `Bundle`, o `trust-manager` suporta selecionar múltiplos recursos dinamicamente via **`selector.matchLabels`** (em vez de um `name` fixo) e incluir todos os certificados de todas as chaves de dados de um recurso via **`includeAllKeys: true`** (em vez de uma única `key`).

## Por que importa
Em clusters multi-região ou malhas federadas onde novos certificados de CAs regionais são provisionados dinamicamente com nomes gerados em runtime, editar o manifesto do `Bundle` manualmente a cada nova CA quebraria a automação.

## Como funciona
Conforme documentado na referência oficial do `trust-manager`, existem duas regras de exclusão mútua estritas: 1) `name` e `selector` são mutuamente exclusivos (exatamente um deve ser definido); e 2) `key` e `includeAllKeys` são mutuamente exclusivos (exatamente um deve ser definido). Você pode combiná-los (`selector` + `includeAllKeys: true`) para agregar automaticamente todos os certificados de todos os Secrets que possuam um label específico.

## Exemplo
```yaml
spec:
  sources:
    - secret:
        selector:
          matchLabels:
            pki.corp.io/trusted-ca: "true"
        includeAllKeys: true
  target:
    configMap:
      key: "all-regional-cas.pem"
```

## Limites e trade-offs
Todos os `Secrets` e `ConfigMaps` lidos como **fontes** (`spec.sources`) pelo `trust-manager` devem residir obrigatoriamente no **trust namespace** (por padrão `cert-manager`), mesmo que o `Bundle` seja um recurso cluster-scoped.

## Como verificar
Adicione o label `pki.corp.io/trusted-ca=true` a um novo Secret com certificado no trust namespace e confirme que o `ConfigMap` de destino é atualizado automaticamente.

## Conexões
- [[trustmanager-fontes-bundle-configmap-secret-inline-usedefaultcas]] — Veja também: trust-manager Fontes de Certificados (`spec.sources`): combinação de `configMap`, `secret`, `inLine` e `useDefaultCAs`.
- [[trustmanager-trust-namespace-isolamento-rbac-seguranca-fontes]] — Veja também: trust-manager Modelo de Segurança e *Trust Namespace*: por que fontes `Secret` e `ConfigMap` são restritas a um único namespace.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://cert-manager.io/docs/trust/trust-manager/) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
