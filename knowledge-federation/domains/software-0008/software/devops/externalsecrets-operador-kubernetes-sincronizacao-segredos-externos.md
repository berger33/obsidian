---
id: software.devops.tranche10.000911
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
fontes: ["https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md", "https://external-secrets.io/latest/introduction/overview/", "https://github.com/external-secrets/external-secrets"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# External Secrets Operator (ESO): sincronização declarativa de gerenciadores de segredos externos com Kubernetes Secrets

## Em uma frase
O **External Secrets Operator (ESO)** (`external-secrets/external-secrets`, projeto da CNCF) é um operador Kubernetes que lê credenciais de APIs externas de gerenciamento de segredos (AWS Secrets Manager, HashiCorp Vault, Google Secret Manager, Azure Key Vault, IBM, Akeyless, CyberArk, Pulumi ESC e outros) e as injeta automaticamente em objetos `Secret` nativos do Kubernetes.

## Por que importa
Em fluxos GitOps (com Argo CD ou Flux), armazenar `Secret`s em texto claro no Git é inseguro, enquanto obrigar cada aplicação a integrar SDKs proprietários da AWS, GCP, Azure ou Vault acopla o código à nuvem. Segundo o README oficial e a página `API Overview` (`external-secrets.io/latest/introduction/overview/`), o ESO unifica projetos anteriores da comunidade em um único operador declarativo que mantém `Secret`s nativos sempre sincronizados com a fonte externa.

## Como funciona
O ESO estende a API do Kubernetes com Custom Resources (`apiVersion: external-secrets.io/v1`). O controlador monitora os recursos **`ExternalSecret`** no cluster, conecta-se ao provedor externo configurado no **`SecretStore`** ou **`ClusterSecretStore`**, busca os valores atuais dos segredos na API externa e cria/atualiza o recurso **`Kind=Secret`** nativo correspondente no namespace da aplicação. Se o valor do segredo mudar no gerenciador externo (por exemplo, após uma rotação de senha no AWS Secrets Manager ou no Vault), o controlador reconcilia periodicamente o estado no cluster e atualiza o `Secret` do Kubernetes automaticamente.

## Exemplo
```bash
# Instalar o External Secrets Operator no cluster Kubernetes via Helm chart oficial e verificar os CRDs registrados
helm repo add external-secrets https://charts.external-secrets.io
helm install external-secrets external-secrets/external-secrets -n external-secrets --create-namespace
kubectl get crds | grep external-secrets.io
```

## Limites e trade-offs
Como explica a seção `Roles and responsibilities` em `external-secrets.io/latest/introduction/overview/`, o ESO **consome e sincroniza** segredos a partir de provedores externos para dentro do Kubernetes (e opcionalmente faz push via `PushSecret`), mas o gerenciamento do ciclo de vida do segredo na origem (como políticas de rotação automática da senha diretamente no banco RDS) continua sendo responsabilidade do provedor externo de segredos (Vault, AWS Secrets Manager, etc.).

## Como verificar
Execute `kubectl get pods -n external-secrets` e `kubectl get externalsecrets -A` para confirmar que os pods do operador (`external-secrets`, `webhook` e `cert-controller`) estão saudáveis (`Running`).

## Conexões
- [[externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore]] — Veja também: External Secrets Operator: separação de responsabilidades entre SecretStore, ClusterSecretStore e ExternalSecret.
- [[vault-gerenciamento-centralizado-segredos-arquitetura-acesso]] — Referência cruzada direta com vault-gerenciamento-centralizado-segredos-arquitetura-acesso.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
