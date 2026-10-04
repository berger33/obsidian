---
id: software.devops.tranche10.000923
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md", "https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md", "https://github.com/bitnami-labs/sealed-secrets"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Bitnami Sealed Secrets: seção spec.template, labels/annotations do Secret gerado, funções Sprig e ownerReferences

## Em uma frase
Assim como um `Deployment` define um template de `Pod`, o recurso `SealedSecret` possui a seção **`spec.template`** para definir o `type` (ex.: `kubernetes.io/dockerconfigjson`), `immutable`, `metadata` (labels e annotations separadas do CRD) e transformações `data` com templates Go/Sprig do `Secret` gerado.

## Por que importa
As anotações e labels colocadas no próprio objeto `SealedSecret` (como anotações do Argo CD ou do `kubectl`) não são necessariamente as anotações que a aplicação precisa ver no `Secret` final (como `jenkins.io/credentials-type`). A seção `SealedSecrets as templates for secrets` do README oficial explica essa separação.

## Como funciona
Quando o controlador descriptografa os itens de `spec.encryptedData`, ele usa **`spec.template`** para construir o objeto `Secret` resultante: (1) copia `spec.template.metadata` (labels e annotations) e adiciona automaticamente um **`ownerReferences`** apontando para o `SealedSecret` pai (de modo que deletar o `SealedSecret` apaga automaticamente o `Secret` dependente, a menos que a anotação `sealedsecrets.bitnami.com/skip-set-owner-references: "true"` seja usada); (2) copia os campos `type` e `immutable`; e (3) avalia opcionalmente expressões Go Text Template + biblioteca **Sprig** (exceto `env`, `expandenv` e `getHostByName` por segurança) em `spec.template.data` para montar arquivos de configuração complexos a partir dos valores descriptografados.

## Exemplo
```yaml
# Exemplo de SealedSecret usando spec.template para definir tipo dockerconfigjson, imutabilidade e labels no Secret final
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: registry-creds
  namespace: mynamespace
spec:
  encryptedData:
    .dockerconfigjson: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq...
  template:
    type: kubernetes.io/dockerconfigjson
    immutable: true
    metadata:
      labels:
        app.kubernetes.io/part-of: checkout
```

## Limites e trade-offs
Se você marcar `immutable: true` dentro de `spec.template`, o `Secret` criado no Kubernetes será imutável (protegido pelo API Server contra alterações e aliviando a carga de watches no `kubelet`); contudo, se posteriormente você atualizar o `encryptedData` daquele mesmo `SealedSecret` sem trocar o nome, o controlador não conseguirá atualizar o `Secret` imutável in-place a menos que o `Secret` antigo seja recriado.

## Como verificar
Inspecione o `Secret` gerado pelo controlador com `kubectl get secret <nome> -o yaml` e confirme a presença de `ownerReferences` apontando para `kind: SealedSecret` e das labels definidas em `spec.template.metadata`.

## Conexões
- [[sealedsecrets-escopos-criptografia-strict-namespace-wide-cluster-wide]] — Veja também: Bitnami Sealed Secrets: os 3 escopos de criptografia (strict, namespace-wide e cluster-wide) contra movimentação não autorizada.
- [[sealedsecrets-certificado-publico-fetch-cert-offline-url]] — Veja também: Bitnami Sealed Secrets: obtenção da chave pública (--fetch-cert) e selamento offline (--cert e SEALED_SECRETS_CERT).
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.
- [[sealedsecrets-atualizacao-merge-into-raw-mode-validacao]] — Referência cruzada direta com sealedsecrets-atualizacao-merge-into-raw-mode-validacao.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
