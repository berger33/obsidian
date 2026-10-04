---
id: software.devops.tranche11.001064
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://pluto.docs.fairwinds.com/quickstart/", "https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md", "https://pluto.docs.fairwinds.com/installation/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Auditoria em-cluster com o Pluto: detect-helm, detect-api-resources e detect-all-in-cluster

## Em uma frase
Para auditar clusters Kubernetes em execução, o Pluto disponibiliza três comandos especializados: **`pluto detect-helm`** (inspeciona releases Helm 2 e Helm 3 no cluster, com filtro opcional `-n <namespace>`), **`pluto detect-api-resources`** (inspeciona recursos da API no cluster) e **`pluto detect-all-in-cluster`** (combina ambas as detecções em uma única execução).

## Por que importa
Em clusters onde diferentes equipes instalam charts de terceiros diretamente via Helm ou controladores GitOps, o repositório de código de uma aplicação individual não mostra o panorama completo do cluster. Os comandos em-cluster do Pluto revelam exatamente qual release Helm em qual namespace ainda carrega uma `apiVersion` depreciada ou removida.

## Como funciona
Conforme documentado no *QuickStart* oficial (`pluto.docs.fairwinds.com/quickstart/`): (1) **`pluto detect-helm -owide`** (ou restrito a um único namespace com `pluto detect-helm -n cert-manager -owide`) lê os metadados das releases Helm no cluster e exibe o `NAME` no formato `<release>/<recurso>`, `NAMESPACE`, `KIND`, `VERSION`, `REPLACEMENT`, `DEPRECATED`, `DEPRECATED IN`, `REMOVED` e `REMOVED IN`; (2) **`pluto detect-api-resources -owide`** inspeciona os recursos diretamente na API do cluster; e (3) **`pluto detect-all-in-cluster -o wide`** executa todas as detecções em-cluster disponíveis em uma única tabela consolidada.

## Exemplo
```bash
# Auditar todas as releases Helm em um namespace específico com saída detalhada (-owide)
pluto detect-helm -n cert-manager -owide

# Auditar simultaneamente todas as releases Helm e recursos de API em todo o cluster
pluto detect-all-in-cluster -o wide 2>/dev/null
```

## Limites e trade-offs
Quando uma `apiVersion` foi totalmente removida sem substituto direto no core do Kubernetes (como `PodSecurityPolicy` em `policy/v1beta1`, depreciada na `v1.21.0` e removida na `v1.25.0`), a coluna `REPLACEMENT` na saída do Pluto aparece em branco, indicando que a migração exige adotar uma nova arquitetura (como Pod Security Admission ou Kyverno/Polaris) em vez de apenas trocar a string `apiVersion`.

## Como verificar
Execute `pluto detect-all-in-cluster -o wide` usando um `kubeconfig` com permissão de leitura sobre `secrets`, `configmaps` e recursos do cluster, verificando se alguma linha apresenta `REMOVED: true` para a versão alvo.

## Conexões
- [[pluto-inspecao-arquivos-iac-detect-files-helm-template]] — Veja também: Inspeção de arquivos locais e Helm charts com o Pluto: detect-files -d e helm template | pluto detect -.
- [[pluto-diferenca-deprecated-vs-removed-politica-kubernetes]] — Veja também: Política de depreciação do Kubernetes no Pluto: diferença operacional entre DEPRECATED e REMOVED.
- [[pluto-deteccao-apiversions-depreciadas-removidas-kubernetes]] — Referência cruzada direta com pluto-deteccao-apiversions-depreciadas-removidas-kubernetes.
- [[pluto-armadilha-conversao-apiserver-last-applied-configuration]] — Referência cruzada direta com pluto-armadilha-conversao-apiserver-last-applied-configuration.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://pluto.docs.fairwinds.com/quickstart/) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
