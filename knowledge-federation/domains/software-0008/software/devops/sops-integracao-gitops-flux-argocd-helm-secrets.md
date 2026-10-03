---
id: software.devops.tranche10.000939
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
fontes: ["https://raw.githubusercontent.com/getsops/sops/main/README.rst", "https://getsops.io/docs/usage/common-operations/", "https://getsops.io/docs/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SOPS: integração nativa com pipelines GitOps no Kubernetes (Flux kustomize-controller, helm-secrets e KSOPS)

## Em uma frase
No ecossistema Kubernetes e GitOps, arquivos criptografados com SOPS são descriptografados nativamente em memória pelo **Flux CD (`kustomize-controller`)**, pelo plugin **`helm-secrets`** e pelo gerador Kustomize **KSOPS** no Argo CD.

## Por que importa
Diferentemente do Bitnami Sealed Secrets (que converte o `Secret` em um CRD `SealedSecret` específico de um único cluster), um `Kind: Secret` criptografado com SOPS (`--encrypted-regex '^(data|stringData)$'`) continua sendo um YAML de `Secret` padrão que pode ser descriptografado em múltiplos clusters (DR/multi-região) que compartilhem acesso à mesma chave KMS ou `age`.

## Como funciona
No fluxo GitOps com SOPS: (1) o desenvolvedor cifra os manifestos `Secret` (ou `values.enc.yaml` do Helm) com `sops` usando a chave pública `age` ou KMS do ambiente e faz commit no Git; (2) no **Flux CD**, o recurso `Kustomization` declara `spec.decryption.provider: sops` (referenciando um `Secret` `sops-age` no cluster com a chave privada `age.agekey` ou usando IAM Role KMS do pod do `kustomize-controller`), descriptografando os recursos em memória antes de aplicá-los; e (3) em **Helm / Argo CD**, plugins como `helm-secrets` ou `ksops` invocam a biblioteca do SOPS durante a renderização dos templates para injetar os valores descriptografados sem nunca salvá-los abertos no repositório.

## Exemplo
```yaml
# Exemplo de configuração de descriptografia nativa SOPS em uma Kustomization do Flux CD (kustomize.toolkit.fluxcd.io)
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: apps-prod
  namespace: flux-system
spec:
  interval: 10m
  path: ./clusters/prod
  prune: true
  sourceRef:
    kind: GitRepository
    name: fleet-infra
  decryption:
    provider: sops
    secretRef:
      name: sops-age
```

## Limites e trade-offs
Quando você utiliza SOPS com Flux CD ou Argo CD, o controlador GitOps descriptografa o manifesto em memória e aplica um `Kind: Secret` nativo no API Server do Kubernetes; portanto, qualquer usuário com permissão RBAC de `get secrets` naquele namespace poderá ler o segredo aplicado no cluster, e o `etcd` do cluster deve estar com `EncryptionConfiguration` (encryption at rest) habilitada.

## Como verificar
Verifique no status da `Kustomization` do Flux (`flux get kustomizations`) ou na saída de `helm secrets dec values.enc.yaml` que os manifestos criptografados com SOPS são descriptografados sem erros.

## Conexões
- [[sops-arquivos-binarios-exec-env-exec-file-processos]] — Veja também: SOPS: criptografia de arquivos binários e injeção segura em processos em memória (sops exec-env e sops exec-file).
- [[sops-compatibilidade-formato-historico-mozilla-cncf-filestatus]] — Veja também: SOPS: governança CNCF Sandbox, garantia de retrocompatibilidade do formato 1.0+ e comando sops filestatus.
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.
- [[sops-criptografia-parcial-chaves-encrypted-regex-mac]] — Referência cruzada direta com sops-criptografia-parcial-chaves-encrypted-regex-mac.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/common-operations/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
