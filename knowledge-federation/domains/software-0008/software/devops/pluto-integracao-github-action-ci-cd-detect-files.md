---
id: software.devops.tranche11.001066
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

# Automação do Pluto no GitHub Actions (FairwindsOps/pluto/github-action) para validação de Pull Requests

## Em uma frase
O Pluto disponibiliza a GitHub Action oficial **`FairwindsOps/pluto/github-action`** para instalar o binário no runner de CI e executar `pluto detect-files` automaticamente em cada Pull Request, impedindo que novos manifestos com `apiVersions` depreciadas entrem no repositório.

## Por que importa
Mesmo após uma grande força-tarefa de limpeza de APIs depreciadas no repositório GitOps, desenvolvedores frequentemente copiam exemplos antigos da internet ou de fóruns contendo `batch/v1beta1` (`CronJob`) ou `autoscaling/v2beta2` (`HorizontalPodAutoscaler`). O gate no GitHub Actions bloqueia a regressão na origem.

## Como funciona
Conforme documenta a seção *GitHub Action Usage* no README oficial (`FairwindsOps/pluto`) e na página principal da documentação (`pluto.docs.fairwinds.com`), basta adicionar um passo com `uses: FairwindsOps/pluto/github-action@master` (ou fixado em tag/commit) para fazer o download do Pluto no ambiente do workflow e, no passo seguinte, executar `pluto detect-files -d <diretório>` sobre os diretórios de manifestos Kubernetes ou Kustomize do repositório.

## Exemplo
```yaml
# Workflow do GitHub Actions utilizando a action oficial do Fairwinds Pluto para validar manifestos
name: Pluto Kubernetes API Deprecation Check
on: [pull_request]
jobs:
  pluto:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Download Pluto
        uses: FairwindsOps/pluto/github-action@master
      - name: Use pluto to detect deprecated apiVersions
        run: |
          pluto detect-files -d ./deploy -o wide
```

## Limites e trade-offs
Se o repositório contiver Helm charts além de manifestos YAML estáticos, execute tanto `pluto detect-files -d ./deploy` quanto um passo de `helm template` canalizado para `pluto detect -`, garantindo cobertura completa das expressões condicionais dos templates Helm.

## Como verificar
Abra um Pull Request de teste contendo um manifesto com `apiVersion: extensions/v1beta1` e confirme que a etapa `pluto detect-files` falha o check do GitHub Actions identificando a substituição por `apps/v1`.

## Conexões
- [[pluto-diferenca-deprecated-vs-removed-politica-kubernetes]] — Veja também: Política de depreciação do Kubernetes no Pluto: diferença operacional entre DEPRECATED e REMOVED.
- [[pluto-instalacao-asdf-homebrew-scoop-binarios]] — Veja também: Métodos de instalação do Pluto: plugin asdf, Homebrew Tap, binários de release e Scoop.
- [[pluto-deteccao-apiversions-depreciadas-removidas-kubernetes]] — Referência cruzada direta com pluto-deteccao-apiversions-depreciadas-removidas-kubernetes.
- [[pluto-inspecao-arquivos-iac-detect-files-helm-template]] — Referência cruzada direta com pluto-inspecao-arquivos-iac-detect-files-helm-template.
- [[polaris-github-action-setup-polaris-automacao-pr]] — Referência cruzada direta com polaris-github-action-setup-polaris-automacao-pr.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://pluto.docs.fairwinds.com/quickstart/) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
