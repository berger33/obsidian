---
id: software.devops.tranche11.001061
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

# Fairwinds Pluto: utilitário para detecção de apiVersions depreciadas e removidas do Kubernetes em IaC e releases Helm

## Em uma frase
O Fairwinds Pluto (`FairwindsOps/pluto`, Apache-2.0) é um utilitário de linha de comando e CI/CD projetado para localizar **`apiVersions` depreciadas (`DEPRECATED`) ou removidas (`REMOVED`)** do Kubernetes tanto em repositórios de Infrastructure-as-Code (manifestos YAML estáticos e Helm charts) quanto em clusters vivos (releases Helm e recursos de API).

## Por que importa
Antes de atualizar a versão do plano de controle do Kubernetes (por exemplo, em upgrades do EKS, GKE, AKS ou clusters autogerenciados), identificar todos os recursos que ainda foram aplicados usando `apiVersions` que serão removidas na versão alvo evita que deploys, Helm upgrades e reconciliações GitOps quebrem imediatamente após a atualização do cluster.

## Como funciona
Conforme explica a seção *Purpose* do README oficial (`FairwindsOps/pluto`), simplesmente pedir ao `kube-apiserver` um recurso (`kubectl get deployments.v1.apps -o yaml`) é enganoso e perigoso: mesmo que o Deployment tenha sido originalmente implantado como `extensions/v1beta1`, o API Server converte internamente o esquema e devolve o manifesto exibindo `apps/v1`, ocultando o fato de que seu pipeline ou release Helm ainda usa a versão depreciada. O Pluto resolve esse problema inspecionando diretamente a fonte da verdade — os arquivos YAML/Helm no disco (`detect-files` / `detect`), os segredos/configmaps das releases Helm no cluster (`detect-helm`) e a anotação `kubectl.kubernetes.io/last-applied-configuration` dos recursos da API (`detect-api-resources` / `detect-all-in-cluster`).

## Exemplo
```bash
# Instalar o Pluto via Homebrew Tap oficial e inspecionar um diretório de manifestos Kubernetes
brew install FairwindsOps/tap/pluto
pluto detect-files -d ./deploy/
```

## Limites e trade-offs
O Pluto verifica especificamente a depreciação e remoção de `apiVersions` (como `networking.k8s.io/v1beta1` → `networking.k8s.io/v1` ou `policy/v1beta1` `PodSecurityPolicy`); ele não audita configurações de segurança ou limites de CPU/memória dentro do spec (papel que cabe ao **Fairwinds Polaris**).

## Como verificar
Execute `pluto detect-files -d ./deploy/ -o wide` para visualizar as colunas `KIND`, `VERSION`, `REPLACEMENT`, `DEPRECATED`, `DEPRECATED IN`, `REMOVED` e `REMOVED IN`.

## Conexões
- [[pluto-armadilha-conversao-apiserver-last-applied-configuration]] — Veja também: Por que consultar o kube-apiserver diretamente oculta apiVersions depreciadas e como o Pluto contorna essa armadilha.
- [[pluto-inspecao-arquivos-iac-detect-files-helm-template]] — Referência cruzada direta com pluto-inspecao-arquivos-iac-detect-files-helm-template.
- [[polaris-motor-politicas-validacao-remediacao-kubernetes]] — Referência cruzada direta com polaris-motor-politicas-validacao-remediacao-kubernetes.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://pluto.docs.fairwinds.com/quickstart/) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
