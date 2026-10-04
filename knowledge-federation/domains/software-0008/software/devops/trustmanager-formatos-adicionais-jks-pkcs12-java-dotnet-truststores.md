---
id: software.devops.tranche20.001915
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

# trust-manager Formatos Binários (`additionalFormats`): geração automática de truststores `JKS` e `PKCS#12` (`.p12`) para Java e .NET

## Em uma frase
Além do bundle em formato texto **PEM** padrão, o `trust-manager` gera automaticamente na mesma reconciliação truststores binários nos formatos **JKS (`spec.target.additionalFormats.jks`)** e **PKCS#12 (`spec.target.additionalFormats.pkcs12`)** prontos para montagem direta em aplicações Java (JVM) e .NET.

## Por que importa
Aplicações Java legadas e serviços Spring Boot frequentemente esperam um arquivo `-Djavax.net.ssl.trustStore=/etc/certs/bundle.jks` ou `.p12`, obrigando equipes a manterem *Init Containers* frágeis rodando `keytool -importcert` em todo Pod startup.

## Como funciona
Com `additionalFormats` configurado no `Bundle`, o próprio `trust-manager` grava as chaves binárias `bundle.jks` e `bundle.p12` diretamente dentro do `ConfigMap` ou `Secret` alvo em todos os namespaces selecionados, atualizando-as instantaneamente sempre que uma CA muda.

## Exemplo
```yaml
spec:
  sources:
    - useDefaultCAs: true
  target:
    configMap:
      key: "ca-bundle.pem"
    additionalFormats:
      jks:
        key: "truststore.jks"
        password: "changeit"
      pkcs12:
        key: "truststore.p12"
        password: ""
```

## Limites e trade-offs
Conforme explicado na documentação oficial do `cert-manager`, truststores contêm apenas certificados públicos (nunca chaves privadas); por isso, a senha padrão do JKS é `changeit` e a do PKCS#12 é `""` (password-less), existindo apenas para satisfazer leitores legados que exigem o campo de senha no formato de arquivo.

## Como verificar
Verifique as chaves geradas no ConfigMap alvo com `kubectl get configmap <bundle-name> -o jsonpath='{.data}'` e `'{.binaryData}'`.

## Conexões
- [[trustmanager-trust-namespace-isolamento-rbac-seguranca-fontes]] — Veja também: trust-manager Modelo de Segurança e *Trust Namespace*: por que fontes `Secret` e `ConfigMap` são restritas a um único namespace.
- [[trustmanager-alvos-secret-targets-namespaceselector-labels-annotations]] — Veja também: trust-manager Targets (`configMap` vs `secret`) e `namespaceSelector`: filtragem de namespaces e metadados para GitOps.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://cert-manager.io/docs/trust/trust-manager/) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
