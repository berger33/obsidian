---
id: software.devops.tranche11.001065
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

# Política de depreciação do Kubernetes no Pluto: diferença operacional entre DEPRECATED e REMOVED

## Em uma frase
Seguindo a *Kubernetes Deprecation Policy* oficial, o Pluto diferencia claramente entre uma versão de API **`DEPRECATED`** (que continua funcionando no cluster atual, mas emite avisos e tem remoção agendada) e uma versão **`REMOVED`** (que já deixou de ser servida pelo `kube-apiserver` na versão alvo).

## Por que importa
Em um planejamento de upgrade (por exemplo, do Kubernetes `v1.28` para `v1.29`), uma API marcada apenas como `DEPRECATED` (com `REMOVED IN` em uma versão futura como `v1.32`) gera dívida técnica que deve ser agendada no backlog, mas uma API marcada como **`REMOVED: true`** para a versão alvo é um **bloqueador imediato** que quebrará o upgrade.

## Como funciona
Conforme explica o README oficial (`FairwindsOps/pluto`) na seção *Kubernetes Deprecation Policy* e demonstra a saída `-o wide` do *QuickStart*: cada entrada do catálogo de versões do Pluto registra exatamente em qual release do Kubernetes a `apiVersion` foi depreciada (`DEPRECATED IN`, ex.: `v1.19.0`), em qual release ela foi ou será removida (`REMOVED IN`, ex.: `v1.22.0`) e qual é a `apiVersion` substituta (`REPLACEMENT`, ex.: `networking.k8s.io/v1` substituindo `networking.k8s.io/v1beta1` para `Ingress`). Com base na versão alvo comparada, o Pluto preenche os booleanos `DEPRECATED` e `REMOVED` e define o código de saída do processo.

## Exemplo
```bash
# Inspecionar manifestos em formato JSON ou wide para filtrar recursos com REMOVED == true
pluto detect-files -d ./deploy/ -o wide
```

## Limites e trade-offs
Quando você atualiza um `Helm chart` no repositório Git para corrigir a `apiVersion` de `networking.k8s.io/v1beta1` para `networking.k8s.io/v1`, você precisa aplicar esse `helm upgrade` no cluster **antes** de atualizar o plano de controle do Kubernetes para a versão onde `v1beta1` foi removida; caso contrário, o próprio `helm upgrade` poderá falhar ao tentar comparar o estado antigo da release com a API removida (exigindo o plugin `helm-mapkubeapis`).

## Como verificar
Revise nas colunas `DEPRECATED IN` e `REMOVED IN` de `pluto detect-all-in-cluster -o wide` se há algum recurso cuja versão de remoção seja menor ou igual à versão de Kubernetes para a qual o cluster será atualizado.

## Conexões
- [[pluto-deteccao-em-cluster-detect-helm-api-resources-all]] — Veja também: Auditoria em-cluster com o Pluto: detect-helm, detect-api-resources e detect-all-in-cluster.
- [[pluto-integracao-github-action-ci-cd-detect-files]] — Veja também: Automação do Pluto no GitHub Actions (FairwindsOps/pluto/github-action) para validação de Pull Requests.
- [[pluto-deteccao-apiversions-depreciadas-removidas-kubernetes]] — Referência cruzada direta com pluto-deteccao-apiversions-depreciadas-removidas-kubernetes.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://pluto.docs.fairwinds.com/quickstart/) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
