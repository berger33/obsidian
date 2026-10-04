---
id: software.devops.tranche11.001062
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
fontes: ["https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md", "https://pluto.docs.fairwinds.com/quickstart/", "https://pluto.docs.fairwinds.com/installation/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Por que consultar o kube-apiserver diretamente oculta apiVersions depreciadas e como o Pluto contorna essa armadilha

## Em uma frase
Consultar diretamente o `kube-apiserver` com `kubectl get <recurso> -o yaml` não revela se um objeto foi implantado com uma `apiVersion` depreciada porque o servidor converte automaticamente o objeto armazenado para a versão preferencial solicitada na query; o Pluto contorna isso analisando os metadados reais de aplicação e os registros do Helm.

## Por que importa
Muitos administradores de cluster executam um script com `kubectl get ingress -A -o yaml | grep apiVersion`, veem `networking.k8s.io/v1` em todas as linhas e assumem que o cluster está pronto para o upgrade, apenas para descobrir após o upgrade do Kubernetes que o Helm upgrade ou o pipeline de CD falha porque o manifesto original armazenado no release secret do Helm ainda declarava `networking.k8s.io/v1beta1`.

## Como funciona
Conforme documentado no README oficial (`FairwindsOps/pluto`), o Kubernetes mantém internamente uma representação hub do objeto no etcd e realiza conversão automática (*version conversion*) entre todas as versões servidas de um mesmo Group/Kind. Por isso, quando você pede `deployments.v1.apps`, o API Server devolve `apps/v1` independentemente de o manifesto ter sido enviado como `extensions/v1beta1`. Para descobrir a versão **originalmente enviada** no cluster vivo, o Pluto inspeciona: (1) os objetos `Secret` (Helm 3) ou `ConfigMap` (Helm 2) onde o Helm armazena o manifesto exato renderizado no momento do `helm install/upgrade` (`pluto detect-helm`); e (2) os metadados de recursos aplicados (`pluto detect-api-resources`).

## Exemplo
```bash
# Combinar todas as detecções em-cluster (releases Helm + recursos da API) com saída detalhada (-o wide)
pluto detect-all-in-cluster -o wide 2>/dev/null
```

## Limites e trade-offs
Para recursos aplicados diretamente na API do Kubernetes sem Helm (inspecionados por `pluto detect-api-resources`), a detecção em-cluster depende da presença da anotação `last-applied-configuration` (gerada por `kubectl apply`) ou metadados equivalentes; recursos criados de forma puramente imperativa sem `last-applied-configuration` são melhor auditados diretamente no repositório Git com `pluto detect-files`.

## Como verificar
Execute `pluto detect-all-in-cluster -o wide` no cluster antes de qualquer upgrade de versão minor do Kubernetes e compare com a saída de `pluto detect-files -d .` nos seus repositórios GitOps.

## Conexões
- [[pluto-deteccao-apiversions-depreciadas-removidas-kubernetes]] — Veja também: Fairwinds Pluto: utilitário para detecção de apiVersions depreciadas e removidas do Kubernetes em IaC e releases Helm.
- [[pluto-inspecao-arquivos-iac-detect-files-helm-template]] — Veja também: Inspeção de arquivos locais e Helm charts com o Pluto: detect-files -d e helm template | pluto detect -.
- [[pluto-deteccao-em-cluster-detect-helm-api-resources-all]] — Referência cruzada direta com pluto-deteccao-em-cluster-detect-helm-api-resources-all.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://pluto.docs.fairwinds.com/quickstart/) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
