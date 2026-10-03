---
id: software.seguranca.tranche10.000993
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/inguardians/peirates/main/README.md", "https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md", "https://raw.githubusercontent.com/inguardians/peirates/main/go.mod"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Peirates na Nuvem (**AWS EKS / kOps & Google GKE**): Comandos **`aws-get-token`**, **`gcp-get-token`**, **`gcp-attack-kube-env`** e **`aws-attack-kops-1`**

## Em uma frase
Um cluster Kubernetes raramente vive no vácuo: seus nós Worker são instâncias EC2 na **AWS** ou VMs Compute Engine no **GCP** que possuem identidades de nuvem associadas na **API de Metadados da Instância (IMDS `169.254.169.254`)**.

## Por que importa
Conforme documentado na seção `Cloud credential and data access` (`docs/commands/README.md`), o Peirates automatiza os ataques clássicos de pivô Pod -> Cloud: **(1) `aws-get-token` (`12`)**, **`aws-enter-credentials` (`6`)** e **`aws-assume-role` (`7`)** — extraem as credenciais IAM temporárias da Role do nó EC2 (ou assumem outra IAM Role via STS) e permitem listar e ler buckets S3 diretamente pelo Peirates (**`aws-s3-ls` (`17`)**, **`aws-s3-ls-objects` (`18`)**)!

## Como funciona
No **GCP / GKE**, **`gcp-get-token` (`13`)** requisita o token OAuth2 da Service Account da VM no Metadata Server (`http://metadata.google.internal/computeMetadata/v1/`), e **`gcp-attack-kube-env` (`14`)** consulta o atributo **`attributes/kube-env`** nos metadados da instância GKE (que historicamente expunha certificados de bootstrap do Kubelet e chaves privadas!); já **`aws-attack-kops-1` (`16`)** e **`gcp-attack-kops-1` (`15`)** buscam buckets de estado de clusters provisionados com **kOps** (onde ficam as chaves privadas da CA raiz do cluster!)!

## Exemplo
```bash
# Executar em modo one-shot (-m) a verificacao de exposicao de credenciais AWS via IMDS a partir do Pod de teste
peirates -m 'aws-get-token'
```

## Limites e trade-offs
Como proteger seus clusters **EKS, GKE e kOps** contra todos os comandos de nuvem (`12` a `18`) do Peirates? **(1)** No **EKS**: exija **IMDSv2 com `HttpPutResponseHopLimit = 1`** nos Launch Templates dos nós e use **EKS Pod Identity / IRSA** (removendo permissões de S3/EC2 da Role do nó Worker!); **(2)** No **GKE**: habilite **GKE Workload Identity** e **`GKE Metadata Server`** (que oculta o endpoint `kube-env` da VM dos Pods!); e **(3)** Em clusters **kOps**: restrinja o acesso ao bucket S3/GCS de estado exclusivamente ao perfil IAM dos Control Planes!

## Como verificar
Teste sempre `aws-get-token` e `gcp-get-token` ao realizar pentests em clusters gerenciados na nuvem.

## Conexões
- [[peirates-coleta-tokens-secrets-secret-to-sa-kubectl-try-all-rbac]] — Veja também: Peirates: Coleta de Tokens (`list-secrets`, **`secret-to-sa`**), Prechecks **`set-auth-can-i`** e Força Bruta de Contextos (**`kubectl-try-all-until-success`**).
- [[peirates-execucao-remota-pods-exec-via-api-exec-via-kubelet-10250]] — Veja também: Peirates: Movimentação Lateral e Execução Remota em Pods via **`exec-via-api` (`21`)** e **Kubelet API (`exec-via-kubelet` `22` na Porta `10250`)**.
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.
- [[cdk-auditoria-cloud-metadata-imds-ak-leakage-istio-route-localnet]] — Referência cruzada direta com cdk-auditoria-cloud-metadata-imds-ak-leakage-istio-route-localnet.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
