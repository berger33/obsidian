---
id: software.devops.tranche11.001046
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
fontes: ["https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md", "https://goldilocks.docs.fairwinds.com/installation/", "https://goldilocks.docs.fairwinds.com/advanced/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Migração de registro e segurança de imagens no Goldilocks (v4.15.0+): Artifact Registry, tags imutáveis e assinatura

## Em uma frase
A partir da versão **`v4.15.0`**, as imagens oficiais do Goldilocks migraram do registro depreciado `quay.io/fairwinds/goldilocks` para **`us-docker.pkg.dev/fairwinds-ops/oss/goldilocks`**, passando a ser criptograficamente assinadas, com tags imutáveis (`v<major>.<minor>.<patch>`) e sem tags flutuantes (`latest`, `v4`, `v4.14`).

## Por que importa
Em ambientes corporativos que espelham imagens ou fixam repositórios em políticas de admissão (Kyverno, OPA Gatekeeper ou Popeye), continuar apontando para `quay.io/fairwinds/goldilocks` ou para tags flutuantes como `:latest` ou `:v4` resultará em imagens desatualizadas sem correções de CVE ou falha de `ImagePullBackOff` em novas versões.

## Como funciona
Conforme o aviso oficial no README do repositório (`FairwindsOps/goldilocks`), na transição `v4.14.19 → v4.15.0` a Fairwinds implementou três mudanças de segurança na cadeia de suprimentos: (1) mudança do endereço de registro para `us-docker.pkg.dev/fairwinds-ops/oss/goldilocks`; (2) eliminação de todas as tags flutuantes (`v4`, `v4.14`, `latest`); e (3) imutabilidade e assinatura das imagens publicadas, exigindo que os manifestos e valores Helm especifiquem a versão semântica completa (`us-docker.pkg.dev/fairwinds-ops/oss/goldilocks:v<major>.<minor>.<patch>`) ou o digest SHA256 (`@sha256:<digest>`).

## Exemplo
```yaml
# Configuração de imagem atualizada do Goldilocks (v4.15.0+) usando o novo registro oficial com tag semântica completa
image:
  repository: us-docker.pkg.dev/fairwinds-ops/oss/goldilocks
  tag: v4.15.0
  pullPolicy: IfNotPresent
```

## Limites e trade-offs
Como tags flutuantes (`v4`, `latest`) foram removidas em prol da reprodutibilidade e segurança da cadeia de suprimentos, atualizações de versão exigem atualizar explicitamente a tag `v<major>.<minor>.<patch>` ou o digest no seu repositório GitOps (por exemplo, automatizando PRs com Renovate ou Dependabot).

## Como verificar
Audite seus manifestos e charts com `grep -rn "quay.io/fairwinds/goldilocks" .` para garantir que todas as referências foram migradas para `us-docker.pkg.dev/fairwinds-ops/oss/goldilocks`.

## Conexões
- [[goldilocks-cli-dashboard-summary-exclusao-containers-sidecars]] — Veja também: Comandos da CLI do Goldilocks (dashboard, summary, create-vpas, delete-vpas) e exclusão de containers sidecar (--exclude-containers).
- [[goldilocks-interpretacao-qos-guaranteed-burstable-dashboard]] — Veja também: Interpretação das recomendações do Goldilocks Dashboard: classes de QoS Guaranteed versus Burstable no Kubernetes.
- [[goldilocks-dimensionamento-requests-limits-vpa-kubernetes]] — Referência cruzada direta com goldilocks-dimensionamento-requests-limits-vpa-kubernetes.
- [[polaris-migracao-registro-imagens-assinadas-imutaveis-v10-2]] — Referência cruzada direta com polaris-migracao-registro-imagens-assinadas-imutaveis-v10-2.
- [[pluto-migracao-registro-verificacao-cosign-checksums-v5-24]] — Referência cruzada direta com pluto-migracao-registro-verificacao-cosign-checksums-v5-24.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://goldilocks.docs.fairwinds.com/installation/) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
