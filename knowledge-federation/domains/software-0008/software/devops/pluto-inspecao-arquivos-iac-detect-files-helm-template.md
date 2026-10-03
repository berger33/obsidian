---
id: software.devops.tranche11.001063
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

# Inspeção de arquivos locais e Helm charts com o Pluto: detect-files -d e helm template | pluto detect -

## Em uma frase
Para repositórios de código e pipelines de CI, o Pluto oferece o subcomando **`pluto detect-files -d <diretório>`** para varrer árvores de arquivos YAML/templates e o comando **`helm template <chart-dir> | pluto detect -`** para validar a saída renderizada de Helm charts via `stdin`.

## Por que importa
Detectar uma `apiVersion` depreciada no momento em que o desenvolvedor abre um Pull Request (Shift-Left) é muito mais simples e seguro do que remediar dezenas de releases Helm em produção na véspera de uma janela de manutenção do cluster.

## Como funciona
Conforme mostra o guia oficial *QuickStart* (`pluto.docs.fairwinds.com/quickstart/`): (1) **`pluto detect-files -d <DIRECTORY>`** percorre recursivamente o diretório informado e lista cada recurso encontrado com `NAME`, `KIND`, `VERSION`, `REPLACEMENT`, `REMOVED` (`true`/`false`) e `DEPRECATED` (`true`/`false`); e (2) para charts Helm locais parametrizados (onde a `apiVersion` pode inclusive depender de condicionais `.Capabilities.KubeVersion`), o engenheiro executa **`helm template <chart-dir> | pluto detect -`**, canalizando os manifestos renderizados pelo Helm para a entrada padrão (`-`) do Pluto.

## Exemplo
```bash
# 1. Escanear recursivamente um diretório de manifestos Kubernetes em busca de apiVersions depreciadas
pluto detect-files -d ./k8s/manifests -o wide

# 2. Renderizar um Helm chart localmente e validar os manifestos via stdin no Pluto
helm template ./charts/meu-servico | pluto detect - -o wide
```

## Limites e trade-offs
Ao usar `helm template <chart-dir> | pluto detect -`, lembre-se de que charts que usam `.Capabilities.KubeVersion` no template Helm renderizarão a `apiVersion` correspondente à versão padrão do cliente Helm local, a menos que você passe `--kube-version <versão-alvo>` para o comando `helm template`.

## Como verificar
Execute `helm template --kube-version 1.31.0 ./charts/meu-servico | pluto detect -` para testar se o chart renderiza `apiVersions` válidas para a versão alvo do seu próximo upgrade de Kubernetes.

## Conexões
- [[pluto-armadilha-conversao-apiserver-last-applied-configuration]] — Veja também: Por que consultar o kube-apiserver diretamente oculta apiVersions depreciadas e como o Pluto contorna essa armadilha.
- [[pluto-deteccao-em-cluster-detect-helm-api-resources-all]] — Veja também: Auditoria em-cluster com o Pluto: detect-helm, detect-api-resources e detect-all-in-cluster.
- [[pluto-deteccao-apiversions-depreciadas-removidas-kubernetes]] — Referência cruzada direta com pluto-deteccao-apiversions-depreciadas-removidas-kubernetes.
- [[pluto-integracao-github-action-ci-cd-detect-files]] — Referência cruzada direta com pluto-integracao-github-action-ci-cd-detect-files.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://pluto.docs.fairwinds.com/quickstart/) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
