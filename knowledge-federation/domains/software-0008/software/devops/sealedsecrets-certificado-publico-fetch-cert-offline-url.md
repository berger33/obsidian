---
id: software.devops.tranche10.000924
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

# Bitnami Sealed Secrets: obtenção da chave pública (--fetch-cert) e selamento offline (--cert e SEALED_SECRETS_CERT)

## Em uma frase
Para selar segredos sem exigir acesso em tempo real ao API Server do cluster, é possível exportar o certificado público do controlador com `kubeseal --fetch-cert > mycert.pem` (ou dos logs do controlador) e usá-lo offline via `--cert` (arquivo local ou URL HTTPS) ou variável `SEALED_SECRETS_CERT`.

## Por que importa
Conforme destaca a seção `Public key / Certificate` do README oficial e o documento `docs/GKE.md`, buscar o certificado em tempo de execução via API proxy do Kubernetes exige que o desenvolvedor tenha acesso direto ao cluster no momento de rodar o `kubeseal` e falha em clusters privados (como Private GKE Clusters) onde há firewall entre o control plane e a porta `8080` dos nós.

## Como funciona
O certificado público de selamento não é uma informação secreta (ele serve apenas para criptografar dados que só o controlador sabe abrir). A equipe de plataforma pode extraí-lo com **`kubeseal --fetch-cert > pub-cert.pem`** (ou copiá-lo do log de inicialização do controlador) e publicá-lo em uma URL interna confiável ou no repositório. Os desenvolvedores então selam segredos de forma 100% offline executando **`kubeseal --cert pub-cert.pem`** ou **`kubeseal --cert https://intranet.empresa.com/certs/prod-sealed-secrets.pem`** (ou exportando **`SEALED_SECRETS_CERT`** no `.envrc` do `direnv`).

## Exemplo
```bash
# Exportar o certificado público do controlador uma vez e usá-lo para selar segredos offline sem conexão ao cluster
kubeseal --fetch-cert > cluster-pub-cert.pem
kubeseal --cert cluster-pub-cert.pem -o yaml < secret.yaml > sealed-secret.yaml
```

## Limites e trade-offs
Como o controlador do Sealed Secrets renova automaticamente suas chaves de selamento a cada **30 dias** por padrão (mantendo as chaves privadas anteriores ativas para continuar descriptografando segredos antigos), se os desenvolvedores usarem um arquivo `--cert mycert.pem` salvo localmente no disco, é boa prática atualizar periodicamente esse certificado offline (ou apontar `SEALED_SECRETS_CERT` para uma URL interna atualizada automaticamente) para que novos segredos sempre usem a chave mais recente.

## Como verificar
Desconecte sua máquina do cluster (por exemplo, passando `--kubeconfig=/dev/null`) e execute `kubeseal --cert cluster-pub-cert.pem -o yaml < secret.yaml` confirmando que o `SealedSecret` é gerado sem nenhuma chamada de rede ao Kubernetes.

## Conexões
- [[sealedsecrets-templates-metadados-ownerreferences-tipos-secret]] — Veja também: Bitnami Sealed Secrets: seção spec.template, labels/annotations do Secret gerado, funções Sprig e ownerReferences.
- [[sealedsecrets-rotacao-chaves-sealing-key-renewal-re-encrypt]] — Veja também: Bitnami Sealed Secrets: renovação periódica de chaves de selamento (30 dias), rotação de segredos e re-encryption.
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.
- [[sealedsecrets-gke-privado-firewall-8080-warden-service-proxier]] — Referência cruzada direta com sealedsecrets-gke-privado-firewall-8080-warden-service-proxier.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
