---
id: software.devops.tranche10.000921
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

# Bitnami Sealed Secrets: criptografia assimétrica de Secrets para GitOps (kubeseal e controlador SealedSecret)

## Em uma frase
O **Sealed Secrets** (`bitnami-labs/sealed-secrets`) resolve o problema de armazenar segredos do Kubernetes em repositórios Git combinando dois componentes: o utilitário cliente **`kubeseal`** (que criptografa um `Secret` com chave pública em um CRD `SealedSecret`) e um **controlador no cluster** (o único que possui a chave privada para descriptografá-lo).

## Por que importa
Em fluxos puramente GitOps sem cofres externos de nuvem, toda a configuração do Kubernetes reside no Git, exceto os `Secret`s (pois `Secret.data` usa apenas codificação `base64`, não criptografia). Conforme explica o README oficial (`Problem: "I can manage all my K8s config in git, except Secrets."`), um `SealedSecret` é seguro para comitar no Git — até mesmo em um repositório público — porque ninguém além do controlador rodando no cluster alvo consegue descriptografá-lo.

## Como funciona
Na inicialização no cluster (por padrão no namespace `kube-system`), o `sealed-secrets-controller` gera um par de chaves criptográficas (chave privada guardada em um `Secret` no cluster + certificado de chave pública). Quando o desenvolvedor cria um manifesto `Secret` localmente (em memória, com `--dry-run=client -o yaml`) e o passa para o **`kubeseal`**, o `kubeseal` cifra cada valor usando a chave pública do controlador e gera um recurso **`apiVersion: bitnami.com/v1alpha1`**, **`kind: SealedSecret`** contendo `spec.encryptedData`. Ao aplicar esse `SealedSecret` no cluster (via `kubectl` ou Argo CD/Flux), o controlador o descriptografa em segundos e cria o `kind: Secret` normal correspondente.

## Exemplo
```bash
# Criar um Secret em memória (--dry-run=client) e selá-lo com kubeseal gerando mysealedsecret.yaml seguro para o Git
kubectl create secret generic mysecret --dry-run=client --from-literal=foo=bar -o yaml \
  | kubeseal -o yaml > mysealedsecret.yaml
```

## Limites e trade-offs
Como o `SealedSecret` funciona como um dispositivo *"write-only"* do ponto de vista do desenvolvedor (nem mesmo o autor original que rodou o `kubeseal` consegue reverter `encryptedData` para obter o texto claro sem a chave privada do cluster), nunca crie um `Secret` aplicando-o primeiro no cluster ou salvando o arquivo `secret.yaml` aberto no repositório Git antes de rodar o `kubeseal`: gere-o sempre via pipe com `--dry-run=client`.

## Como verificar
Aplique o `mysealedsecret.yaml` no cluster com `kubectl apply -f mysealedsecret.yaml` e verifique após alguns segundos com `kubectl get secret mysecret` que o controlador criou o `Secret` nativo descriptografado.

## Conexões
- [[sealedsecrets-escopos-criptografia-strict-namespace-wide-cluster-wide]] — Veja também: Bitnami Sealed Secrets: os 3 escopos de criptografia (strict, namespace-wide e cluster-wide) contra movimentação não autorizada.
- [[sealedsecrets-templates-metadados-ownerreferences-tipos-secret]] — Referência cruzada direta com sealedsecrets-templates-metadados-ownerreferences-tipos-secret.
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
