---
id: software.devops.tranche11.001070
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

# Roteiro de pré-upgrade de clusters Kubernetes combinando Pluto, Polaris e Popeye

## Em uma frase
Em operações de plataforma, o Pluto atua como o verificador obrigatório de compatibilidade de APIs antes de qualquer upgrade de versão do Kubernetes, combinando a varredura estática nos repositórios GitOps (`pluto detect-files` / `helm template | pluto detect -`) com a varredura dinâmica no cluster vivo (`pluto detect-all-in-cluster`).

## Por que importa
Executar apenas a varredura no Git deixa passar charts instalados manualmente no cluster; executar apenas a varredura no cluster vivo deixa passar manifestos de Jobs sazonais ou pipelines de deploy que não estão rodando naquele instante no cluster, mas que falharão na próxima execução após o upgrade.

## Como funciona
Combinando os fluxos documentados no README e no *QuickStart* oficial do Pluto (`pluto.docs.fairwinds.com/quickstart/`), um checklist robusto de pré-upgrade de cluster executa quatro verificações: (1) `pluto detect-files -d .` em todos os repositórios GitOps e de aplicações; (2) `helm template <chart> | pluto detect -` para todos os Helm charts internos; (3) `pluto detect-all-in-cluster -o wide` conectado ao cluster que sofrerá o upgrade; e (4) uma varredura complementar de saúde do cluster vivo com o **Popeye** (código `403` de depreciação e checagem de recursos órfãos) e **Polaris** (conformidade dos workloads).

## Exemplo
```bash
# Script de pré-validação antes de atualizar um cluster Kubernetes (GitOps + Cluster Vivo)
set -e
echo "1. Verificando manifestos estáticos no repositório GitOps..."
pluto detect-files -d ./clusters/producao -o wide

echo "2. Verificando releases Helm e recursos aplicados no cluster vivo..."
pluto detect-all-in-cluster -o wide 2>/dev/null
```

## Limites e trade-offs
Como o Pluto opera de forma rápida e somente-leitura tanto no CI quanto contra o cluster vivo, não há impacto de performance ao executá-lo periodicamente (por exemplo, em um workflow semanal agendado no GitHub Actions ou CronJob no cluster) para antecipar depreciações muitos meses antes da janela de upgrade.

## Como verificar
Confirme que ambos os comandos (`detect-files` e `detect-all-in-cluster`) retornam código de saída `0` antes de iniciar a atualização do control plane do Kubernetes.

## Conexões
- [[pluto-exemplos-classicos-ingress-webhook-psp-migracao]] — Veja também: Casos reais de detecção do Pluto: MutatingWebhookConfiguration, Ingress (v1beta1 -> v1) e PodSecurityPolicy.
- [[pluto-deteccao-apiversions-depreciadas-removidas-kubernetes]] — Referência cruzada direta com pluto-deteccao-apiversions-depreciadas-removidas-kubernetes.
- [[popeye-codigos-erro-severidades-containers-pods-seguranca]] — Referência cruzada direta com popeye-codigos-erro-severidades-containers-pods-seguranca.
- [[polaris-auditoria-iac-cli-ci-cd-scores-danger-flags]] — Referência cruzada direta com polaris-auditoria-iac-cli-ci-cd-scores-danger-flags.

## Fontes
- [Fairwinds Pluto GitHub — README.md & QuickStart (API Server Conversion Pitfall, Deprecation Policy, detect-files, detect-helm & detect-all-in-cluster)](https://pluto.docs.fairwinds.com/quickstart/) — README e QuickStart oficiais do Fairwinds Pluto explicando a armadilha de conversão de versão do kube-apiserver, diferença entre DEPRECATED e REMOVED e uso de detect-files, detect-helm, detect-api-resources e detect-all-in-cluster; consultado em 2026-10-03.
- [Fairwinds Pluto Official Documentation — Installation & Artifact Verification (asdf, Homebrew, Cosign Verification & v5.24.0+ Images)](https://raw.githubusercontent.com/FairwindsOps/pluto/master/README.md) — Guia oficial de instalação do Pluto documentando plugin asdf, Homebrew Tap, verificação de assinatura criptográfica com Cosign (verify-blob e verify) e migração para imagens imutáveis na v5.24.0+; consultado em 2026-10-03.
- [Fairwinds Pluto — Official Documentation & Repository](https://pluto.docs.fairwinds.com/installation/) — Documentação e repositório oficial do Fairwinds Pluto; consultado em 2026-10-03.
